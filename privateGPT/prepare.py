from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler, BaseCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import LlamaCpp
from constants import CHROMA_SETTINGS
from dotenv import load_dotenv

import os

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))

# Metal https://python.langchain.com/docs/integrations/llms/llamacpp#metal
n_gpu_layers = 1  # Metal set to 1 is enough.

def prepare_llm():
    # activate/deactivate the streaming StdOut callback for LLMs
    callbacks = [StreamingStdOutCallbackHandler()]
    
    # Prepare the LLM
    return LlamaCpp(stream=True, model_path=model_path, n_gpu_layers=n_gpu_layers, f16_kv=True, max_tokens=model_n_ctx, n_ctx=10000, n_batch=model_n_batch, callbacks=callbacks, verbose=True)

def prepare_retrieval_QA(llm):
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)

    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)
