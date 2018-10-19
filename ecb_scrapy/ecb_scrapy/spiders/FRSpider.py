import scrapy
from ecb_scrapy.items import FRScrapyItem
from scrapy.http import Request

class FRSpider(scrapy.Spider):
    name = 'FR'
    start_urls = ['https://www.federalreserve.gov/feeds/press_monetary.xml']

    def parse_detail(self, response):
        FRScrapyItem = response.meta['part_items']
        data_all = response.xpath('//div[@class="col-xs-12 col-sm-8 col-md-8"]/p/text()').extract()
        content = ''
        for data in data_all:
            content = content + data + '\n'
        FRScrapyItem['content'] = content
        yield FRScrapyItem

    def parse(self, response):
        item = FRScrapyItem()
        titles = response.xpath('//item/title/text()').extract()
        hrefs = response.xpath('//item/link/text()').extract()
        dates = response.xpath('//item/pubDate/text()').extract()
        for n in range(len(titles)):
            item['title'] = titles[n]
            item['href'] = hrefs[n]
            item['date'] = dates[n]
            yield Request(hrefs[n], meta={'part_items': FRScrapyItem(date=item['date'],\
                                          title=item['title'], href=item['href'])}, callback=self.parse_detail)
            # if n == 1:
            #     break
