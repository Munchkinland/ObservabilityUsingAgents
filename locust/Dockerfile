FROM locustio/locust

COPY locustfile.py /locustfile.py

CMD ["locust", "-f", "locustfile.py", "--host=http://web:5000"]
