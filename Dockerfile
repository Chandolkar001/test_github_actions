FROM shreyas001/helloworld:latest

COPY entrypoint.sh /entrypoint.sh

COPY . /check

ENTRYPOINT ["/entrypoint.sh"]
