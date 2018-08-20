import scrapy


class QQNewsSpider(scrapy.Spider):
    name = 'qqnews'
    start_urls = ['http://news.qq.com/society_index.shtml']

    def parse(self, response):
        for href in response.xpath('//*[@id="news"]/div/div/div/div/em/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        print(response.xpath('//div[@class="qq_article"]/div/h1/text()').extract_first())
        print(response.xpath('//span[@class="a_time"]/text()').extract_first())
        print(response.xpath('//span[@class="a_catalog"]/a/text()').extract_first())
        print("\n".join(response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p[@class="text"]/text()').extract()))
        print("")
        yield {
            'title': response.xpath('//div[@class="qq_article"]/div/h1/text()').extract_first(),
            'content': "\n".join(response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p[@class="text"]/text()').extract()),
            'time': response.xpath('//span[@class="a_time"]/text()').extract_first(),
            'cate': response.xpath('//span[@class="a_catalog"]/a/text()').extract_first(),
        }
