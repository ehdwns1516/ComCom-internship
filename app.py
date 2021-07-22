from transformers import AutoTokenizer, pipeline
from flask import Flask, request, jsonify, render_template
from queue import Queue, Empty
from threading import Thread
import time

app = Flask(__name__)

print("model loading...")

# Model loading

tokenizer_1_kor = AutoTokenizer.from_pretrained("ehdwns1516/gpt3-kor-based_gpt2_review_SR1")
tokenizer_2_kor = AutoTokenizer.from_pretrained("ehdwns1516/gpt3-kor-based_gpt2_review_SR2")
tokenizer_3_kor = AutoTokenizer.from_pretrained("ehdwns1516/gpt3-kor-based_gpt2_review_SR3")
tokenizer_4_kor = AutoTokenizer.from_pretrained("ehdwns1516/gpt3-kor-based_gpt2_review_SR4")
tokenizer_5_kor = AutoTokenizer.from_pretrained("ehdwns1516/gpt3-kor-based_gpt2_review_SR5")

tokenizer_1_en = AutoTokenizer.from_pretrained("ehdwns1516/gpt2_review_star1")
tokenizer_2_en = AutoTokenizer.from_pretrained("ehdwns1516/gpt2_review_star2")
tokenizer_3_en = AutoTokenizer.from_pretrained("ehdwns1516/gpt2_review_star3")
tokenizer_4_en = AutoTokenizer.from_pretrained("ehdwns1516/gpt2_review_star4")
tokenizer_5_en = AutoTokenizer.from_pretrained("ehdwns1516/gpt2_review_star5")

generator_1_kor = pipeline(
    "text-generation",
    model="ehdwns1516/gpt3-kor-based_gpt2_review_SR1",
    tokenizer=tokenizer_1_kor
)
generator_2_kor = pipeline(
    "text-generation",
    model="ehdwns1516/gpt3-kor-based_gpt2_review_SR2",
    tokenizer=tokenizer_2_kor
)
generator_3_kor = pipeline(
    "text-generation",
    model="ehdwns1516/gpt3-kor-based_gpt2_review_SR3",
    tokenizer=tokenizer_3_kor
)
generator_4_kor = pipeline(
    "text-generation",
    model="ehdwns1516/gpt3-kor-based_gpt2_review_SR4",
    tokenizer=tokenizer_4_kor
)
generator_5_kor = pipeline(
    "text-generation",
    model="ehdwns1516/gpt3-kor-based_gpt2_review_SR5",
    tokenizer=tokenizer_5_kor
)

generator_1_en = pipeline(
    "text-generation",
    model="ehdwns1516/gpt2_review_star1",
    tokenizer=tokenizer_1_en
)
generator_2_en = pipeline(
    "text-generation",
    model="ehdwns1516/gpt2_review_star2",
    tokenizer=tokenizer_2_en
)
generator_3_en = pipeline(
    "text-generation",
    model="ehdwns1516/gpt2_review_star3",
    tokenizer=tokenizer_3_en
)
generator_4_en = pipeline(
    "text-generation",
    model="ehdwns1516/gpt2_review_star4",
    tokenizer=tokenizer_4_en
)
generator_5_en = pipeline(
    "text-generation",
    model="ehdwns1516/gpt2_review_star5",
    tokenizer=tokenizer_5_en
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
                    requests["output"] = make_review(requests['input'][0], requests['input'][1], requests['input'][2])

                except Exception as e:
                    requests["output"] = e


handler = Thread(target=handle_requests_by_batch).start()

def del_dup(text):
    result_textList = list()
    d_text = text.split(' ')
    for word in d_text:
        if word not in result_textList:
            result_textList.append(word)
    return {'generated_text': " ".join(result_textList)}


def make_review(language ,star_rating, context):
    try:
        if language == "Korean":
            result = dict()
            if star_rating == "1":
                result[0] = del_dup(generator_1_kor(context)[0]["generated_text"])
                print(result)
                return result
            elif star_rating == "2":
                result[0] = del_dup(generator_2_kor(context)[0]["generated_text"])
                print(result)
                return result
            elif star_rating == "3":
                result[0] = del_dup(generator_3_kor(context)[0]["generated_text"])
                print(result)
                return result
            elif star_rating == "4":
                result[0] = del_dup(generator_4_kor(context)[0]["generated_text"])
                print(result)
                return result
            elif star_rating == "5":
                result[0] = del_dup(generator_5_kor(context)[0]["generated_text"])
                print(result)
                return result

        elif language == "English":
            result = dict()
            if star_rating == "1":
                result[0] = generator_1_en(context)[0]
                print(result)
                return result
            elif star_rating == "2":
                result[0] = generator_2_en(context)[0]
                print(result)
                return result
            elif star_rating == "3":
                result[0] = generator_3_en(context)[0]
                print(result)
                return result
            elif star_rating == "4":
                result[0] = generator_4_en(context)[0]
                print(result)
                return result
            elif star_rating == "5":
                result[0] = generator_5_en(context)[0]
                print(result)
                return result

    except Exception as e:
        print('Error occur in script generating!', e)
        return jsonify({'error': e}), 500


@app.route('/generate', methods=['POST'])
def generate():
    if requests_queue.qsize() > BATCH_SIZE:
        return jsonify({'Error': 'Too Many Requests'}), 429

    try:
        args = []
        sel_lan = request.form['sel_lan']
        star_rating = request.form['star_rating']
        context = request.form['context']

        args.append(sel_lan)
        args.append(star_rating)
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
    return render_template('main.html'), 200


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')