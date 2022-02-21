# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import csv


class InstagramParserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        client.drop_database('ig1402')
        self.mongobase = client.ig1402

    def process_item(self, item, spider):
        try:
            collection = self.mongobase[item['profile_username']]
            collection.insert_one(item)
        except Exception as e:
            print(e)
        return item


class CSVPipeline(object):
    def __init__(self):
        self.file = 'data.csv'
        with open(self.file, 'r', newline='') as csv_file:
            self.tmp_data = csv.DictReader(csv_file)

        self.csv_file = open(self.file, 'a', newline='', encoding='utf-8')

    def process_item(self, item, spider):
        columns = item.fields.keys()

        data = csv.DictWriter(self.csv_file, columns)
        if not self.tmp_data:
            data.writeheader()
            self.tmp_data = True
        data.writerow(item)
        return item

    def __del__(self):
        self.csv_file.close()
