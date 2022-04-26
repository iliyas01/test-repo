# todo reuse make
b:
	docker-compose build
d:
	docker-compose down
u:
	docker-compose up -d

# Dev
db:	
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	
dd:	
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
	
du:		
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
#restart comm after rebuild
dcomm:		
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build comm
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml restart comm
# Stage
sb:
	docker-compose -f docker-compose.yml -f docker-compose.stage.yml down
	docker-compose -f docker-compose.yml -f docker-compose.stage.yml build

sd:
	docker-compose -f docker-compose.yml -f docker-compose.stage.yml down

su:
	docker-compose -f docker-compose.yml -f docker-compose.stage.yml up


# ECS
eb:
	docker-compose -f docker-compose.ecs.stage.yaml down
	docker-compose -f docker-compose.ecs.stage.yaml build

ed:
	docker-compose -f docker-compose.ecs.stage.yaml down

eu:
	docker-compose -f docker-compose.ecs.stage.yaml up

ep:
	docker-compose -f docker-compose.ecs.stage.yaml push

debug:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down --remove-orphans
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

train:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
	docker-compose run -u root bot_engine train

# todo argument instead of comm_gateway
rerun comm:
	docker-compose build comm
	docker-compose up --no-deps -d comm

# rerun nginx:
# 	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build nginx
# 	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --no-deps -d nginx

#https://www.percona.com/blog/2019/08/21/cleaning-docker-disk-space-usage/
#https://www.omgubuntu.co.uk/2016/08/5-ways-free-up-space-on-ubuntu
prune:
	docker system prune --volumes
	docker image prune -a -f
	du -sh /var/cache/apt/archives
# rerun action:
#  	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --no-deps --build comm_gateway
help:
	@echo "make"
	@echo "    clean"
	@echo "        Remove Python/build artifacts."
	@echo "    formatter"
	@echo "        Apply black formatting to code."
	@echo "    lint"
	@echo "        Lint code with flake8, and check if black formatter should be applied."
	@echo "    types"
	@echo "        Check for type errors using pytype."


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf .pytype/
	rm -rf dist/
	rm -rf docs/_build

formatter:
	black comm --line-length 79

lint:
	flake8 comm
	black --check comm

types:
	pytype --keep-going comm