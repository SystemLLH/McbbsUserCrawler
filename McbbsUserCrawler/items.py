from scrapy import Item, Field


class McbbsusercrawlerItem(Item):

    uid = Field()
    username = Field()
    friend = Field()
    comment = Field()
    topic = Field()
    online_time = Field()
    reg_time = Field()
    point = Field()
    popularity = Field()
    gold_grain = Field()
    gold_ingot = Field()
    emerald = Field()
    nether_star = Field()
    contribution = Field()
    assistance = Field()
    diamond = Field()
