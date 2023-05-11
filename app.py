from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]
model_engine = "text-davinci-003" # Change this to the GPT model you want to use

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)
