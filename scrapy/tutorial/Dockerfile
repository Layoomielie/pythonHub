FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD tutorial /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD scrapy crawl quotes
