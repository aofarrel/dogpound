import subprocess
import shutil
import os
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
import requests

res = requests.get("https://pbs.twimg.com/media/EfKADlvWAAE7P0p?format=jpg&name=small", stream = True)
if res.status_code == 200:
	counter = 0
	for x in os.walk("."):
		try:
			with open("%s/wow.jpg" % x[0], 'wb') as meme:
				shutil.copyfileobj(res.raw, meme)
				counter += 1
		except OSError:
			pass
	print("Wrote image %s times." % counter)
else:
	print("Darn... they're onto us.")

