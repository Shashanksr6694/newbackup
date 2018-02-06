#!/usr/bin/python
import os,commands,cgi,cgitb
cgitb.enable()

print "content-type:text/html"
print ""
x=cgi.FieldStorage()
namenode_name=x.getvalue('nn_name')
datanode_name=x.getvalue('dn_name')
namenode_ip=x.getvalue('ip')


#setting java path
f=open( '/var/www/cgi-bin/ans_bashrc2.txt','w')
f.write("# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\n\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n\nJAVA_HOME=/usr/java/jdk1.7.0_79\nPATH=$JAVA_HOME/bin:$PATH\nexport PATH\n\n")
f.close()


#HDFS Sample File
hdfs_sample_file="<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!--Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/"+namenode_name+"</value>\n</property>\n</configuration>"

#setting hdfs-site.xml
f=open('/var/www/cgi-bin/ans_hdfsnn.txt','w')
f.write(hdfs_sample_file)
f.close()




#CORE Sample File
core_sample_file="<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!--Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+namenode_ip+":10001</value>\n</property>\n</configuration>"


#setting core-site.xml
f=open('/var/www/cgi-bin/ans_core1.txt','w')
f.write(core_sample_file)
f.close()

#mapred-site.xml sample file
mapred_site_file="<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+namenode_ip+":9001</value>\n</property>\n</configuration>"

#setting mapred-site.xml
f=open('/var/www/cgi-bin/ans_mapred.txt','w')
f.write(mapred_site_file)
f.close()

#for playbook
os.system('sudo ansible-playbook -i /var/www/cgi-bin/ans_ipnn.txt /var/www/cgi-bin/ans_container.yml')





#-------------------------------------------------------------------------------------------------------------------------------------
#for Datanode

#to get list of ip of dn

f=open('/var/www/cgi-bin/ans_ipdn.txt','r')
b=f.read()
ip_list_dn=b.split('\n')
ip_list_dn.remove("")
f.close()


#HDFS Sample File
hdfs_sample_file="<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n\n<!--Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/"+datanode_name+"</value>\n</property>\n</configuration>"

#setting hdfs-site.xml
f=open('/var/www/cgi-bin/ans_hdfsdn.txt','w')
f.write(hdfs_sample_file)
f.close()

#for playbook
os.system('sudo ansible-playbook -i /var/www/cgi-bin/ans_ipdn.txt /var/www/cgi-bin/ans_cdatanode.yml')

print "<h1>Done</h1>"
