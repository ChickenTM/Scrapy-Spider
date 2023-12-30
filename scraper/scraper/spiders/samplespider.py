import scrapy

class SampleSpider(scrapy.Spider):
    name = 'sample'
    proxy = "http://172.24.175.125:9090"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for quotes in response.css('div.quote'):
            yield { 
                'quote': quotes.css('span.text::text').get(),
                'author': quotes.css('small.author::text').get(),
                'tags': quotes.css('div.tags a.tag::text').getall()
            }

        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)