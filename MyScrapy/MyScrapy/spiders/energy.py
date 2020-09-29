import scrapy


class EnergySpider(scrapy.Spider):
    name = 'energy'
    allowed_domains = ['www.energy-chemical.com']
    start_urls = ['https://www.energy-chemical.com/']

    def parse(self, response):
        pass
