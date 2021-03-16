FROM python:3
#FROM ubuntu:18.04
WORKDIR /root

RUN apt-get update
RUN apt install libgl1-mesa-glx -y

RUN pip3 install numpy opencv-python Flask requests

RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-Interface.git

RUN mv /root/AutomaticTraining-Interface/__init__.py /root
RUN mv /root/AutomaticTraining-Interface/static /root
RUN mv /root/AutomaticTraining-Interface/templates /root

ENTRYPOINT ["python3","__init__.py"]
