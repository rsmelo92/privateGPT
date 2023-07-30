#!/usr/bin/env python3
from prepare import prepare_llm, prepare_retrieval_QA
import time

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

def call_as_module(query):
    llm = prepare_llm()
    chain = prepare_retrieval_QA(llm)
    enquire(chain, query)

def main():
    llm = prepare_llm()
    chain = prepare_retrieval_QA(llm)
    while True:
        query = input("\nEnter a query: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue
        enquire(chain, query)

if __name__ == "__main__":
    main()
