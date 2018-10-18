.PHONY: env

env:
	echo 'DJANGO_SECRET_KEY=dev123' >> .env
	echo 'DATABASE_URL=psql://'`whoami`':@127.0.0.1:5432/rmp' >> .env
	echo 'DEBUG=True' >> .env
