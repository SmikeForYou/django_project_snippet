dev:
	docker-compose -f docker-compose.dev.yml up --build

local:
	docker-compose -f docker-compose.local.yml up --build