import subprocess

def main():
    # Start cec-client in background
    cec_process = subprocess.Popen(
        ["cec-client", "-d", "1"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        bufsize = 1
    )

    # Wait for cec to be ready for input
    wait_for_ready(cec_process)
    print("Done")
    
def wait_for_ready(process):
    print("Waiting for Ready")
    for line in iter(process.stdout.readline, ''):
        print(line.strip())
        if "waiting for input" in line:
            print("Ready")
            break


main()