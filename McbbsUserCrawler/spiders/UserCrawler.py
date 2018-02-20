from scrapy.spiders import Spider, Request
from McbbsUserCrawler.items import McbbsusercrawlerItem
from data import insert_user


class UserCrawler(Spider):
    name = 'UserCrawler'
    start_urls = [r'http://www.mcbbs.net/?1']

    def parse(self, response):
        items = McbbsusercrawlerItem()
        items['uid'] = response.url.split('?')[1]
        if response.xpath(r'//div[@id="messagetext"]/p/text()').extract():
            print(items['uid'], "Not Found Get")
        else:
            try:
                items['username'] = str(response.xpath(r'//h2[@class="mt"]/text()').extract()[0]).split()[0]
                items['friend'], items['comment'], items['topic'] = \
                    map(lambda s: str.split(s)[1],
                        response.xpath('//ul[@class="cl bbda pbm mbm"]/li/a/text()').extract())
                items['online_time'] = response.xpath(r'//ul[@id="pbbs"]/li[1]/text()').extract()[0].split()[0]
                if not str.isdigit(items['online_time']):
                    items['online_time'] = '0'
                items['reg_time'] = response.xpath(r'//ul[@id="pbbs"]/li[2]/text()').extract()[0] + ":00"
                items['point'], items['popularity'], items['gold_grain'], items['gold_ingot'], \
                items['emerald'], items['nether_star'], items['contribution'], items['assistance'], items['diamond'] = \
                    map(lambda s: str.split(s)[0],
                        response.xpath(r'//div[@id="psts"]/ul/li[position()>1]/text()').extract())
            except:
                print(items['uid'], "Unusual Get")
            else:
                print(items['uid'], "Succeeded Get")
                insert_user(**items)

        yield Request(str('http://www.mcbbs.net/?%d' % (int(items['uid']) + 1)), callback=self.parse)
