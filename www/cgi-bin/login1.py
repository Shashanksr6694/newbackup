#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
username=data.getvalue('usr')
password=data.getvalue('passwd')


a=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $1}'")
b=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $3}'")



if  a[1] == username and b[1] == password :
	execfile("scan.py")		
	print "<META HTTP-EQUIV='refresh' content='0; url=../cgi-bin/table1.py'/>"
		
	
else:	
	print "<script>alert('Wrong Password')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/login1.html'/>"


