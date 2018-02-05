PROJECT := grio
NAME := p-service
DIR := $(shell pwd)

VERSION := 0.0.1
IMAGE_NAME := ${PROJECT}/${NAME}:${VERSION}
IMAGE_LATEST := ${PROJECT}/${NAME}:latest
TEST_CONTAINER := ${NAME}_test

image:
    docker build --rm -t ${IMAGE_NAME} .

test:
    docker run --rm postgres -d --name ${TEST_CONTAINER}-postgres && \
    docker run --rm --link ${TEST_CONTAINER}-postgres --name ${TEST_CONTAINER} ${IMAGE_LATEST}

clean:
    docker rm -f ${TEST_CONTAINER} ${TEST_CONTAINER}-postgres
