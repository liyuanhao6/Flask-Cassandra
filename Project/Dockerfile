# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6.3
COPY . /app
WORKDIR /app
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install -r requirements.txt
EXPOSE 8080 9042
CMD ["/bin/bash"]
# CMD ["python", "app.py"]