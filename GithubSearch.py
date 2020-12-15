import http.client
import json

# API call to get the # of contributors
# https://api.github.com/repos/[ProjectOwner]/[ProjectName]/contributors

# be sneaky - get the max number of pages in the response header's 'link' value:
# <https://api.github.com/repositories/20580498/contributors?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/20580498/contributors?per_page=1&page=383>; rel="last"

def getProjectTotal(owner, repository, location, payload, headers):

  conn2 = http.client.HTTPSConnection("api.github.com")
  conn2.request("GET", "/repos/" + owner + "/" + repository + "/" + location + "?per_page=1", payload, headers)

  #print(conn2.request)  #debugging

  res = conn2.getresponse()
  total_pageresults = ''
  
  res_header = res.getheader('link').split(' ')[2].split('=')[2]
  total_pageresults = res_header.strip('>;')
  #print(total_pageresults)
  
  return total_pageresults
  
  # try:
  #
  #except AttributeError:
  #  total_pageresults = 'No value found'
  #except:
  #  total_pageresults = 'API Error'
  #finally:
  #  return total_pageresults

  """
  getContributorsTotal(owner, repository, payload, headers) returns a string
  """

conn = http.client.HTTPSConnection("api.github.com")
# 'Kubernetes'

# Prompt for user input
searchString = input('Enter Github Project Search String: ')

payload = ''
headers = {
  'Accept': 'application/vnd.github.v3.text-match+json',
  'User-Agent': 'Python3'
}
conn.request("GET", "/search/repositories?q=" + searchString + "&in:readme,name,description&page=1&per_page=10", payload, headers)

res = conn.getresponse()
data = res.read()
thisdict = json.loads(data.decode("utf-8"))

#get count of total results
thecount = thisdict['total_count']

print('Your search returned', thecount, 'Results (Top 10 are shown below):\n' )

print('Name', 'Language', 'Contributors', 'Watchers', 'Open Issues', 'Stars', 'Forks', sep='\t\t' )
print('----', '--------', '------------', '--------', '-----------', '-----', '-----', sep='\t\t')

#print(thisdict)
for dataitems in thisdict['items']:

  total_contributors = getProjectTotal(str(dataitems['owner']['login']), str(dataitems['name']), 'contributors', payload, headers)
  total_watchers = getProjectTotal(str(dataitems['owner']['login']), str(dataitems['name']), 'stargazers', payload, headers)
  print(dataitems['name'], dataitems['language'], total_contributors, total_watchers, dataitems['open_issues_count'], dataitems['stargazers_count'], dataitems['forks'], sep='\t\t')
