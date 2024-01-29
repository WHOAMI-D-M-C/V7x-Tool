import platform
import os
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("xxx")._login()
elif 'aarch' in arc:
	__import__("DM").asyncio.run(approval())
else:
	exit(f' Unknow device machine {arc}')
