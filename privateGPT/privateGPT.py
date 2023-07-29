#!/usr/bin/env python3
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler, BaseCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import LlamaCpp
from queue import SimpleQueue

import os
import time

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

# Metal https://python.langchain.com/docs/integrations/llms/llamacpp#metal
n_gpu_layers = 1  # Metal set to 1 is enough.

from constants import CHROMA_SETTINGS

# q = SimpleQueue()
# # Custom callback for streaming
# class StreamingGradioCallbackHandler(BaseCallbackHandler):
#     def __init__(self, q: SimpleQueue):
#         self.q = q

#     def on_llm_new_token(self, token: str) -> None:
#         self.q.put(token)


def enquire(chain, query):
    # Get the answer from the chain
    start = time.time()
    res = chain(query)
    answer = res['result']
    end = time.time()

    print("\n\n> Question:")
    print(query)
    print(f"\n> Answer (took {round(end - start, 2)} s.):")
    print(answer)

    return answer

def prepare():
    # Parse the command line arguments
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    
    # activate/deactivate the streaming StdOut callback for LLMs
    callbacks = [StreamingStdOutCallbackHandler()]
    
    # Prepare the LLM
    llm = LlamaCpp(stream=True, model_path=model_path, n_gpu_layers=n_gpu_layers, f16_kv=True, max_tokens=model_n_ctx, n_batch=model_n_batch, callbacks=callbacks, verbose=True)

    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)

def call_as_module(query):
    chain = prepare()
    enquire(chain, query)

def main():
    chain = prepare()
    while True:
        query = input("\nEnter a query: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue
        enquire(chain, query)

if __name__ == "__main__":
    main()
