import scrapy


class CasesSpiderSpider(scrapy.Spider):
    name = "cases_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org"]

    def parse(self, response):
        pass
