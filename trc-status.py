from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import ssl
import functools
import json

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://newsinteractives.cbc.ca/longform-single/beyond-94"

# Get the webpage
request = urllib.request.Request(url)
raw_response = urllib.request.urlopen(request).read()
html = raw_response.decode("utf-8")

# Extract the data
soup = BeautifulSoup(html, 'html.parser')
counts = soup.select(".progress-row h3")
counts = list(map(lambda x: int(x.getText().strip()), counts))
complete = counts[-1] # Get last h3 element
total = functools.reduce(lambda a, b: a+b, counts) # Calculate the total

# Output results as JSON
print(json.dumps({ "total" : total, "complete" : complete }))

