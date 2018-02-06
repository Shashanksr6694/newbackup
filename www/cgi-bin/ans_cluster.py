#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print ""

#this is for IP address list

file=open('/etc/ansible/hosts','w')
file.write('[project1]\n192.168.122.1\n')
file.close()


ip_info="sudo arp-scan --interface=virbr0 192.168.122.0/24 | grep -i 192 | awk {'print $1'} >> /etc/ansible/hosts"
os.system(ip_info)


#for get ip which is successfully access and their cpu and memory size

os.system("sudo ansible all -m setup --tree /etc/ansible/info >/var/www/cgi-bin/ans_info.txt")

os.system("sudo cat /var/www/cgi-bin/ans_info.txt | grep -vEi 'Failed|Unreachable' | grep -i 192 | cut -f1 -d' ' >/var/www/cgi-bin/ans_ip1.txt ; cat ans_info.txt | grep -i 'ansible_processor_vcpus' | awk {'print $2'} | cut -f1 -d',' >/var/www/cgi-bin/ans_cpu.txt ; cat /var/www/cgi-bin/ans_info.txt | grep -i 'ansible_memtotal_mb' | awk {'print $2'} | cut -f1 -d',' >/var/www/cgi-bin/ans_mem.txt")

os.system('cat /var/www/cgi-bin/ans_ip1.txt | grep "192" > /var/www/cgi-bin/ans_ip.txt')

#to get list of all scan ip

f=open('/var/www/cgi-bin/ans_ip.txt','r')
b=f.read()
ip=b.split('\n')
f.close()

#ssh in ips

for i in ip:
	os.system("sudo ssh-copy-id "+i)

#to get list of ip(successfuly access)

f=open('/var/www/cgi-bin/ans_ip.txt','r')
b=f.read()
ip_list=b.split('\n')
ip_list.remove("")
f.close()

#print len(ip_list)

f=open('/var/www/cgi-bin/ans_cpu.txt','r')
b=f.read()
cpu_list=b.split('\n')
cpu_list.remove("")
f.close()

#to get list of memory

f=open('/var/www/cgi-bin/ans_mem.txt','r')
b=f.read()
mem_list=b.split('\n')
mem_list.remove("")
f.close()

#to get ip of max memory,cpu,ip

max_mem=max(mem_list)
ip_max_mem=ip_list[mem_list.index(max_mem)]
cpu_max_mem=cpu_list[mem_list.index(max_mem)]
index_of_max_mem=mem_list.index(max_mem)

#to store ip of namenode
file=open('/var/www/cgi-bin/ans_ipnn.txt','w')
file.write(ip_max_mem)
file.close()


print """
	<form action='../cgi-bin/ans_namenode.py' method='POST'>
	<table cellpadding='5px' border='1px solid black'>
			
	<tr><th>IP Address</th>
	<th>CPU Core</th>
	<th>RAM Size</th></tr>
 
"""
	
for i in range(len(ip_list)):
	print "<tr>"
	if i==index_of_max_mem:
		print "<td><input type='radio' checked='checked' name='ip' value="+ip_list[i]+">"+ip_list[i]+"</td>"
	else:
		print "<td><input type='radio' name='ip' value="+ip_list[i]+">"+ip_list[i]+"</td>"
	print "<td>"+cpu_list[i]+"</td>"
	print "<td>"+mem_list[i]+"</td>"
	
	print "</tr>"
	
print "</table>"
print "<td><input type='text' name='nn_name' placeholder='Enter name of namenode Directory'></td>"
print "<td><input type='text' name='dn_name' placeholder='Enter name of datanode Directory'></td>"
#print "<input type='hidden' name='index' value='"+str(index_of_max_mem)+"'>"
print "<input type='submit' value='check'>"
print "</form>"


#to store ip of datanode
f=open('/var/www/cgi-bin/ans_ip.txt','r')
b=f.read()
ip_list=b.split('\n')
ip_list.remove(ip_max_mem)
ip_list.remove("")
f.close()

f=open('/var/www/cgi-bin/ans_ipdn.txt','w')
for i in ip_list:
	f.write(i+'\n')
f.close()



