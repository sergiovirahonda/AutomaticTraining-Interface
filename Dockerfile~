FROM python:3
#FROM ubuntu:18.04
WORKDIR /root

RUN apt-get update
RUN apt install libgl1-mesa-glx -y
#RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install numpy opencv-python Flask requests

# If you're going to pull the code from GitHub repo
# RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-BaseCode.git

# RUN mv /root/AutomaticTraining-Interface/model_assembly.py /root
# RUN mv /root/AutomaticTraining-Interface/task.py /root
# RUN mv /root/AutomaticTraining-Interface/data_utils.py /root
# RUN mv /root/AutomaticTraining-Interface/email_notifications.py /root

COPY __init__.py ./__init__.py
COPY static ./static
COPY templates ./templates

ENTRYPOINT ["python3","__init__.py"]
