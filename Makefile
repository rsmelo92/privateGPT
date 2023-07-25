default:
	python3 privateGPT.py --hide-source --mute-stream

build:
	rm -rf ./db
	python3 ingest.py
