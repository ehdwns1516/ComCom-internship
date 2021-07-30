from transformers import AutoTokenizer, pipeline
from flask import Flask, request, jsonify, render_template
from queue import Queue, Empty
from threading import Thread
import time

app = Flask(__name__)

print("model loading...")

# Model loading

tokenizer = AutoTokenizer.from_pretrained("ehdwns1516/bart_finetuned_xsum")

generator = pipeline(
    "summarization",
    model="ehdwns1516/bart_finetuned_xsum",
    tokenizer=tokenizer
)

requests_queue = Queue()    # request queue.
BATCH_SIZE = 1              # max request size.
CHECK_INTERVAL = 0.1

print("complete model loading")


def handle_requests_by_batch():
    while True:
        request_batch = []

        while not (len(request_batch) >= BATCH_SIZE):
            try:
                request_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for requests in request_batch:
                try:
                    requests["output"] = summarize(requests['input'][0], requests['input'][1], requests['input'][2], requests['input'][3])

                except Exception as e:
                    requests["output"] = e


handler = Thread(target=handle_requests_by_batch).start()

def summarize(min_words, max_words ,num_beams, context):
    try:
        result_list = list()
        result_dict = dict()
        result = generator(context, min_length=int(min_words), max_length=int(max_words), num_beams=int(num_beams), 
        num_return_sequences=int(num_beams), no_repeat_ngram_size=2)

        for item in result:
            result_list.append(item["summary_text"])

        for i in range(0, len(result_list)):
            result_dict[i] = result_list[i]

        return result_dict

    except Exception as e:
        print('Error occur in script generating!', e)
        return jsonify({'error': e}), 500


@app.route('/generate', methods=['POST'])
def generate():
    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'Error': 'Too Many Requests'}), 429

    try:
        args = []
        min_words = request.form['min_words']
        max_words = request.form['max_words']
        num_beams = request.form['num_beams']
        context = request.form['context']

        args.append(min_words)
        args.append(max_words)
        args.append(num_beams)
        args.append(context)

    except Exception as e:
        return jsonify({'message': 'Invalid request'}), 500

    req = {'input': args}
    requests_queue.put(req)

    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    return req['output']


@app.route('/queue_clear')
def queue_clear():
    while not requests_queue.empty():
        requests_queue.get()

    return "Clear", 200


@app.route('/healthz', methods=["GET"])
def health_check():
    return "Health", 200


@app.route('/')
def main():
    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')