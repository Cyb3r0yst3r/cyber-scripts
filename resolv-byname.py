import socket
import sys

# resolve a text file containing a list of hostnames 

fList = sys.argv[1]

with open(fList, "r") as ins:
   for line in ins:
      hostName = line.strip()
      hostName = hostName[:-1]
      # print ("HOSTNAME = [{}]" .format(hostName))
      try:
         ipAddr = socket.gethostbyname_ex(hostName)
      except socket.error:
         print ("{}, " .format(hostName))
      else:
         print ("{}, {}".format(hostName, ipAddr))
