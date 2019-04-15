.PHONY: env syncdbschema createrds deleterds recreaterds

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

createrds:
	aws --profile rji-futures-lab rds create-db-instance \
	--db-instance-identifier "rtk-dev" --db-name "rmp" \
	--db-instance-class "db.t2.micro" --engine "postgres" \
	--master-username "postgres" --master-user-password ${DB_PASSWORD} \
	--allocated-storage 20 --vpc-security-group-ids "sg-0f98cf25206b5c515" \
	--tags Key='name',Value='rtk'
	
	aws --profile rji-futures-lab rds wait db-instance-available \
	--db-instance-identifier "rtk-dev"
	
	zappa manage dev migrate

deleterds:
	aws --profile rji-futures-lab rds delete-db-instance \
	--db-instance-identifier "rtk-dev" --skip-final-snapshot \
	--delete-automated-backups
	
	aws --profile rji-futures-lab rds wait db-instance-deleted \
	--db-instance-identifier "rtk-dev"

recreaterds:
	make deleterds
	
	make createrds