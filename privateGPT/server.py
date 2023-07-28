import time
from flask import Flask, Response, render_template, request, stream_with_context
import privateGPT

from flask import Flask, Response
from langchain.callbacks.base import AsyncCallbackHandler

app = Flask("server")
gpt = privateGPT.prepare()

@app.route("/")
def init():
   return render_template('test.html')

@app.route("/ask")
def ask():
    args = request.args
    query = args.get("query", default="hello", type=str)
    print("query:", query)
    answer = privateGPT.enquire(gpt, query)
    return answer

@app.route("/ask-stream")
def ask_stream():
    args = request.args
    query = args.get("query", default="hello", type=str)
    print("query:", query)
    def generate():
        res = gpt(query)
        yield  res['result']
    return Response(generate(), mimetype="text/event-stream")

@app.route('/progress')
def progress():
    def progress_func():
        x = 0
        while x < 100:
            time.sleep(1)
            x = x + 10
            yield 'data:' + str(x) + "\n\n"
    return Response(progress_func(), mimetype='text/event-stream')
