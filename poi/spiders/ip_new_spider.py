import scrapy
from poi.items import Url

class PoiSpider(scrapy.Spider):
    name = "newip"
    allowed_domains = ["www.xicidaili.com"]

    start_urls = ["http://www.xicidaili.com/wn/"]

    def parse(self, response):
        for se in response.xpath('//tr'):
            info = se.xpath('td/text()').extract()
            if len(link) > 0:
                item = Ip()
                item['ip'] = info[1]
                item['port'] = info[2]
                print info[1],info[2]
                yield item
