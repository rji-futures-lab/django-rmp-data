.PHONY: env syncdbschema

env:
	echo 'DJANGO_SECRET_KEY=dev123' >> .env
	echo 'DATABASE_URL=psql://'`whoami`':@127.0.0.1:5432/rmp' >> .env
	echo 'DEBUG=True' >> .env

syncdbschema:
	dropdb rmp
	createdb rmp
	rm -f -r rmp/migrations
	python manage.py makemigrations rmp
	python manage.py migrate
