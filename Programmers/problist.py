import requests
import re

def get(handle,tags):	
	url="http://codeforces.com/api/user.status?handle=";
	url+=(handle)
	data=requests.get(url)
	submission=data.json()
	lis = {}
	i=0
	if submission['status']=="OK":
		result=submission['result']
		for rslt in result:
			if rslt['verdict']=="OK":
					problem=rslt['problem']
					if tags in problem['tags']:
						lis[i]=problem['name']
						i+=1
	return lis	


def getProb(handle,tags):
	url="https://codeforces.com/api/problemset.problems?tags=";
	url+=(tags)
	data=requests.get(url)
	submission=data.json()
	probs={}
	i=0
	j=0
	nme=get(handle,tags)
	if submission['status']=="OK":
		result=submission['result']
		for rslt in result['problems']:
				problem=rslt['name']		
				if i>10:return probs
				if problem not in nme:
					probs[j]=problem
					j+=1
				i+=1
		