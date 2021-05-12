from typing import List, Tuple
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient, SCPException


class RemoteClient:
    """Client to interact with a remote host via SSH & SCP."""

    def __init__(
        self,
        host: str,
        user: str,
        password: str = None,
        passphrase: str = None,
        port: int = 22,
    ) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.passphrase = passphrase
        self.port = port
        self.ssh_client = None
        self.scp_client = None

    def __connect(self, auto_add: bool = False):
        """Open connection to remote host."""
        self.ssh_client = SSHClient()
        if auto_add:
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        else:
            self.ssh_client.load_system_host_keys()
        self.ssh_client.connect(
            self.host,
            username=self.user,
            port=self.port,
            passphrase=self.passphrase,
            password=self.password,
        )
        self.scp_client = SCPClient(self.ssh_client.get_transport())
        return self.ssh_client

    def disconnect(self):
        """Close ssh connection."""
        self.ssh_client.close()
        self.scp_client.close()

    def __check_shell(self) -> bool:
        stdin, stdout, stderr = self.ssh_client.exec_command("echo $SHELL")
        response = stdout.readlines()
        if response:
            output = response[0].strip()
            if output == "/bin/bash":
                return True
        return False

    def __execute_command(self, command: str) -> Tuple:
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        status_code = stdout.channel.recv_exit_status()
        std_out_response = "\n".join(stdout.readlines())
        std_err_response = "\n".join(stderr.readlines())
        return (status_code, std_out_response, std_err_response)

    def execute_commands(self, commands: List):
        """Execute multiple commands in succession."""
        results = []
        if not self.ssh_client:
            self.ssh_client = self.__connect()
        if self.__check_shell():
            for command in commands:
                results.append(self.__execute_command(command))
            return results
        else:
            print("This is not a bash shell.")

    def upload_single_file(self, local_file_path: str, remote_path: str):
        if not self.ssh_client:
            self.ssh_client = self.__connect()

        try:
            self.scp_client.put(
                local_file_path, recursive=True, remote_path=remote_path
            )
        except SCPException as err:
            print(err)
        else:
            print(f"File {local_file_path} uploaded to {remote_path}.")
