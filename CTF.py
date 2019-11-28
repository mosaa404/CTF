#!/usr/bin/python3
from requests import get
from optparse import OptionParser
from sys import platform
if platform in ["linux","linux2"]:
    F = '\033[92m'
    N = '\033[91m'
else:
    F = N = ''
parser = OptionParser(F+'''
	            W3lcoM3 My Name'5 Critical T001 F0und
                    This tool built to penetration testing
T0 U53 Th3 T00l
~$python3 ctf.py -u http://www.exampel.com -f filelist.txt''')
print(F+'''
T0 Know H0W use this to0l
please run
~$python3  ctf.py -h

######################################################
[ #Developed_by_Mo0Ssaa ]
[ Github:https://github.com/mosaa404 ]
#######################################################''')
parser.add_option('-u','--url',dest='url',help='Enter target url')
parser.add_option('-f','--file',dest='file',help='Enter the file list')
(options,args) = parser.parse_args()
print(options.url)
try:
    if options.url[len(options.url)-1] == '/' and options.url[0] == 'h':
        pass
    elif options.url[len(options.url)-1] == '/' and options.url[0] != 'h':
        options.url='http://'+options.url
    elif options.url[len(options.url)-1] != '/' and options.url[0] == 'h':
        options.url=options.url+'/'
    else:
        options.url='http://'+options.url+'/'
    with open(options.file,mode='r') as f:
        for line in f:
            line = line.strip()
            if get(options.url+line).status_code == 200:
                print(F+'##########\n[+]f0und --> '+options.url+line+'\n##########')
            else:
                print(N+'[-]N0t f0und --> '+options.url+line)
except:
    print(parser)
