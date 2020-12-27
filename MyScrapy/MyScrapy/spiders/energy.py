import scrapy
from loguru import logger


class EnergySpider(scrapy.Spider):
    # 唯一表示
    name = 'energy'
    # 允许的域名
    allowed_domains = ['www.energy-chemical.com']
    # 起始的url
    start_urls = ['https://www.energy-chemical.com/']

    def parse(self, response):
        print(response)
        # pass
