build:
	docker-compose -p twf build	

init:
	docker-compose -p twf up -d
	sleep 5
	docker-compose -p twf exec web python manage.py migrate

create superuser:
	docker-compose -p twf run web python manage.py createsuperuser

stop:
	docker stop twf_web_1 twf_db_1

make_migrations:
	docker-compose -p twf exec web python manage.py makemigrations

down:
	docker-compose -p twf down