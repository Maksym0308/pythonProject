import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
    current = 0
    max_page = 1

    def parse(self, response):
        rows = response.xpath('//div[@class="quote"]')
        for row in rows:
            text = row.xpath('.//span[@class="text"]/text()').get()
            author = row.xpath('.//small[@class="author"]/text()').get()
            yield {
                "text": text.strip('“”') if text else None,
                "author" : author
            }
        next_page = response.xpath('.//li[@class="next"]/a/@href').get()
        if next_page is not None and self.current < self.max_page:
            self.current +=1
            yield response.follow(next_page, callback=self.parse)
