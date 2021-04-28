# Take a screenshot of the website if it resolves using the 
# WHOISAPIXML.COM Screenshot API
# Ed Gibbs

import socket
import sys
import os

# resolve a text file containing a list of hostnames 

fList = sys.argv[1]
oDir = sys.argv[2]

notResolvable = 0
reSolvable = 0

# Provide your API Key
# APIKEY = <YOUR_API_KEY_FROM_WHOISXMLAPI.COM>


with open(fList, "r") as ins:
   for line in ins:
      hostName = line.strip()
      hostName = hostName[:-1]   # Remove comma
      
      print ("HOSTNAME = [{}]" .format(hostName))
      try:
         ipAddr = socket.gethostbyname_ex(hostName)
      except socket.error:
         notResolvable += 1
         print(f"Not resolvable = " + str(notResolvable))
      else:
         webSite = "curl \"https://website-screenshot.whoisxmlapi.com/api/v1?apiKey=" + APIKEY + "&url=" + hostName + "&credits=DRS&scroll=1\" -o " + oDir + hostName + ".jpg"
         os.system(webSite)
         print(webSite)
         reSolvable += 1
         print(f"Resolvable = " + str(reSolvable))
