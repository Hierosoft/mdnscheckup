# mdnscheckup/mdnscheckup.py
import os
import sys
from zeroconf import Zeroconf, ServiceBrowser, ServiceListener

if __name__ == "__main__":
    MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
    REPO_PATH = os.path.dirname(MODULE_PATH)
    sys.path.insert(0, REPO_PATH)

from mndscheckup.ipv6check import (
    # is_ipv6_enabled_windows,
    main as ipv6check_main,
)


class MDNSListener(ServiceListener):
    def __init__(self):
        self.devices = []

    def add_service(self, zeroconf, service_type, name):
        self.devices.append(name)

def check_mdns():
    zeroconf = Zeroconf()
    listener = MDNSListener()

    try:
        browser = ServiceBrowser(zeroconf, "_services._dns-sd._udp.local.", listener)
        # Allow some time to discover services
        import time
        time.sleep(2)

        devices = listener.devices
        mdns_status = len(devices) > 0
    finally:
        zeroconf.close()

    return mdns_status, devices


def main():
    # is_enabled = True if (ipv6check_main() == 0) else False
    ipv6check_main()

    mdns_status, devices = check_mdns()
    print(f"MDNS Status: Devices listed: {mdns_status}")
    if mdns_status:
        print(f"Devices: {devices}")
    return 0 if mdns_status else 1


if __name__ == "__main__":
    sys.exit(main())
