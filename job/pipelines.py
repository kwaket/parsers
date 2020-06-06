# -*- coding: utf-8 -*-
import re

from lxml.html.clean import Cleaner


class JobPipeline(object):
    def __init__(self):
        self.cleaner = Cleaner(style=True, links=True,
            add_nofollow=True, page_structure=False, safe_attrs=[],
            remove_tags=['svg', 'img'])

    def clean_html(self, html):
        html = self.cleaner.clean_html(html)
        return re.sub(r'\s+', ' ', html)

    def process_item(self, item, spider):
        item['description'] = self.clean_html(item['description'])
        return item