import codecs
f=codecs.open("htmltext.html", 'r')
data = f.read()

from BeautifulSoup import BeautifulSoup
import datetime
now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
from urlparse import urlparse

# data = '''<div class="image">
#         <a href="http://www.example.com/eg1">Content1<img  
#         src="http://image.example.com/img1.jpg" /></a>
#         </div>
#         <div class="image">
#         <a href="http://www.example.com/eg2">Content2<img  
#         src="http://image.example.com/img2.jpg" /> </a>
#         </div>'''

soup = BeautifulSoup(data)

urls = None
for div in soup.findAll('tbody'):
    urls = div.findAll('a')
allUrls = []
with open("like4like_" + str(now) + ".txt","w") as fw:
	for lines in urls:
		if str(lines)[:32] == "<a href=\"https://www.twitter.com":
			content = str(lines)[33:-26]
			userName = content.split("/")[0]
			tweetId = content.split("/")[2]
			fw.write(userName + "," + tweetId + "\n")
