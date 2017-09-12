FROM python:3.4
MAINTAINER glyif <122@holbertonschool.com>
g
RUN git clone https://github.com/glyif/AirBnB_clone_v3.git ~/AirBnB
WORKDIR /root/AirBnB
RUN pip install -r requirements.txt

RUN HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=db HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app