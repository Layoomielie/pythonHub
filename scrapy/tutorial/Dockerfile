FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip3 install scrapy
RUN pip3 install pymongo
CMD scrapy crawl quotes
