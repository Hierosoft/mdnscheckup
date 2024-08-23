# mdnscheckup

mdnscheckup is a Python utility designed to check if MDNS (Multicast
DNS) is functioning correctly on Windows 11 systems and attempt to
troubleshoot common issues. Windows 11 is known for occasionally failing
to list MDNS devices, and the reasons behind this are unclear. This
utility helps diagnose and potentially resolve these issues.

The `mdnscheckup` module also includes a submodule called
`ipv6checkup`, which checks whether IPv6 is enabled on
network adapters. Some users have reported that disabling IPv6 resolves
MDNS issues, while others with IPv6 enabled do not experience any
problems.


## Features

- **MDNS Troubleshooting**: Diagnose MDNS functionality on Windows 11.
- **IPv6 Check**: Determine if IPv6 is enabled on network adapters, as
    it may affect MDNS performance.


## Installation

To install mdnscheckup, you'll need Python 3.7 or higher. You can
install the required dependencies using \`pip\`:

### Windows
```bash
pip install -r requirements.txt
```

### Linux/macOS/other
```bash
pip install -r requirements-dev.txt
```

## Usage

To run the MDNS check and IPv6 check, install the mdnscheckup Python package then execute the main script:

```bash
python3 -m mdnscheckup
```

or if not installed, run the script directly from the repo:
```bash
python3 mdnscheckup/mdnscheckup.py
```

This will run both the MDNS diagnostic and the IPv6 check, providing
insights into potential issues.

### Example Output

```
Ethernet: IPv6 enabled: True
Wi-Fi: IPv6 enabled: False
MDNS Status: Devices listed: False
Devices: ['_printer._tcp.local.']
```

## How It Works

1. **ipv6checkup**: Uses the `ipv6checkup` submodule to
   determine if IPv6 is enabled on each network adapter.
   - This may not affect mdns on some system configurations.
2. **mdnscheckup**: Checks whether MDNS is functioning by
   attempting to list devices on the network.
   - NOTE: Even if "MDNS Status: Devices listed: False", there may not be a problem. Ensure you are connected to the same network as your device(s) before running the test to get an accurate test.
   - Windows Firewall can block this, potentially.
     - Click allow for public or private, whichever you have told it to use to designate your network. Ideally, allow both, since the public-private distinction is arbitrary and you may change it later and not realize the repercussions.
3. **Combined Report**: Provides a summary of the MDNS status and IPv6
   configuration.

### Key Files

- **mdnscheckup.py**: The main script that performs the MDNS
  diagnostic.
- **ipv6checkup.py**: The submodule that checks IPv6 status.
- **README.rst**: This file, providing documentation and usage
  instructions.

## Development

### Development Dependencies
If you'd like to contribute to mdnscheckup, clone the repository and
install the development dependencies:

```bash
git clone https://github.com/Hierosoft/mdnscheckup.git
cd mdnscheckup
pip install -r requirements-dev.txt
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request
on [GitHub](https://github.com/Hierosoft/mdnscheckup).

### Tasks
- [ ] tests using \`pytest\`:

```bash
pytest
```
- Requires "Development Dependencies" steps.


## License

mdnscheckup is licensed under the MIT License. See the
[license.txt](license.txt) file for more details.


## Acknowledgments

- [ifaddr](https://github.com/pydron/ifaddr) for adapter enumeration.
- [pywin32](https://github.com/mhammond/pywin32) for Windows API
    access.

## Contact

For any questions or feedback, feel free to reach out via the [issues
page](https://github.com/Hierosoft/mdnscheckup/issues) on GitHub.
