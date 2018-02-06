#!/usr/bin/python

import commands
import os

os.system("sudo arp-scan --interface=virbr0  192.168.122.0/24 > scan.txt")
os.system("sudo cat scan.txt | grep -i 192 | awk '{print $1}' >/etc/ansible/hosts")
