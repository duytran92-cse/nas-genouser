REGISTRY=registry.novogenialab.com

build:
	sudo docker build -f docker/Dockerfile-dev -t genopedia/user/front-web/dev .

release-test:
	sudo docker build --no-cache -f docker/Dockerfile-test -t genopedia/user/front-web/test .
	sudo docker tag genopedia/user/front-web/test $(REGISTRY)/genopedia/user/front-web/test
	sudo docker push $(REGISTRY)/genopedia/user/front-web/test

release-prod:
	sudo docker build --no-cache -f docker/Dockerfile-prod -t genopedia/user/front-web/prod .
	sudo docker tag genopedia/user/front-web/prod $(REGISTRY)/genopedia/user/front-web/prod
	sudo docker push $(REGISTRY)/genopedia/user/front-web/prod
