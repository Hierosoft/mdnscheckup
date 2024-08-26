import ifaddr
import platform
import sys

if platform.system() == "Windows":
    # import win32api  # requires pywin32
    import win32con  # requires pywin32
    import winreg  # requires pywin32


def is_ipv6_enabled_windows():
    """Check if IPv6 is enabled on each adapter on Windows.

    Returns:
        dict: A dictionary mapping adapter `nice_name` to a boolean indicating
              if IPv6 is enabled.
    """
    if platform.system() != "Windows":
        raise NotImplementedError("This function is only implemented for Windows.")

    adapters = ifaddr.get_adapters()
    ipv6_enabled_dict = {}

    for adapter in adapters:
        nice_name = adapter.nice_name
        ipv6_enabled = False

        try:
            # Open the network key in the registry for the adapter
            key_path = f"SYSTEM\\CurrentControlSet\\Services\\Tcpip6\\Parameters\\Interfaces\\{adapter.nice_name}"
            reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, win32con.KEY_READ)

            # Check for the existence and value of the 'DisabledComponents' registry key
            try:
                value, reg_type = winreg.QueryValueEx(reg_key, "DisabledComponents")
                if value & 0x20 == 0:  # Check the specific bit that controls IPv6
                    ipv6_enabled = True
            except FileNotFoundError:
                # No DisabledComponents key found, assuming IPv6 is enabled
                ipv6_enabled = True
            finally:
                winreg.CloseKey(reg_key)
        except FileNotFoundError:
            # Registry key for the adapter not found, assuming IPv6 is enabled
            ipv6_enabled = True

        ipv6_enabled_dict[nice_name] = ipv6_enabled

    return ipv6_enabled_dict


def main():
    ipv6_status = is_ipv6_enabled_windows()
    is_enabled = False
    for adapter, is_enabled in ipv6_status.items():
        print(f"{adapter}: IPv6 enabled: {is_enabled}")
        if is_enabled:
            is_enabled = True
    return 0 if is_enabled else 1


if __name__ == "__main__":
    sys.exit(main())