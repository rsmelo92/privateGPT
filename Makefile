default:
	make build
	make run

build:
	rm -rf ./db
	python3 ingest.py

run:
	python3 privateGPT.py --hide-source --mute-stream
