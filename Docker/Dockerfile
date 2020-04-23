# base image
FROM ubuntu:latest

# install python3, pip3 et vim
RUN apt-get update && apt-get -y install python3.6 python3-pip vim git

# un espace de travail appelé workspace
WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

# Clone git repo
RUN git clone https://github.com/Dagga78/Cours_BigData.git /workspace/Cours_BigData

# install
RUN pip3 freeze > requirements.txt && \
	pip3 install -r requirements.txt && \
	pip3 install jupyter

# une exposition du port 8000
EXPOSE 8888

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
