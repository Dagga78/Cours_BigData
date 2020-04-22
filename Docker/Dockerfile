# base image
FROM ubuntu:latest

# un espace de travail appelé workspace
WORKDIR /workspace

# install python3, pip3 et vim
RUN sudo apt-get install python3.6 && sudo apt-get install python3-pip && sudo apt-get install vim

# install 
RUN pip-3.3 install -r requirements.txt

# un set up des credentials git pour l'utilisateur du container
RUN git clone https://github.com/Dagga78/Cours_BigData.git /workspace/Cours_BigData

# une exposition du port 8000 
EXPOSE 8000
