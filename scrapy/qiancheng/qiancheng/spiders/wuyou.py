# -*- coding: utf-8 -*-
import re
import time

import scrapy
from scrapy import Spider, Request
from qiancheng.items import QianchengItem

class WuyouSpider(scrapy.Spider):
    name = 'wuyou'
    allowed_domains = ['www.51job.com']
    start_urls = ['https://www.51job.com/']
    url='https://search.51job.com/list/{city},000000,0000,00,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear={workyear}&cotype={cotype}&degreefrom={degree}&jobterm={jobterm}&companysize={companysize}&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=8&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    dayurl = 'https://search.51job.com/list/{city},000000,0000,00,0,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear={workyear}&cotype={cotype}&degreefrom={degree}&jobterm={jobterm}&companysize={companysize}&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=8&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    citydict={'010000':'北京','020000':'上海','030200':'广州','040000':'深圳','080200':'杭州','180200':'武汉','200200':'西安','070200':'南京','090200':'成都','060000':'重庆','030800':'东莞','230300':'大连','230200':'沈阳','070300':'苏州','250200':'昆明','190200':'长沙','150200':'合肥','080300':'宁波','170200':'郑州','050000':'天津','120300':'青岛','120200':'济南','030600':'佛山','030500':'珠海'}
    cotypedict={'01':'外资(欧美)','02':'外资(非欧美)','03':'合资','04':'国企','05':'民营公司','06':'外企代表处','07':'政府机关','08':'事业单位','09':'非盈利组织','10':'上市公司','11':'创业公司'}
    workyeardict={'01':'无经验','02':'1-3年','03':'3-5年','04':'5-10年','05':'10年以上'}
    companysizedict = {'01': '少于50人', '02': '50-150人', '03': '150-500人', '04': '500-1000人', '05': '1000-5000人', '06': '5000-10000人', '07': '10000人以上'}
    jobtermdict={'01':'全职','02':'兼职','03':'实习全职','04':'实习兼职'}
    degreedict={'01':'初中及以下','02':'高中/中技/中专','03':'大专','04':'本科','05':'硕士','06':'博士'}

    minprice = 0.0
    maxprice = 0.0
    avgprice = 0.0


    def start_requests(self):
        for city in self.citydict:
            for cotype in self.cotypedict:
                for workyear in self.workyeardict:
                    for companysize in self.companysizedict:
                        for jobterm in self.jobtermdict:
                            for degree in self.degreedict:
                                dict={'city':self.citydict[city],'cotype':self.cotypedict[cotype],'workyear':self.workyeardict[workyear],'companySize':self.companysizedict[companysize],'jobTerm':self.jobtermdict[jobterm],'degree':self.degreedict[degree]}
                                yield Request(self.url.format(city=city,cotype=cotype,workyear=workyear,companysize=companysize,jobterm=jobterm,degree=degree),self.parse,meta=dict)
                                #yield Request('https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',self.parse,meta=dict)


    def parse(self, response):
        lines=response.css('#resultList div.el:not(div.title)')
        dict = response.meta
        for line in lines:
            url=line.css('p.t1 span a::attr(href)').extract_first()
            regioninfo=line.css('span.t3::text').extract_first()
            region='未知'
            if '-' in regioninfo:
                region=regioninfo.split('-')[1]
            price = line.css('span.t4::text').extract_first()
            self.avgprice = 0.0
            self.minprice = 0.0
            self.maxprice = 0.0
            if (price!=None):
                self.priceFormat(str(price))
            date=line.css('span.t5::text').extract_first()
            year = time.strftime("%Y", time.localtime())
            date=year+'-'+date
            dict['region']=region
            dict['date'] = date
            avgprice=round(self.avgprice,2)
            minprice = round(self.avgprice, 2)
            maxprice=round(self.avgprice,2)
            if(avgprice>20):
                print(response.url)
                print('aa')
            dict['minprice']=minprice
            dict['maxprice']=maxprice
            dict['avgprice']=avgprice
            yield Request(url,self.parse1,meta=dict)
        nexturl=response.css('#resultList  div.dw_page div.p_in li.bk a::attr(href)').extract_first()
        if(nexturl!=None):
            yield Request(str(nexturl),self.parse,meta=dict)

    def parse1(self, response):

        header=response.css('div.tHeader div.cn')
        position=header.css('h1::attr(title)').extract_first()
        price=header.css('strong::text').extract_first()

        sider=response.css('div.tCompany_sidebar')
        company=sider.css('div.com_msg a.com_name p::attr(title)').extract_first()
        companyType=sider.css('div.com_tag p:nth-last-child(1)::attr(title)').extract_first()

        main=response.css('div.tCompanyPage  div.tCompany_main')
        profession=str(main.css('div.tBorderTop_box div.mt10 a.tdn::text').extract_first())
        profession=re.sub('\t','',profession)
        profession=re.sub('\n','',profession)
        profession = re.sub('\r', '', profession)

        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dict = response.meta
        item=QianchengItem()
        if(len(position)>30):
            return
        if(dict==None):
            return
        if(position==None):
            return
        if(company==None):
            return
        item['position'] = position
        item['company'] = company
        item['city'] = dict['city']
        item['region'] = dict['region']
        item['date'] = dict['date']
        item['time'] = t
        item['maxPrice'] = dict['maxprice']
        item['minPrice'] = dict['minprice']
        item['avgPrice'] = dict['avgprice']
        item['profession'] = profession
        item['companyType'] = companyType
        item['cotype'] = dict['cotype']
        item['degree'] = dict['degree']
        item['workyear'] = dict['workyear']
        item['companySize'] = dict['companySize']
        item['jobTerm'] = dict['jobTerm']
        yield item


    def priceFormat(self,price):
        print(price)
        if(price.find('月')!=-1):
            if(price.find('万')!=-1):
                if(price.find('-')!=-1):
                    minprice = price.split('-')[0]
                    maxprice = price.split('-')[1]
                    maxprice=re.search('\d*\.?\d*', maxprice).group()
                    self.minprice=float(minprice)*10
                    self.maxprice = float(maxprice)*10
                    self.avgprice=(self.minprice+self.maxprice)/2
            elif(price.find('千')!=-1):
                if (price.find('-')!=-1):
                    minprice = price.split('-')[0]
                    maxprice = price.split('-')[1]
                    maxprice = re.search('\d*\.?\d*', str(maxprice)).group()
                    self.minprice = float(minprice)
                    self.maxprice = float(maxprice)
                    self.avgprice = (self.minprice + self.maxprice) / 2
        elif(price.find('年')!=-1):
            if (price.find('万')!=-1):
                if (price.find('-')!=-1):
                    minprice = price.split('-')[0]
                    maxprice = price.split('-')[1]
                    maxprice = re.search('\d*\.?\d*', str(maxprice)).group()
                    self.minprice = float(minprice) * 10/12
                    self.maxprice = float(maxprice) * 10/12
                    self.avgprice = (self.minprice + self.maxprice) / 2
            elif (price.find('千')!=-1):
                if (price.find('-')!=-1):
                    minprice = price.split('-')[0]
                    maxprice = price.split('-')[1]
                    maxprice = re.search('\d*\.?\d*', str(maxprice)).group()
                    self.minprice = float(minprice)/12
                    self.maxprice = float(maxprice)/12
                    self.avgprice = (self.minprice + self.maxprice) / 2
        elif(price.find('天')!=-1):
            if(price.find('元')!=-1):
                maxprice = re.search('\d*\.?\d*', str(price)).group()
                self.minprice = float(maxprice) /1000*30
                self.maxprice = self.minprice
                self.avgprice = self.minprice
