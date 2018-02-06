#!/usr/bin/python2

import commands
import cgi,cgitb

cgitb.enable()


print "Content-type:text/html"
print ""

form=cgi.FieldStorage()

iname1=form.getvalue('osl')


igroup1=form.getvalue('sgs')


icount1=form.getvalue('icou')


itype1=form.getvalue('iflav')


ikey1=form.getvalue('ikey')



#print iname1
#print igroup1
#print icount1
#print itype1
#print ikey1

if iname1=="amzlinux": 


	a=commands.getstatusoutput("sudo aws ec2 run-instances --image-id  ami-531a4c3c --security-group-ids " + igroup1 + " --count  " + icount1 + "  --instance-type " + itype1 + " --key-name " + ikey1 + "")
	#print a
	

if iname1=="rhel" :

	a=commands.getstatusoutput("sudo aws ec2 run-instances --image-id  ami-e60e5a89 --security-group-ids " + igroup1 + " --count  " + icount1 + "  --instance-type " + itype1 + " --key-name " + ikey1 + " --query 'Instances[0].InstanceId'")
	#print a


if iname1 == "ubun" :

	a=commands.getstatusoutput("sudo aws ec2 run-instances --image-id  ami-5d055232 --security-group-ids " + igroup1 + " --count  " + icount1 + "  --instance-type " + itype1 + " --key-name " + ikey1 + " --query 'Instances[0].InstanceId'")
	#print a

print "<script>alert('Instance Launched! Login to the Instances using the public ip in the below shell')</script>" 
print "<META HTTP-EQUIV='refresh' content='0; url=../cgi-bin/ec2table.py'/>"
