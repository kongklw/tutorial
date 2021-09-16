from mySpider.items import ItcastItem

def parse(self, response):
    #open("teacher.html","wb").write(response.body).close()
    # 存放老师信息的集合
    #items = []
    for each in response.xpath("//div[@class='li_txt']"):
        # 将我们得到的数据封装到一个 `ItcastItem` 对象
        item = ItcastItem()
        #extract()方法返回的都是字符串
        name = each.xpath("h3/text()").extract_first()
        title = each.xpath("h4/text()").extract_first()
        info = each.xpath("p/text()").extract_first()
        #items.append(item)
        #将获取的数据交给pipelines
        yield item

    # 返回数据，不经过pipeline
    #return items