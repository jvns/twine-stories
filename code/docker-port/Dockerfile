FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip 
RUN pip install redis flask
ADD code.py /code.py

CMD ["python3", "/code.py"]
