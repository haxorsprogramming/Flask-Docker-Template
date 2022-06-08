FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /home/pythonApps/imgcnn/app/static
COPY ./requirements.txt /home/pythonApps/imgcnn/requirements.txt
RUN pip install -r /home/pythonApps/imgcnn/requirements.txt