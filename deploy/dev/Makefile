USER_API_MYSQL_HOST_PORT=3300
USER_API_WEB_HOST_PORT=8000
USER_ADMIN_MYSQL_HOST_PORT=3301
USER_ADMIN_WEB_HOST_PORT=8001
USER_FRONT_MYSQL_HOST_PORT=3302
USER_FRONT_WEB_HOST_PORT=8002
USER_API_RABBITMQ_HOST_PORT=5900
USER_API_RABBITMQ_ADMIN_HOST_PORT=15800
GENOPEDIA_USER_HOME=$(GENOPEDIA_HOME)/genopedia-user

create-storage:
	sudo docker run -d --name=genopedia-dev.user-api.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true
	sudo docker run -d --name=genopedia-dev.user-admin.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true
	sudo docker run -d --name=genopedia-dev.user-front.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true

clear-storage:
	-sudo docker stop genopedia-dev.user-api.mysql.storage
	-sudo docker rm genopedia-dev.user-api.mysql.storage
	-sudo docker stop genopedia-dev.user-admin.mysql.storage
	-sudo docker rm genopedia-dev.user-admin.mysql.storage
	-sudo docker stop genopedia-dev.user-front.mysql.storage
	-sudo docker rm genopedia-dev.user-front.mysql.storage

deploy:
	sudo docker run -d --name=genopedia-dev.user-api.rabbitmq \
		-p $(USER_API_RABBITMQ_HOST_PORT):5672 \
		-p $(USER_API_RABBITMQ_ADMIN_HOST_PORT):15672 \
		registry.novogenialab.com/notasquare-zero/images/standard-rabbitmq:0.1
	sudo docker run -d --name=genopedia-dev.user-api.mysql \
		--volumes-from=genopedia-dev.user-api.mysql.storage \
		-p $(USER_API_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=genopedia-dev.user-api.web \
		--link genopedia-dev.user-api.mysql:mysql \
		--link genopedia-dev.user-api.rabbitmq:rabbitmq \
		-v $(GENOPEDIA_USER_HOME)/api-web/src/www:/opt/www \
		-p $(USER_API_WEB_HOST_PORT):80 \
		genopedia/user/api-web/dev

	sudo docker run -d --name=genopedia-dev.user-admin.mysql \
		-p $(USER_ADMIN_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=genopedia-dev.user-admin.web \
		--link genopedia-dev.user-admin.mysql:mysql \
		--link genopedia-dev.user-api.web:user-api \
		-v $(GENOPEDIA_USER_HOME)/admin-web/src/www:/opt/www \
		-p $(USER_ADMIN_WEB_HOST_PORT):80 \
		genopedia/user/admin-web/dev

	sudo docker run -d --name=genopedia-dev.user-front.mysql \
		-p $(USER_FRONT_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=genopedia-dev.user-front.web \
		--link genopedia-dev.user-front.mysql:mysql \
		--link genopedia-dev.user-api.web:user-api \
		-v $(GENOPEDIA_USER_HOME)/front-web/src/www:/opt/www \
		-p $(USER_FRONT_WEB_HOST_PORT):80 \
		genopedia/user/front-web/dev

	sudo cp nginx/genopedia-user-api-rabbitmq /etc/nginx/sites-enabled
	sudo cp nginx/genopedia-user-api-web /etc/nginx/sites-enabled
	sudo cp nginx/genopedia-user-admin-web /etc/nginx/sites-enabled
	sudo cp nginx/genopedia-user-front-web /etc/nginx/sites-enabled
	sudo service nginx reload

	sleep 10

	-sudo docker exec -it genopedia-dev.user-api.mysql mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS api_db;"
	-sudo docker exec -it genopedia-dev.user-api.web python /opt/www/manage.py migrate

	-sudo docker exec -it genopedia-dev.user-admin.mysql mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS admin_db;"
	-sudo docker exec -it genopedia-dev.user-admin.web python /opt/www/manage.py migrate
	-sudo docker exec -it genopedia-dev.user-admin.web python /opt/www/manage.py linkstatic

	-sudo docker exec -it genopedia-dev.user-front.mysql mysql -uroot -p123456 -e "CREATE DATABASE IF NOT EXISTS front_db;"
	-sudo docker exec -it genopedia-dev.user-front.web python /opt/www/manage.py migrate
	-sudo docker exec -it genopedia-dev.user-front.web python /opt/www/manage.py linkstatic

clean:
	-sudo docker stop genopedia-dev.user-admin.mysql
	-sudo docker stop genopedia-dev.user-admin.web
	-sudo docker stop genopedia-dev.user-api.rabbitmq
	-sudo docker stop genopedia-dev.user-front.mysql
	-sudo docker stop genopedia-dev.user-front.web
	-sudo docker stop genopedia-dev.user-api.mysql
	-sudo docker stop genopedia-dev.user-api.web

	-sudo docker rm genopedia-dev.user-admin.mysql
	-sudo docker rm genopedia-dev.user-admin.web
	-sudo docker rm genopedia-dev.user-api.rabbitmq
	-sudo docker rm genopedia-dev.user-front.mysql
	-sudo docker rm genopedia-dev.user-front.web
	-sudo docker rm genopedia-dev.user-api.mysql
	-sudo docker rm genopedia-dev.user-api.web

	-sudo rm /etc/nginx/sites-enabled/genopedia-user-api-web
	-sudo rm /etc/nginx/sites-enabled/genopedia-user-api-rabbitmq
	-sudo rm /etc/nginx/sites-enabled/genopedia-user-admin-web
	-sudo rm /etc/nginx/sites-enabled/genopedia-user-front-web

start:
	sudo docker start genopedia-dev.user-api.mysql
	sudo docker start genopedia-dev.user-api.web
	sudo docker start genopedia-dev.user-api.rabbitmq
	sudo docker start genopedia-dev.user-admin.mysql
	sudo docker start genopedia-dev.user-admin.web
	sudo docker start genopedia-dev.user-front.mysql
	sudo docker start genopedia-dev.user-front.web

stop:
	sudo docker stop genopedia-dev.user-api.mysql
	sudo docker stop genopedia-dev.user-api.web
	sudo docker stop genopedia-dev.user-api.rabbitmq
	sudo docker stop genopedia-dev.user-admin.mysql
	sudo docker stop genopedia-dev.user-admin.web
	sudo docker stop genopedia-dev.user-front.mysql
	sudo docker stop genopedia-dev.user-front.web

migrate:
	-sudo docker exec -it genopedia-dev.user-api.web python /opt/www/manage.py migrate
	-sudo docker exec -it genopedia-dev.user-admin.web python /opt/www/manage.py migrate
	-sudo docker exec -it genopedia-dev.user-front.web python /opt/www/manage.py migrate

ssh-api-rabbitmq:
	sudo docker exec -it genopedia-dev.user-api.rabbitmq bash

ssh-api-mysql:
	sudo docker exec -it genopedia-dev.user-api.mysql bash

ssh-api-web:
	sudo docker exec -it genopedia-dev.user-api.web bash

ssh-admin-mysql:
	sudo docker exec -it genopedia-dev.user-admin.mysql bash

ssh-admin-web:
	sudo docker exec -it genopedia-dev.user-admin.web bash

ssh-front-mysql:
	sudo docker exec -it genopedia-dev.user-front.mysql bash

ssh-front-web:
	sudo docker exec -it genopedia-dev.user-front.web bash
