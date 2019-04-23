# -*- coding: utf-8 -*-
import scrapy

import html2text

from y5000_crawler.items import Y5000CrawlerItem


class Y5000Spider(scrapy.Spider):
    name = 'y5000'
    allowed_domains = ['www.y5000.com']


    # start_urls = start_urls_map.values()

    start_urls = ["https://www.y5000.com/"]

    def parse(self, response):
        #
        data = response.xpath('//div[@class="cd_ls_cnt"]/a/@href').extract()

        for url in data:
            yield scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        # print(response.body.decode('utf-8'))

        page_data = response.xpath('//div[@class="pages"]//a[@class="next"]/@href').extract()



        if page_data and len(page_data) == 1:

            print("PAGE:-----------------------" + page_data[0])

            yield scrapy.Request(page_data[0], callback=self.parse_category)

        else:
            if len(page_data) == 2:

                print("NO PAGE:" + response.url + " {}".format(len(page_data))  +  " {}".format(page_data[0]) + " {}".format(page_data[1]))

                yield scrapy.Request(page_data[1], callback=self.parse_category)

        data = response.xpath('//div[@class="ls_zx_wz"]//div[@class="lzw_cont"]//a/@href').extract()

        for url in data:
            yield scrapy.Request(url, callback=self.parse_document)

    def parse_document(self, response):
        # print(response.body.decode('utf-8'))

        # pass

        data = response.xpath('//div[@class="lct_box"]')

        title = data.xpath('./div[@class="lct_tit"]/h1/text()').extract()[0]

        content = data.xpath('./div[@class="lct_cont"]').extract()[0]


        tags = data.xpath('//div[@class="lc_tt"]/a/text()').extract()



        content = html2text.html2text(content)


        text = """* * *

**下一章"""

        index = content.find(text)

        content = content[:index]

        item = Y5000CrawlerItem()
        item['title'] = title
        item['url'] = response.url
        item['content'] = content
        item['tags'] = tags

        # print(item['title'],item['link'],item['posttime'])
        yield item


        pass


#         <div class="ls_cl_tab">
#         <div class="lc_tt">
#     <span>本文标签：</span>
#     <a target="_blank" href=https://www.y5000.com/tags/xiaqi/>夏启</a>
#     <a target="_blank" href=https://www.y5000.com/tags/chanrangzhi/>禅让制</a>
# </div>
# <div class="lc_tb">
# <p>上一篇：<a  href="https://www.y5000.com/zgls/sgls/26453.html" >涿鹿之战：黄帝大战蚩尤</a></p>
# <p>下一篇：<a  href="https://www.y5000.com/zgls/sgls/24920.html" >远古时代中国历史介绍</a></p>
# </div>
# </div>




        pass

        #
        # for url in data:
        #     yield scrapy.Request(url, callback=self.parse_document)