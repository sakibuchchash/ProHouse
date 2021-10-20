
import requests

def rating(handle):
	urlr="https://codeforces.com/api/user.info?handles=";
	urlr+=(handle)
	datar=requests.get(urlr)
	submissionr=datar.json()
	store={}
	if submissionr['status']=="OK":
		resultr=submissionr['result']
		i=0
		for rslt in resultr:
				if 'rating' in rslt:
					rating=rslt['rating']		
					store['rating']=rating
				if 'rank' in rslt:
					rank=rslt['rank']		
					store['rank']=rank
				if 'maxRating' in rslt:
					maxRating=rslt['maxRating']			
					store['maxRating']=maxRating

	return store	
"""

def main():
	handler="SadrulToaha"
	s=rating(handler)
	print(s)
	print(s['rating'])
	print(s['rank'])
	print(s['maxRating'])
if __name__=='__main__' :
	main()
"""