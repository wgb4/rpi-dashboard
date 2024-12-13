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

    # Wait for cec to be ready for input
    wait_for_ready(cec_process)
    
def wait_for_ready(process):
    while True:
        output = process.stdout.readline()
        if output:
            print(output.strip())
            if "waiting for input" in output:
                print("Readty for input...")
                break


main()