test:
	rust test
	pytest tests/

benchmark:
	rust bench
	sudo stress-ng --cpu 8 --vm 4 --timeout 30s

format:
	rust fmt
	python -m black .

release: test
	rust build --release
	docker build -t agent-symphony .
	docker push agent-symphony