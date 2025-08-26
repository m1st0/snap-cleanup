#!/usr/bin/python3
# Removes disabled or old Snap packages

# Author: Maulik Mistry
# If you appreciate my work or help, consider supporting me through donations.
# You can donate via Venmo at https://venmo.com/code?user_id=3319592654995456106&created=1756212520  
# or PayPal at https://www.paypal.com/paypalme/m1st0 

# License:
#   This script is licensed under the Apache License 2.0.
#   See the LICENSE.txt file in the same directory for full details.

import subprocess
import sys


#LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' | while read snapname revision; do snap remove $snapname --revision=$revision; done
snap_script = "LANG=en_US.UTF-8 sudo snap list --all | awk '/disabled/{print $1, $3}' | " \
        "while read snapname revision; do " \
            "sudo snap remove \"$snapname\" --revision=\"$revision\"; " \
        "done" 
process1 = subprocess.run([snap_script], 
                          shell=True,
                          check=True, 
                          stdout=subprocess.PIPE, 
                          text=True)

if process1.stdout:
    print("Snap cleanup stdout:", process1.stdout)
if process1.stderr:
    print("Snap cleanup stderr:", process1.stderr)

# On Kubuntu?
process2 = subprocess.run(['sudo', 'systemctl', 'restart', 'snapd'], 
                          check=True, 
                          capture_output=True,
                          text=True)    # Better than universal_newlines=True

# Check the restart command output
if process2.stdout:
    print("Restart command stdout:", process2.stdout)
if process2.stderr:
    print("Restart command stderr:", process2.stderr)

# Check service status too
status_result = subprocess.run(['sudo', 'systemctl', 'status', 'snapd'], 
                               capture_output=True, 
                               text=True)

if status_result.stdout:
    print(status_result.stdout)

# Check return code (0 = active, non-zero = not active/failed)
if status_result.returncode == 0:
    print("Service snapd is running successfully")
else:
    if status_result.stderr:
        print("snapd failed to restart:", status_result.stderr)
