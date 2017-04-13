import scrapy
from poi.items import Url

class PoiSpider(scrapy.Spider):
    name = "ip"
    allowed_domains = ["www.kuaidaili.com"]
    seed = [
        "http://www.kuaidaili.com/free/inha/%d/",
        "http://www.kuaidaili.com/free/outha/%d/"
    ]

    count = [10, 10]
    #start_urls = ["http://www.poi86.com/poi/amap/district/330102/1.html"]
    start_urls = []
    for a,c in zip(seed, count):
        for i in xrange(1,c+1):
            start_urls.append(a%i)

    print len(start_urls)

    def parse(self, response):
        for se in response.xpath('//tr'):
            info = se.xpath('td/text()').extract()
            if len(link) > 0:
                item = Ip()
                item['ip'] = info[0]
                item['port'] = info[1]
                yield item
