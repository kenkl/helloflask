FROM python:3.15.2-alpine3.23
RUN apk --no-cache add tzdata curl
RUN pip install Flask
RUN cp /usr/share/zoneinfo/America/New_York  /etc/localtime
COPY helloflask.py /helloflask.py
RUN chmod 755 /helloflask.py
EXPOSE 5000
CMD ["python", "/helloflask.py"]

