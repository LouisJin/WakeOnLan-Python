WakeOnLan-Python
===

wol.py
tiny python3 script
input the mac address only
wakeup most windows or linux devices on the lan

Require
---
The device which will be wakeup requires the following conditions

##### Software:
1. Control Panel -> Network Connections -> Network Card -> Properties -> Configure -> Advance

	Wake on magic packet : Enabled
2. Control Panel -> Network Connections -> Network Card -> Properties -> Configure -> Power Management

	uncheck "Allow the computer to turn off this device to save power"
	or
	check above but also check "Allow this device to wake the computer"
3. Control Panel -> Power Options -> Choose what the power buttons do -> Change settings that are currently unavailable

	uncheck "Turn on fast start-up"
	
##### Hardware:
1. Enter BIOS advance settings，each motherboard has different fields，if you found one of "wake on lan","Resume on lan","Power on PME","Power on by PCI-E device" or "Power on by Onboard LAN", make it enable.


Usage
---

    Usage: wol.py [-m mac_address]

	Options:
		-?,-h           : this help
		-v              : show version and exit
		-m mac_address  : where the magic packet will send to. (eg. 2C-4D-54-CF-9E-50 or 2C:4D:54:CF:9E:50)


License
---

Apache License 2.0, see [LICENSE](LICENSE)
