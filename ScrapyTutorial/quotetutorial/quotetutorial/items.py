# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MarksItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    hall_ticket = scrapy.Field()
    student_name = scrapy.Field()
    current_branch = scrapy.Field()
    proctor_id = scrapy.Field()
    first_semester = scrapy.Field()
    second_semester = scrapy.Field()
    third_semester = scrapy.Field()
    fourth_semester = scrapy.Field()
    fifth_semester = scrapy.Field()
    sixth_semester = scrapy.Field()


