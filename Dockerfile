FROM nandeuserbot/nandebot: nande

RUN git clone -b main https://github.com/sip-userbot/ShicyProject /home/Shicy/
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install -r https://raw.githubusercontent.com/sip-userbot/ShicyProject/main/requirements.txt

WORKDIR /home/Shicy

CMD ["python3","-m","Shicy"]
