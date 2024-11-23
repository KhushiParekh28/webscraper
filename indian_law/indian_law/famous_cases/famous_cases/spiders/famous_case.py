import scrapy

class FamousCasesSpider(scrapy.Spider):
    name = "famous_cases"
    start_urls = [
        'https://www.scobserver.in/journal/10-cases-that-shaped-india-in-2018/'  # Example URL
    ]

    def parse(self, response):
        # Modify the selector below based on the structure of the Wikipedia page
        for case in response.css("div.mw-parser-output > ul > li"):
            title = case.css("a::text").get()
            summary = case.css("::text").getall()

            yield {
                'title': title,
                'summary': ' '.join(summary).strip()
            }
        
        # Pagination (if applicable)
        next_page = response.css("a[title='next page']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
