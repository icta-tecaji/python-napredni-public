import logging
import asyncio
import random
import string
import uuid
import signal


import attr


# NB: Using f-strings with log messages may not be ideal since no matter
# what the log level is set at, f-strings will always be evaluated
# whereas the old form ("foo %s" % "bar") is lazily-evaluated.
# But I just love f-strings.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


class RestartedFailed(Exception):
    pass


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)
    restarted = attr.ib(repr=False, default=False)
    saved = attr.ib(repr=False, default=False)
    acked = attr.ib(repr=False, default=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


def handle_exception(loop, context):
    msg = context.get("exception", context["message"])
    logging.error(f"Caught exception: {msg}")
    logging.info("Shutting down...")
    asyncio.create_task(shutdown(loop))


def handle_results(results, msg):
    for result in results:
        if isinstance(result, RestartedFailed):
            logging.error(f"Restart fail: {msg.hostname}")
        elif isinstance(result, Exception):
            logging.error(f"Handling general error: {result}")


async def publish(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)

        # publish an item
        asyncio.create_task(queue.put(msg))
        logging.debug(f"Published message {msg}")
        await asyncio.sleep(random.random())


async def restart_host(msg):
    # simuliram čaš potreben za restart
    await asyncio.sleep(random.random())
    # simuliramo realno napako
    if random.randrange(1, 8) == 3:
        raise RestartedFailed(f"Could not restart {msg}")
    msg.restarted = True
    logging.info(f"Restarted {msg.hostname}")


async def save(msg):
    # simuliram čaš potreben za dodajanje v bazo
    await asyncio.sleep(random.random())
    if random.randrange(1, 10) == 3:
        raise Exception(f"Could not save {msg}")
    msg.saved = True
    logging.info(f"Saved {msg} into database")


async def cleanup(msg):
    # simuliram čaš potreben za ack
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"Done. Acked {msg}")


async def handle_message(msg):
    results = await asyncio.gather(save(msg), restart_host(msg), return_exceptions=True)
    handle_results(results, msg)
    await cleanup(msg)


async def consume(queue):
    """Consumer client to simulate subscribing to a publisher.
    Args:
        queue (queue.Queue): Queue from which to consume messages.
    """
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        # simuliramo realno napako
        if random.randrange(1, 25) == 3:
            raise Exception(f"Could not consume {msg}")

        # process the msg
        logging.info(f"Consumed {msg}")
        asyncio.create_task(handle_message(msg))


async def shutdown(loop, signal=None):
    if signal:
        logging.info(f"Prijeti zunanji signal {signal.name}")

    logging.info("Closing database connection")
    logging.info("Sporocamo v queue (nack)")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    logging.info(f"Cancelling {len(tasks)} tasks.")
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info("Dodajanje metrik")
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(loop, signal=s))
        )

    loop.set_exception_handler(handle_exception)
    queue = asyncio.Queue()

    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()

    finally:
        loop.close()
        logging.info("Uspešno smo zaustavili našo storitev.")


if __name__ == "__main__":
    main()
