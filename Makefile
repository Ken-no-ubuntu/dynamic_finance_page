run-db:
	docker-compose up -d

stop-db:
	docker-compose down

run-api:
	cd backend-api && cargo run

build-api:
	cd backend-api && cargo build

test-api:
	cd backend-api && cargo test
