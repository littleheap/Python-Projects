import scrapy


class JulyeduSpider(scrapy.Spider):
    name = "julyedu"
    start_urls = [
        'https://www.julyedu.com/category/index',
    ]

    def parse(self, response):
        for julyedu_class in response.xpath('//div[@class="course_info_box"]'):
            print(julyedu_class.xpath('a/h4/text()').extract_first())
            print(julyedu_class.xpath('a/p[@class="course-info-tip"][1]/text()').extract_first())
            print(julyedu_class.xpath('a/p[@class="course-info-tip"][2]/text()').extract_first())
            print(response.urljoin(julyedu_class.xpath('a/img[1]/@src').extract_first()))
            print("\n")

            yield {
                'title': julyedu_class.xpath('a/h4/text()').extract_first(),
                'desc': julyedu_class.xpath('a/p[@class="course-info-tip"][1]/text()').extract_first(),
                'time': julyedu_class.xpath('a/p[@class="course-info-tip"][2]/text()').extract_first(),
                'img_url': response.urljoin(julyedu_class.xpath('a/img[1]/@src').extract_first())
            }
