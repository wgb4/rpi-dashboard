import subprocess

def main():
    scan_output = run_cec_client("scan")
    print(scan_output)


def run_cec_client(command):
    # Run cec-client, scan for devices
    result = subprocess.run(["cec-client", "-s", "-d", "1"], input=f"{command}\n", text=True, capture_output=True)
    return result.stdout

main()