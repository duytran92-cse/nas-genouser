REGISTRY=registry.novogenialab.com

build:
	sudo docker build -f docker/Dockerfile-dev -t genopedia/user/admin-web/dev .

release-test:
	sudo docker build --no-cache -f docker/Dockerfile-test -t genopedia/user/admin-web/test .
	sudo docker tag genopedia/user/admin-web/test $(REGISTRY)/genopedia/user/admin-web/test
	sudo docker push $(REGISTRY)/genopedia/user/admin-web/test

release-prod:
	sudo docker build --no-cache -f docker/Dockerfile-prod -t genopedia/user/admin-web/prod .
	sudo docker tag genopedia/user/admin-web/prod $(REGISTRY)/genopedia/user/admin-web/prod
	sudo docker push $(REGISTRY)/genopedia/user/admin-web/prod
