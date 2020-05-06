# QRadar API call with Python
# Warren Perez
import requests
import json
import time

##################################### VARIABLES #####################################
headers={
  "Version":"<API Version>",
  "SEC":"<TOKEN>",
  "Accept":"application/json",
  "Content-Type": "application/json",
}

QRadarURL= "<IP>"


# Search
search_query = "<AQL query>"


searchUrl= "https://" + QRadarURL + "/api/ariel/searches?query_expression="
searchQueryURL = searchUrl + search_query

#First you need to make the search query, then you need to use the query ID to search for the results
##################################### FUNCTIONS #####################################

def queryQRadarAPI(url, headers):
		#verify=false is necessary because it is not able to verify the Certificate
		response = requests.post(url,headers=headers,verify=False)
		jsonRes = response.json()
		return jsonRes

def getResults(queryID, headers):
	url = "https://" + QRadarURL + "/api/ariel/searches/" + queryID + "/results"
	response = requests.get(url,headers=headers,verify=False)
	print(url)
	return response

	
def getQueryStatus(queryID):
# Get the query status information like status, query_execution_time
	url = "https://" + QRadarURL + "/api/ariel/searches/"+queryID
	response = requests.get(url,headers=headers,verify=False)
	#print ("Response status: ",response.content)
	jsonRes=response.json()
	if jsonRes['status'] == "COMPLETED":
		return jsonRes
	
	
##################################### END FUNCTIONS #####################################


##################################### MAIN #####################################

#Run query 30,15,5 Minutes search for 1.2.3.4
jsonResponse = queryQRadarAPI(searchQueryURL,headers)



#Get cursor of the queries
cursorID = jsonResponse['cursor_id']

#Get results from previously ran query
time.sleep(5)

#get query status
jsonResults = getQueryStatus(cursorID)

query_execution_time = jsonResults['query_execution_time']
print ("Search Status: ",query_execution_time)


	
	
##################################### END MAIN #####################################

