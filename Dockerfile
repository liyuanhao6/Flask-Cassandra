# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6.3
MAINTAINER AntoineLi <li15932804366@outlook.com>
COPY . /app
WORKDIR /app
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install -r requirements.txt --index-url https://pypi.tuna.tsinghua.edu.cn/simple/
EXPOSE 8080 9042
CMD ["python", "app.py"]