

import xml.etree.ElementTree as ET
import urllib.request

url= "http://py4e-data.dr-chuck.net/comments_709560.xml"
html = urllib.request.urlopen(url)
data=html.read()
#print(data)
tags=ET.fromstring(data)
lst=tags.findall('comments/comment')
x=0
for item in lst:
  element=int((item.find('count').text))
  x=element+x
print(x)

