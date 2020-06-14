REGISTRY=registry.novogenialab.com

build:
	sudo docker build -f docker/Dockerfile-dev -t genopedia/user/api-web/dev .

release-test:
	sudo docker build --no-cache -f docker/Dockerfile-test -t genopedia/user/api-web/test .
	sudo docker tag genopedia/user/api-web/test $(REGISTRY)/genopedia/user/api-web/test
	sudo docker push $(REGISTRY)/genopedia/user/api-web/test

release-prod:
	sudo docker build --no-cache -f docker/Dockerfile-prod -t genopedia/user/api-web/test .
	sudo docker tag genopedia/user/api-web/prod $(REGISTRY)/genopedia/user/api-web/prod
	sudo docker push $(REGISTRY)/genopedia/user/api-web/prod
