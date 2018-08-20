import scrapy


class CnBlogSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = ['http://www.cnblogs.com/pick/#p%s' % p for p in range(1, 11)]

    def parse(self, response):
        for article in response.xpath('//div[@class="post_item"]'):
            print(article.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first().strip())
            print(response.urljoin(article.xpath('div[@class="post_item_body"]/h3/a/@href').extract_first()).strip())
            print(article.xpath('div[@class="post_item_body"]/p/text()').extract_first().strip())
            print(article.xpath(
                'div[@class="post_item_body"]/div[@class="post_item_foot"]/a/text()').extract_first().strip())
            print(response.urljoin(article.xpath('div[@class="post_item_body"]/div/a/@href').extract_first()).strip())
            print(article.xpath(
                'div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_comment"]/a/text()').extract_first().strip())
            print(article.xpath(
                'div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_view"]/a/text()').extract_first().strip())
            print("")
            yield {
                'title': article.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first().strip(),
                'link': response.urljoin(
                    article.xpath('div[@class="post_item_body"]/h3/a/@href').extract_first()).strip(),
                'summary': article.xpath('div[@class="post_item_body"]/p/text()').extract_first().strip(),
                'author': article.xpath(
                    'div[@class="post_item_body"]/div[@class="post_item_foot"]/a/text()').extract_first().strip(),
                'author_link': response.urljoin(
                    article.xpath('div[@class="post_item_body"]/div/a/@href').extract_first()).strip(),
                'comment': article.xpath(
                    'div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_comment"]/a/text()').extract_first().strip(),
                'view': article.xpath(
                    'div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_view"]/a/text()').extract_first().strip(),
            }
