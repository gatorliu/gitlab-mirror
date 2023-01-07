FROM python:3.7

WORKDIR /webapi
RUN mkdir -p /webapi/logs
RUN mkdir -p /webapi/repos

COPY requirements.txt /webapi/
RUN pip3 install -r requirements.txt

# 將內容複製到工作目錄中
COPY src/templates/* /webapi/templates
COPY src/app.py /webapi/

# 執行python的指令語法
CMD ["python3","app.py"]