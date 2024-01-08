FROM shreyas001/helloworld:latest

COPY entrypoint.sh /entrypoint.sh

COPY . /check

RUN ls

ENTRYPOINT ["/entrypoint.sh"]
