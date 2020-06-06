# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Field


class JobItem(scrapy.Item):
    name = Field()
    salary = Field()
    company = Field()
    responsibilities = Field()
    requirements = Field()
    conditions = Field()
    as_a_plus = Field()
    skills = Field()
    address = Field()
    experience = Field()
    employment_mode = Field()
    url = Field()
