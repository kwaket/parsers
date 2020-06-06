# -*- coding: utf-8 -*-
import scrapy

from job.items import JobItem


class HhSpider(scrapy.Spider):
    name = 'hh'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/vacancy/36476804']

    def parse(self, response):
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

        xpath_t = './p/strong[contains(text(), "{}")]/ancestor::p/following::ul[1]/li/text()'
        item['responsibilities'] = vacancy_section.xpath(xpath_t.format(
            'Обязанности')).getall()
        item['requirements'] = vacancy_section.xpath(xpath_t.format(
            'Требования')).getall()
        item['conditions'] = vacancy_section.xpath(xpath_t.format(
            'Условия')).getall()
        item['as_a_plus'] = vacancy_section.xpath(xpath_t.format(
            'Будет преимуществом')).getall()
        item['skills'] = content.xpath(
            './/*[contains(@data-qa, "skills-element")]/span/text()'
            ).getall()

        item['address'] = content.xpath(
            './/p[@data-qa="vacancy-view-location"]//text()').getall()
        item['experience'] = content.xpath(
            './/*[@data-qa="vacancy-experience"]//text()').getall()
        item['employment_mode'] = content.xpath(
            './/*[@data-qa="vacancy-view-employment-mode"]//text()'
            ).getall()
        item['description'] = vacancy_section.get()
        item['url'] = response.request.url

        yield item
