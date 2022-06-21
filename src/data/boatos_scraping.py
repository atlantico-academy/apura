# scrape webpage
import scrapy
from scrapy.crawler import CrawlerProcess
# text cleaning
import re

def verify_label_boatos(response):
    if ('boato'or'#boato') in response:
        return 1
    else:
        return 0

class BoatosSpider(scrapy.Spider):
    name = 'BoatosSpider'
    start_urls = ['https://boatos.org/politica'] 
    custom_settings = {
        'FEEDS': {
            '../data/raw/scraping/boatosb.csv': {
                'format': 'csv',
                'overwrite': True
            }
        },
        'LOG_LEVEL':'WARNING'
    }    

    def parse(self, response):
        responses = response.xpath('*//article')
        next_page = response.xpath("*//li[@class='previous']/a/@href").get()

        for noticia in responses:
            item = {}
            
            item['titulo'] = noticia.xpath("*//h2[@class='entry-title']/a/text()").get()
            item['data'] = noticia.xpath("*//time[@class='entry-date published']/text()").get()
            item['autoria'] = noticia.xpath("normalize-space(*//a[@class='url fn n']/text())").get()
            item['label'] = verify_label_boatos(noticia.xpath("*//h2[@class='entry-title']/a/text()").get())
  
            ler_tudo = noticia.xpath("*//a[@class='more-link']/@href").get()
            yield response.follow(ler_tudo, callback=self.parse_noticia_completa, meta=item)
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_noticia_completa(self, response):
        item = {}

        item['titulo'] = response.meta["titulo"]
        item['data'] = response.meta["data"]

        item['autoria'] = response.meta["autoria"]
      
        try:
            tags = response.xpath("*//script[@class='yoast-schema-graph']/text()").re(r'keywords":(.+?])')[0]
            item['tags'] = ';'.join(re.findall(r'\"(.+?)\"', tags))
        except IndexError:
            item['tags'] = None
      
        item['principal'] = response.xpath("*//strong/text()").get()
        item['texto'] = response.xpath("*//article//p/text()").get()

        item['label'] = response.meta["label"]

        yield item

process = CrawlerProcess()
process.crawl(BoatosSpider)
process.start()