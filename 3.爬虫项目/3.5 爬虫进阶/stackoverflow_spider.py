import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.xpath('//*[@class="question-summary"]/div[2]/h3/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.xpath('//*[@id="question-header"]/h1/a/text()').extract(),
            'votes': response.xpath('//span[@itemprop="upvoteCount"]/text()').extract_first(),
            'body': response.xpath('//*[@id="question"]/table/tbody/tr[1]/td[2]/div/div[1]/text()').extract(),
            'tags': ",".join(response.xpath('//div[@class="post-taglist"]/a/text()').extract()),
            'link': response.url,
        }
