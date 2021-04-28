# Look for a pattern within domain names
# WHOISXMLAPI.COM
# Search all files, traversing directories, looking for a matching pattern
# For example, 
#    search all files starting in /tmp/whois_download/ for  
#    the pattern "music" regardless of what the TLD is.
#    CLI: python walkdir.py -p /tmp/whois_download/ music 
#           if fnmatch.fnmatch(file, "*" + pattern + "*"):
#

import os
import fnmatch
import sys
import getopt
 
file_list = []
path = ''
pattern = ''

def check_for_string(file_name):
   with open(file_name, 'r') as read_obj:
      for line in read_obj:
         if pattern in line:
            print (file_name + "," + line)
   return False 

try:
   opts, args = getopt.getopt(sys.argv[1:], "hp:k:",["path=","keyword="])
except getopt.GetoptError:
   print ("walkdir.py -p <path> -k keyword")
   sys.exit(2)

for opt, arg in opts:
   if opt == '-h':
      print ("HELP:- walkdir -p <path> -k keyword")
      print ("(C)2021 WHOIXMLAPI.COM")
      sys.exit(1)
   elif opt in ("-p", "--path"):
      path = arg
   elif opt in ("-k", "--keyword"):
      pattern = arg

print ("Path set to   : ", path)
print ("Search keyword: ", pattern)

for path, folders, files in os.walk(path):
    for file in files:
        if fnmatch.fnmatch(file, '*.csv'):
            if check_for_string(os.path.join(path, file)):
               file_list.append(os.path.join(path, file))
 
for filename in file_list:
    print(filename) 
