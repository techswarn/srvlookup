import srvlookup #pip install srvlookup
import sys 
import dns.resolver #pip install dnspython 

def main(args):
      host = "ab-database-2427a88b.mongo.ondigitalocean.com"

      if len(sys.argv) > 1 : 
            host = sys.argv[1] 

      if host : 
            services = srvlookup.lookup("mongodb", domain=host) 
            for i in services:
                  print("%s:%i" % (i.hostname, i.port)) 
            for txtrecord in dns.resolver.query(host, 'TXT'): 
                  print("%s: %s" % ( host, txtrecord))

      else: 
            print("No host specified") 

      message = "Ran DNS checks"
      print(message)
      return {"body": message}
  