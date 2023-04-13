***ll Over Internet Explorer***
**Introduction**

This script was developed for a CTF challenge and provides a backdoor to control a victim's Internet Explorer through a remote shell. This can be used for educational or informational purposes, but use it at your own risk. The author and contributors are not responsible for any damages or consequences arising from the use of this software.

**Usage**

The victim needs to run the following command on their Windows machine:

```C:\> python IEbackdoor.py ```

This opens up Internet Explorer and waits for the attacker to connect.

The attacker needs to run the following command:

```$ httpserverRshell.py ```

This starts a web server on the attacker's machine and waits for the victim to connect.

Once the victim connects to the attacker's server, the attacker will have a remote shell to control the victim's Internet Explorer.


**Disclaimer**

This script is provided "as is" and is intended for educational and informational purposes only. The author and contributors are not responsible for any damages or consequences arising from the use of this software. Use at your own risk.
