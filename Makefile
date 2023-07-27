default:
	make build
	make run

build:
	rm -rf ./privateGPT/db
	python3 ./privateGPT/ingest.py

run:
	python3 ./privateGPT/privateGPT.py --hide-source

client:
	cd ./app && yarn start && cd ..
