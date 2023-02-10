FROM python
RUN useradd -m work && cd /home/work && chmod 755 . 
RUN pip install flask && wget https://publictest.s3.ladydaily.com/MS/indocker.py && wget https://publictest.s3.ladydaily.com/MS/clientconfig.py
USER work
WORKDIR /home/work
