import aiohttp
import bs4
from colorama import Fore
import time
import asyncio


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f"https://talkpython.fm/{episode_number}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            html_bin = await resp.read()
            html = html_bin.decode("utf-8")
            return (html, episode_number)


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, "html.parser")
    header = soup.select_one("h1")
    if not header:
        return "MISSING"

    return header.text.strip()


async def get_title_range():
    # Please keep this range pretty small to not DDoS my site. ;)
    tasks = []
    for n in range(185, 200):
        tasks.append(asyncio.create_task(get_html(n)))

    results = await asyncio.gather(*tasks)

    for html, episode_number in results:
        title = get_title(html, episode_number)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


def main():
    s = time.perf_counter()
    asyncio.run(get_title_range())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    print("Done.")


if __name__ == "__main__":
    main()
