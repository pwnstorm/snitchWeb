import shodan
from pprint import pprint
import requests
import argparse
import json
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI as dnsdumpster

def domain_info(site):
	results = dnsdumpster().search(str(site))
	rs = results['dns_records']['host']
	for domain in rs:
		print domain['domain'] + "\t" + domain['ip']
		ip_fisia(domain['ip'])

def ip_fisia(ip):
	try:	
		SHODAN_API_KEY = str(open('/root/.shodan/api_key','r').readlines()[0])
		api = shodan.Shodan(SHODAN_API_KEY)
		results = api.host(str(ip))
		print """
==================================================================================
org: \t\t%s
os: \t\t%s

			""" % (results.get('org','n/a'), results.get('os','n/a'))
		
		for bn in results['data']:
			print """
Port: %s
Banner: \t%s
**********************************************************************************
""" 			% (bn['port'], bn['data'])
	except shodan.APIError, e:
		#print "Error: " + str(e)
		pass

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--domain', dest="tdomain", help="The domain you want to scan")
	args = parser.parse_args()
	if args.domain:
		domain_info(args.tdomain)
	else:
		print "Weka domain babaa. python 

if __name__=='__main__':
	main()
