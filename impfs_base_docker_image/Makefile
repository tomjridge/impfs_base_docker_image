NAME:=impfs_base_docker_image
all:
	docker build -t $(NAME) .
#	docker run -ti $NAME bash

Dockerfile: FORCE
	./Generate.py

FORCE:
