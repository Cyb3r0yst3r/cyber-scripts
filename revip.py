# Ed Gibbs

import sys

from datetime import datetime
from reverseip import *

ipAddr = sys.argv[1]
apiKey = sys.argv[2] 

client = Client(apiKey)

result = client.data(ipAddr)

print("index,domain,last_visited_date,last_visited_time")

i = 1

for record in result.result:
   ts = int(record.last_visit)
   lastVisitDate = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
   lastVisitTime = datetime.utcfromtimestamp(ts).strftime("%H%M%S")
   print("{},{},{},{}".format(i, record.name, lastVisitDate, lastVisitTime))
   i += 1
