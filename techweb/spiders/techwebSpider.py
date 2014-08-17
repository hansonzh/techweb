#-*- coding: utf-8 _*_
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from techweb.items import TechwebItem


class TechWebSpider(CrawlSpider):
    name = "junzhang"
    allowed_domains = ["techweb.com.cn"]
    start_urls = [
            "http://www.techweb.com.cn",
        ]
    
    rules = (
            Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div/h1/a')), callback = 'parse_item', follow = True, process_links = 'handle_links'),

            Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//div[@class="left0"]/ul/li/a')), callback = 'parse_item', follow = True, process_links = 'handle_links'),
        )
    
    def parse_item(self, response):
        item = TechwebItem()
        item['headTitle'] = response.xpath("//div[@class='title']/h1/text()").extract()[0]
        item['url'] = response.url
        
        body = response.xpath('//div[@id="artibody"]/p')

        #print "----------------------"
        #print item['headTitle']
        #print item['url']
        #print "----------------------"

        item['description'] = ""
        for sel in body:
            #选中当前p下的所有节点，包括p本身
            for it in sel.xpath("./descendant-or-self::*"):
                text = it.xpath("./text()").extract()
                if len(text) != 0:
                    #replace \xa0 with  ' ' to avoid UnicodeDecoderError
                    item['description'] += text[0].replace(u'\xa0', u' ')
            item['description'] += "\n"
            
        #print item['description']
        #print "----------------------"
        return item
        
    def handle_links(self, links):
        
        newlinks = []
        
        for link in links:
            #除去link中的空格%20
            link.url = link.url.strip('%20')
            newlinks.append(link)

        return newlinks
        
