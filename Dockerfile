FROM shreyas001/helloworld:latest

COPY entrypoint.sh /entrypoint.sh

COPY . /check

CMD [ "ls", "-a" ]

ENTRYPOINT ["/entrypoint.sh"]
