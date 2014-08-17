# -*- coding: utf-8 -*-

# Scrapy settings for techweb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'techweb'

SPIDER_MODULES = ['techweb.spiders']
NEWSPIDER_MODULE = 'techweb.spiders'

CONCURRENT_REQUESTS = 1
DOWNLOAD_TIMEOUT = 1800

ITEM_PIPELINES = {
        'techweb.pipelines.TechwebPipeline': 300,
    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'techweb (+http://www.yourdomain.com)'
