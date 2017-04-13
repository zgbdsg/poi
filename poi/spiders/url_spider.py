import scrapy
from poi.items import Url

class PoiSpider(scrapy.Spider):
    name = "url"
    allowed_domains = ["www.poi86.com"]
    seed = [
        "http://www.poi86.com/poi/amap/district/330102/%d.html",
        "http://www.poi86.com/poi/amap/district/330103/%d.html",
        "http://www.poi86.com/poi/amap/district/330104/%d.html",
        "http://www.poi86.com/poi/amap/district/330105/%d.html",
        "http://www.poi86.com/poi/amap/district/330106/%d.html",
        "http://www.poi86.com/poi/amap/district/330108/%d.html",
        "http://www.poi86.com/poi/amap/district/330109/%d.html",
        "http://www.poi86.com/poi/amap/district/330110/%d.html",
        "http://www.poi86.com/poi/amap/district/330122/%d.html",
        "http://www.poi86.com/poi/amap/district/330127/%d.html",
        "http://www.poi86.com/poi/amap/district/330182/%d.html",
        "http://www.poi86.com/poi/amap/district/330183/%d.html",
        "http://www.poi86.com/poi/amap/district/330185/%d.html"
    ]

    count = [607, 891, 1107, 713, 1276, 391, 1452, 1237, 328, 235, 321, 444, 503]
    #start_urls = ["http://www.poi86.com/poi/amap/district/330102/1.html"]
    start_urls = []
    for a,c in zip(seed, count):
        for i in xrange(1,c+1):
            start_urls.append(a%i)

    print len(start_urls)

    def parse(self, response):
        for se in response.xpath('//td'):
            link = se.xpath('a/@href').extract()
            if len(link) > 0:
                item = Url()
                item['url'] = link[0]
                yield item
