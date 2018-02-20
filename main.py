from scrapy import cmdline
from data import init_database, open_database


if __name__ == '__main__':
    open_database()
    init_database()
    name = 'UserCrawler'
    cmdline.execute(('scrapy crawl ' + name).split())
