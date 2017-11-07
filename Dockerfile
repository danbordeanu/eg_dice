FROM debian:latest

# let's set the local proxy
RUN echo 'Acquire::http::Proxy "http://webproxy.merck.com:8080";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::Proxy "https://webproxy.merck.com:8080";' >> /etc/apt/apt.conf

ADD code/ /code
RUN apt-get update
RUN apt-get install bash procps python-flask curl -y
WORKDIR /code
EXPOSE 5000
CMD ["python", "/code/dice.py"]
