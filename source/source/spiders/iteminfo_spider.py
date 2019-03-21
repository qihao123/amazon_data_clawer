from scrapy.selector import selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import CrawlSpider as Spider
from scrapy.contrib.spider import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractors
from source.items import sourceItem
import scrapy

class AmazonItemsInfo(scrapy.Spider):
	name = "amazon"
    allowed_domains = ["amazon.cn","www.amazon.cn"]
    start_urls = [
        'https://www.amazon.cn/s/ref=sr_pg_2?rh=n%3A116087071%2Ck%3A电子书阅读器&page=1&keywords=电子书阅读器&ie=UTF8&qid=1552999294'
    ]

    def parse(self, response):
        NextPage = response.xpath("//*[@id="pagnNextLink"]/@href").extract()
        print(NextPage)

        if (NextPage != []):
            self.start_urls.append('http://www.amazon.cn' + NextPage[0])
        sites = response.xpath("//*[@id="s-results-list-atf"]").extract()
        items = []
        for site in sites:
            source = SourceItem()
            source['price'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/a/span[2]/text()")
            source['name'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[1]/div[1]/@title")
            source['url'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[1]/div[1]/@href")
            source['itemsid'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span/@name")
            source['star'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span/span/a/i[1]/span/text()")
            source['comments_number'] = Selector(text = site).xpath("//li/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/a/text()")
            items.append(source)
        return items
    def _process_request(self,request):
        return request