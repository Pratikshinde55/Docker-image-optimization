FROM redhat/ubi8
RUN yum install python36 -y
RUN pip3 install flask
WORKDIR /myapp
COPY app.py app.py
EXPOSE 5000
CMD ["pratik"]
ENTRYPOINT ["python3" , "app.py"]
