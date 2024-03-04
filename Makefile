APPLICATION_NAME ?= fastapi-summarizer
CONTAINER_NAME ?= ${APPLICATION_NAME}-container
 
build:
#build and run the dockerfile
	docker build -t ${APPLICATION_NAME} .
	docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${APPLICATION_NAME}

delete:
#stop and delete the container
	docker container stop ${CONTAINER_NAME}
	docker container rm ${CONTAINER_NAME}

logs:
#find the logs for the container
	docker logs ${CONTAINER_NAME}

