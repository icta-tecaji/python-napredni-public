import subprocess
from typing import List, Tuple


def run_external_command(commad: str, timeout=None) -> Tuple[int, List, List]:
    completed = subprocess.run(
        commad, shell=True, capture_output=True, text=True, timeout=timeout
    )
    status_code = completed.returncode
    stdoutput = []
    stderror = []

    if status_code == 0:
        stdoutput = completed.stdout.split("\n")
    else:
        print(f"ERROR: {status_code}")
        stderror = completed.stderr.split("\n")
    return (completed.returncode, stdoutput, stderror)


if __name__ == "__main__":
    # completed = subprocess.run("echo $HOME", shell=True)
    # print(f"return code: {completed.returncode}")

    results = run_external_command("ps -aux")
    print(results)
