import urllib.request
import re


# Make sure the url entered is valid.
while True:
    url = input('Enter the website to crawl: ')
    if url.startswith('http://') or url.startswith('https://'):
        break
    else:
        print("Please enter a url that starts with http:// or https://")

# Get the Html contents from the url provided
html =urllib.request.urlopen(url).read()

# Pull all links starting with http or https using regular expressions
links = re.findall('"((http)s?://.*?)"', str(html))

# Search for all anchor tags especially in web application routes
tags = re.findall(r'<a href=(.*?)>(.*?)</a>', str(html))


# Print sll the found links
for link in links:
    print(link)

# print all the snchor tags located
for tag in tags:
    print(tag)

