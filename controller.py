import subprocess

def main():
    # Start cec-client in background
    cec_process = subprocess.Popen(
        ["cec-client", "-s", "-d", "1"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )

    while True:
        print(cec_process.stdout)

main()