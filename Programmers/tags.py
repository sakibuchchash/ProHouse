import requests
import re
def List(handle):	
	url="http://codeforces.com/api/user.status?handle=";
	url+=(handle)
	data=requests.get(url)
	submission=data.json()

	i=0
	counts = {}
	final={}
	if submission['status']=="OK":
		result=submission['result']
		for rslt in result:
			if rslt['verdict']=="OK":
					problem=rslt['problem']
					for prb in problem['tags']:
						if prb in counts:
							counts[prb]+=1
						else:
							counts[prb]=1
					i+=1
	final[1]=counts
	final[0]=i
	return final
