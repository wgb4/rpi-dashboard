import subprocess

def main():
    # Start cec-client in background
    cec_process = connect_cec()

    # Wait for cec to be ready for input
    wait_for_ready(cec_process)

    # turn_on_tv(cec_process)
    turn_off_tv(cec_process)

    print("Exiting")
    disconnect_cec(cec_process)
    
def connect_cec():
    return subprocess.Popen(
        ["cec-client"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        bufsize = 1
    )

def wait_for_ready(process):
    print("Waiting for Ready")
    for line in iter(process.stdout.readline, ''):
        print(line.strip())
        if "waiting for input" in line:
            print("Ready")
            break

def turn_on_tv(process):
    print("Turning on TV")
    process.stdin.write("on 0\n")
    process.stdin.flush()

def turn_off_tv(process):
    print("Turning off TV")
    process.stdin.write("standby 0\n")
    process.stdin.flush()

def disconnect_cec(process):
    print("Disconnecting cec cleanly")
    process.stdin.write("q")
    process.stdin.flush

main()