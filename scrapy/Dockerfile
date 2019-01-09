FROM python:3.6
ENV PATH /usr/local/bin:$PATH
RUN pip3 install -r requirements.txt
RUN mkdir /gerapy
RUN cd ./gerapy
RUN gerapy init
RUN cd gerapy
RUN gerapy migrate
EXPOSE 8000
CMD gerapy runserver