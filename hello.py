from urllib import request
import re

class Spider():
    url = 'https://book.douban.com/'            
    root_pattern = '<div class="info">\n([\s\S]*?)<div class="more-meta">\n'
    title_pattern = 'title=([\s\S]*?)>'
    author_pattern = '<div class="author">\n([\s\S]*?)\n'

    def __fetch_contents(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

    def __analysis(self,htmls):
        anchors=[]
        root_htmls = re.findall(Spider.root_pattern, htmls)
        for html in root_htmls:
            title = re.findall(Spider.title_pattern, html)
            author = re.findall(Spider.author_pattern, html)
            anchor = {'title':title, 'author':author}
            anchors.append(anchor)
        return anchors
    
    def __refine(self, anchors):
        l = lambda anchors : {
        'title' : anchors['title'][0],
        'author' : anchors['author'][0].strip()}
        return map(l, anchors)
    
    def __show(self,anchors):
        for rank in range(0, len(anchors)):
            print('rank' + str(rank + 1) + ':' + 
                  'title' + anchors[rank]['title'] + '     '
                  'author' + anchors[rank]['author'])

    def go(self):
        htmls = self.__fetch_contents()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        self.__show(anchors)

    
spider = Spider()
spider.go()
