#!/usr/bin/python3
import os
import getpass
import argparse

parser = argparse.argument_parser()
parser.add_argument('-l','--login', action='store', help='username')
parser.add_argument('-p','--port', action='store', default='22', help='port')
parser.add_argument('-L','--list', action='store', help='file list of IPs')
parser.add_argument('-i','--ip-address', action='store', nargs='+', metavar='host' help='ip or list of ips')

args = parser.parse_args()
if not args.login:
    print("You need a login, broski!")
    return 0

if args.list:
    ips = [i for i in open(args.list, 'r').readlines()]
    passwd = getpass.getpass('Password: ')

    for ip in ips:
        cmd = 'ssh-id-copy {0}@{1} -p {2}'.format(ip,args.port,passwd)            
        os.system('sshpass -p ' + passwd + ' ' + cmd)
        print("Key added: ", ip)   # prints if successful
        # ex: sshpass -p passwd ssh-id-copy login@1.1.1.1

elif args.host:
    ip = args.host
    cmd = 'ssh-id-copy {0}@{1} -p {2}'.format(ip,args.port,passwd)
    os.system('sshpass -p ' + passwd + ' ' + cmd)
    print("Key added: ", ip)   # prints if successful
else:
    print("No IP addresses were given to run script...")
    return 0 
