import socket
import sys

# resolve a text file containing a list of ip addresses

fList = sys.argv[1]

with open(fList, "r") as ins:
   for line in ins:
      ipAddress = line.strip()
      try:
         hostName = socket.gethostbyaddr(ipAddress)
      except socket.error:
         print ("{}, " .format(ipAddress))
      else:
         print ("{}, {}".format(ipAddress, hostName[0]))
