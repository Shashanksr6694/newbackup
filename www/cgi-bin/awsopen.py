#!/usr/bin/python

import commands
import os
import webbrowser

os.system("sudo cat /etc/ansible/apache | awk 'NR==3{print $1}' > /etc/ansible/apacheipread.txt")

lines = [line.rstrip('\n') for line in open('/etc/ansible/apacheipread.txt')]

for f in lines:
	url = 'http://'+f+'/index.html'
	b = webbrowser.get('firefox')
	b.open_new_tab(url)
