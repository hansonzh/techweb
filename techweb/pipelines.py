# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import time

class TechwebPipeline(object):
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(user = "root", passwd = "zhangjun", db = "techweb", host = "localhost", charset = "utf8", use_unicode = True)       
            self.cursor = self.conn.cursor()
            #print "----------------"
            #print "successfully init"
            #print "----------------"
        except MySQLdb.Error, e:
            print "Error %d, %s" % (e.args[0], e.args[1])

    '''
    create database techweb;
    create table article
    (
	id int not null primary key auto_increment,
	title varchar(255),
	url varchar(255),
	content varchar(1500),
	ltime date
    );
    '''
    def process_item(self, item, spider):
        #print "***********************"
        #print item['headTitle']
        #print item['url']
        #print item['description']
        #print "***********************"
        
        try:     
            sql = 'select * from article where url = "%s"' % item['url']
            self.cursor.execute(sql)
            if not self.cursor.fetchall():
                self.cursor.execute('insert into article(title, url, content, ltime) values (%s, %s, %s, %s)' , (item['headTitle'], item['url'], item['description'],time.strftime('%Y-%m-%d',time.localtime(time.time())) ))
                self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d, %s" % (e.args[0], e.args[1])
        
        return item
