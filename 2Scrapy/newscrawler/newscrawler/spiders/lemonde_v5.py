import scrapy
from scrapy import Request
from ..items import ArticleItem


class LemondeSpider(scrapy.Spider):
    name = "lemondev5"
    allowed_domains = ["www.lemonde.fr"]
    start_urls = ['https://www.lemonde.fr']

    def parse(self, response):
        title = response.css('title::text').extract_first()
        all_links = {
            name:response.urljoin(url) for name, url in zip(
            response.css("#nav-markup .Nav__item")[3].css("a::text").extract(),
            response.css("#nav-markup .Nav__item")[3].css("a::attr(href)").extract())
        }
        for link in all_links.values():
            yield Request(link, callback=self.parse_category)
            
    def parse_category(self, response):
        for article in response.css(".river")[0].css(".teaser"):
            title = article.css("h3::text").extract_first()
            image = article.css("img::attr(data-src)").extract_first()
            description = article.css(".teaser__desc::text").extract_first()
            yield ArticleItem(
                title=title,
                image=image,
                description=description
            )
