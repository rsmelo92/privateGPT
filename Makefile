default:
	make build
	make run

build:
	rm -rf ./privateGPT/db
	python3 ./privateGPT/ingest.py

run:
	python3 ./privateGPT/privateGPT.py

client:
	cd ./app && yarn start && cd ..

server:
	cd ./privateGPT && python3 -m flask run --port 8000 && cd ..
