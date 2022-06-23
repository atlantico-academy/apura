# scrape webpage
import scrapy
from scrapy.crawler import CrawlerRunner
# text cleaning
import re
# Reactor restart
from crochet import setup, wait_for
setup()

#---------------------------------------------#
#-------------- G1 FATO OU FAKE --------------#
#---------------------------------------------#

def verify_label_G1(response):
    if (('#FAKE'or'FAKE') and ('FATO' or '#FATO')) in response:
        return 2
    if ('#FAKE'or'FAKE') in response:
        return 1
    if ('#FATO'or'FATO') in response:
        return 0
    else:
        return 3

class G1Spider(scrapy.Spider):
    name = 'G1Spider'
    start_urls = ['https://g1.globo.com/fato-ou-fake/'] 
    custom_settings = {
        'FEEDS': {
            '../data/raw/scraping/g1ff.csv': {
                'format': 'csv',
                'overwrite': True
            }
        }
    }    

    def parse(self, response):
        responses = response.xpath('*//div[@class ="feed-post-body"]')
        next_page = response.xpath("*//div[@class='load-more gui-color-primary-bg']/a/@href").get()
        #print(len(responses))

        for noticia in responses:
            item = {}
            
            item['title'] = noticia.xpath("*//a[@class='feed-post-link gui-color-primary gui-color-hover']/text()").extract()
            item['vinheta'] = noticia.xpath("*//span[@class='feed-post-metadata-section']/text()").extract()
            item['data'] = noticia.xpath("*//span[@class='feed-post-datetime']/text()").extract()
            item['lead'] = noticia.xpath('div[contains(@class,"feed-post-body-resumo")]/text()').extract()
            item['label'] = verify_label_G1(noticia.xpath("*//a[@class='feed-post-link gui-color-primary gui-color-hover']/text()").get())
            
            ler_tudo = noticia.xpath("*//a/@href").get()
            yield response.follow(ler_tudo, callback=self.parse_noticia_completa, meta=item)
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_noticia_completa(self, response):
        item = {}

        item['titulo'] = response.meta["title"]
        item['vinheta'] = response.meta["vinheta"]

        item['tempo'] = response.meta["data"]
        item['data_explicita'] = response.xpath("*//amp-timeago[@class='content-publication-data__amp-timeago']/text()").get()
        item['autoria'] = response.xpath("*//p[@class='content-publication-data__from']/text()").get()
        
        item['lead'] = response.meta["lead"]
        item['principal'] = response.xpath("*//p[@class='content-text__container theme-color-primary-first-letter']/text()").get()
        item['texto'] = response.xpath("*//p[@class='content-text__container ']/text()").get()

        item['label'] = response.meta["label"]
        
        yield item

@wait_for(timeout = 600)
def run_g1ff_spider():
    """run spider with G1Spider"""
    crawler = CrawlerRunner()
    d = crawler.crawl(G1Spider)
    return d

#----------------------------------------#
#-------------- BOATOS.ORG --------------#
#----------------------------------------#

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
        }
    }    

    def parse(self, response):
        responses = response.xpath('*//article')
        next_page = response.xpath("*//li[@class='previous']/a/@href").get()
        #print(len(responses))

        for noticia in responses:
            #print(':', end = "")
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
        #print(response.meta["data"], end = "\t")
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

@wait_for(timeout = 10)
def run_boatos_spider():
    """run spider with BoatosSpider"""
    crawler = CrawlerRunner()
    d = crawler.crawl(BoatosSpider)
    return d