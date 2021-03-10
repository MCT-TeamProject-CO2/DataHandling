FROM python:3.8

WORKDIR /usr/src/app

COPY config/requirements.txt ./config/
RUN pip install --no-cache-dir -r ./config/requirements.txt

COPY . .

RUN sudo openfortivpn sslvpn.howest.be -u firstname.lastname@student.howest.be -p "password" --trusted-cert 8a1949c10b938b29eea96b70426cd94647439c3c383c4cc40800714d59712246 &

CMD ["python", "-u", "main.py"]
