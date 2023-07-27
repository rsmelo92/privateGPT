default:
	make build
	make run

build:
	rm -rf ./privateGPT/db
	python3 ./privateGPT/ingest.py

run:
	PERSIST_DIRECTORY=privateGPT/db MODEL_PATH=privateGPT/models/LLAMA/vicuna-7b-v1.3-instruct-pl-lora.ggmlv3.q4_0.bin  python3 ./privateGPT/privateGPT.py --hide-source

client:
	cd ./app && yarn start && cd ..
