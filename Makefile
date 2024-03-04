APPLICATION_NAME ?= fastapi-summarizer
CONTAINER_NAME ?= ${APPLICATION_NAME}-container
 
build:
	docker build -t ${APPLICATION_NAME} .
	docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${APPLICATION_NAME}

delete:
	docker container stop ${CONTAINER_NAME}
	docker container rm ${CONTAINER_NAME}

