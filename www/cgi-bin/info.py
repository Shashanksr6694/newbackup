#!/usr/bin/python

import commands
import os

os.system("sudo ansible all -m setup --tree /etc/ansible/info >info.txt")
os.system("sudo cat info.txt | grep -vEi 'Failed|Unreachable' | grep -i 192 | cut -f1 -d' ' >ip.txt ; cat info.txt | grep -i 'ansible_processor_cores' | awk {'print $2'} | cut -f1 -d',' >cpu.txt ; cat info.txt | grep -i 'ansible_memtotal_mb' | awk {'print $2'} | cut -f1 -d',' >mem.txt")

os.system("sudo cat /etc/ansible/ip.txt | grep -i 192 > /etc/ansible/ipread.txt")

