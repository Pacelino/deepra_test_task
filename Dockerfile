FROM ubuntu:latest
LABEL authors="danilkushnerov"

ENTRYPOINT ["top", "-b"]