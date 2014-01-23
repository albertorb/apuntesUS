__author__ = 'AlbertoRinconBorreguero'
# web crawler utilizando pattern clips
from pattern.web import crawl, URL, DOM

urls = []
count = 0;
for link, source in crawl('http://ayudaatucompi.over-blog.es/articles-blog.html', delay=0, throttle=0):
    urls.append(link)
    count += 1
    if count == 5:
        break;
f = open('databse_urls.txt', 'r+')
for elem in urls:
    f.write(elem.url + "\n")

f = open('databse_urls.txt', 'r+')

for elem in f.readlines():
    dom = DOM(URL(elem).download(cached=True))
    bs = dom._beautifulSoup.findAll('a', attrs={'href': 'http://www.mediafire.com/?.*'})
    print bs



