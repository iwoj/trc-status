from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import ssl
import functools
import json

ssl._create_default_https_context = ssl._create_unverified_context

# Urlencode the URL
# url = urllib.parse.quote_plus("https://newsinteractives.cbc.ca/longform-single/beyond-94")
url = "https://newsinteractives.cbc.ca/longform-single/beyond-94"

# Create the query URL.
query = "https://api.scraperbox.com/scrape"
query += "?token=%s" % "4ACAF450EAC31DDD730B0FC04C1B18FC"
query += "&url=%s" % url
query += "&javascript_enabled=true"

# Call the API.
#request = urllib.request.Request(query)
request = urllib.request.Request(url)
raw_response = urllib.request.urlopen(request).read()
html = raw_response.decode("utf-8")

# Setup beautifulsoup
soup = BeautifulSoup(html, 'html.parser')

# Find the elements
totals = soup.select(".progress-row h3")
totals = list(map(lambda x: int(x.getText().strip()), totals))
complete = totals[-1]
total = functools.reduce(lambda a, b: a+b, totals)

# Get the text contents
print(json.dumps({ "total" : total, "complete" : complete }))

