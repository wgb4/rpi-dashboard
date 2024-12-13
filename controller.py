import subprocess

def main():
    tv_address = 0

    get_tv_status(0)


def get_tv_status(tv_address):
    # Run cec-client, scan for devices
    result = subprocess.run(["cec-client", "-s", "-d", "1"], input="scan\n", text=True, capture_output=True)
    print(result.stdout)


main()