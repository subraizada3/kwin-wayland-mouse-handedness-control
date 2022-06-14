#!/usr/bin/env python3

import sys

# pip package: pydbus
# Arch package: python-pydbus
from pydbus import SessionBus

help_msg = 'Call with "l" or "r" as argument'



# Check that this is called with one arg, which must be "l" or "r"

valid_args = False
if len(sys.argv) == 2:
	arg = sys.argv[1].upper()
	if arg in ['L', 'R']:
		valid_args = True

if not valid_args:
	print(help_msg)
	sys.exit(0)



bus = SessionBus()

# There doesn't seem to be a way to get all 'InputDevice/event*' objects
for i in range(0,100):
	try:
		obj = bus.get('org.kde.KWin', f'InputDevice/event{i}')
		if hasattr(obj, 'leftHanded'):
			obj.leftHanded = arg == 'L'
	except:
		continue
