# Snap Disabled Versions Cleanup Script

This Python script removes all disabled or old Snap packages from an Ubuntu-based system and restarts the `snapd` service to ensure proper operation.

If you find this project useful and would like to support its development, consider donating via PayPal or Venmo: 
- [PayPal](https://www.paypal.com/paypalme/m1st0)
- [Venmo](https://venmo.com/code?user_id=3319592654995456106&created=1753280522)

© 2025 Maulik Mistry

This project is licensed under the Apache License 2.0.
See the [LICENSE.txt](LICENSE.txt) file for full license text.

## Features
- Uses `subprocess` for secure command execution.
- Automatically removes all disabled Snap revisions.
- Restarts `snapd` service and checks its status.

## Usage
1. Ensure Python 3 is installed.
2. Save the script to a file, for example: `cleanup_snap_disabled.py`.
3. Make the script executable:
   chmod +x cleanup_snap_disabled.py
4. Run with:
   ./cleanup_snap_disabled.py

**Note:** This script requires `sudo` privileges since it modifies system-level Snap installations.

## References
- https://people.ubuntu.com/~robert-ancell/snapd-glib/reference/SnapdClient.html
- https://gist.github.com/flexiondotorg/84c3f137d70f4e21ea46419833c0aff4
- https://forum.snapcraft.io/t/python-example-of-using-snapd-glib-to-authenticate-install-and-remove-snaps/2417
- https://forum.snapcraft.io/t/how-to-communicate-with-run-snapd-socket-using-python/6432/4
- https://stackoverflow.com/questions/13334634/the-difference-between-os-system-and-subprocess-calls

