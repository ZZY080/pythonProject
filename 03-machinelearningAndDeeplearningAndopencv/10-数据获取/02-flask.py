import json
import os
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
# 配置apikey
openai.api_key = "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"
messages = [{"role": "user", "content": ""}]


@app.route('/')
def index():
    return render_template('text_chat_image.html')


@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [{"role": "user", "content": user_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response.choices[0].message["content"]
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)


@app.route('/gpt4chat', methods=['GET', 'POST'])
def gpt4chat():
    # messages = [{"role": "user", "content": ""}]
    while 1:
        try:
            user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
            if user_input == 'quit':
                break
            d = {"role": "user", "content": user_input}
            messages.append(d)  # 把输入添加到里面
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            content = response.choices[0].message["content"]  # 得到问题的答案
            d = {"role": "user", "content": content}
            messages.append(d)
        except RateLimitError:
            content = "The server is experiencing a high volume of requests. Please try again later."
        print(messages)
        return jsonify(content=messages)


@app.route('/gpt4image', methods=['GET', 'POST'])
def gpt4image():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    prompt = user_input
    print(user_input)

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            response_format="b64_json",
            size="512x512"
        )
        content = response['data'][0]['b64_json']
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."
    return jsonify(content=content)


if __name__ == '__main__':
    app.run(host='192.168.1.139', port=8000, debug=False)
