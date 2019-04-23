# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

md_head = """---
layout: "post"
title: "{title}"
date: "{date}"
categories: "{categories}"
description: "{description}"
tags: {tags}
url: {url}
---





"""

start_urls_map = {
    "https://www.y5000.com/zgls/sgls/": "上古历史",
    "https://www.y5000.com/zgls/xsz/": "夏商周历史",
    "https://www.y5000.com/zgls/cqzg/": "春秋战国历史",
    "https://www.y5000.com/zgls/qh/": "秦汉历史",
    "https://www.y5000.com/zgls/sglj/": "三国两晋历史",
    "https://www.y5000.com/zgls/nb/": "南北朝历史",
    "https://www.y5000.com/zgls/st/": "隋唐历史",
    "https://www.y5000.com/zgls/wdsg/": "五代十国历史",
    "https://www.y5000.com/zgls/xixialishi/": "西夏历史",
    "https://www.y5000.com/zgls/liaojinlishi/": "辽金历史",
    "https://www.y5000.com/zgls/sy/": "宋元历史",
    "https://www.y5000.com/zgls/mq/": "明清历史",
    "https://www.y5000.com/zgls/mg/": "民国历史",
    "https://www.y5000.com/zgls/ghg/": "共和国历史"
}


class Y5000CrawlerPipeline(object):
    def process_item(self, item, spider):

        category = ''

        for key in start_urls_map.keys():

            if item['url'].startswith(key):

                category = start_urls_map[key]


        tags = category
        if item['tags'] and len(item['tags']) > 0:
            tags = ' '.join(item['tags'])


        cwd = os.getcwd()
        date = '2018-12-17 16:15'
        head_content = md_head.format(title=item['title'], date=date, categories=category, description=item['title'], tags=tags, url=item['url'])

        path = os.path.join(cwd, 'results', category)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, '{}.md'.format(item['title'])), 'wb') as f:

            f.write(head_content.encode("utf-8"))

            f.write(item['content'].encode("utf-8"))

        return item
