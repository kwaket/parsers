# -*- coding: utf-8 -*-
import scrapy

from job.items import JobItem


class HhSpider(scrapy.Spider):
    name = 'hh'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?area=1&text=Data+scientist'
    ]

    def parse(self, response):
        for href in response.xpath(
                '//a[@data-qa="vacancy-serp__vacancy-title"]/@href'):
            url = response.urljoin(href.extract().split('?')[0])
            yield scrapy.Request(url, callback=self.parse_item)

        next_page = response.xpath(
            '//a[@data-qa="pager-next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        item = JobItem()

        content = response.xpath(
            '(//div[@class="main-content"]//div[contains(@class, "bloko-column_container")])[1]')
        vacancy_section = content.xpath(
            '(//div[@class="vacancy-description"]/div[@class="vacancy-section"])[1]/div[1]')

        item['name'] = content.xpath(
            './/div[contains(@class, "vacancy-title")]/h1//text()').get()
        item['salary'] = content.xpath(
            './/p[@class="vacancy-salary"]//*/text()').getall()
        item['company'] = content.xpath(
            './/a[@data-qa="vacancy-company-name"]//*/text()').getall()
        item['address'] = content.xpath(
            './/p[@data-qa="vacancy-view-location"]//text()').getall()
        item['experience'] = content.xpath(
            './/*[@data-qa="vacancy-experience"]//text()').getall()
        item['employment_mode'] = content.xpath(
            './/*[@data-qa="vacancy-view-employment-mode"]//text()'
            ).getall()
        item['skills'] = content.xpath(
            './/*[contains(@data-qa, "skills-element")]/span/text()'
            ).getall()
        item['description'] = vacancy_section.get()
        item['url'] = response.request.url

        yield item
