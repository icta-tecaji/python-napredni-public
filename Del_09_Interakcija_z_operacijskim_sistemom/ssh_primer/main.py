from sshhelper.client import RemoteClient


if __name__ == "__main__":

    client = RemoteClient(
        host="212.101.137.47", port=22, user="sshtest", passphrase="leons"
    )
    results = client.execute_commands(["ls ~"])
    for result in results:
        print(result)
        print("---------------------")
    client.upload_single_file("myfile.txt", "~")
    results = client.execute_commands(["ls ~"])
    for result in results:
        print(result)
        print("---------------------")

    client.disconnect()
