import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]/article'):
            text_value = cit.xpath('.//div[@class="figsco__quote__text"]/a/text()').extract_first()
            author = cit.xpath('.//div[@class="figsco__fake__col-9"]/a/text()').extract_first()
            
            if  not text_value == None :
                text_value = text_value[1:len(text_value)-1]
            yield { 'text' : text_value, "author" : author}