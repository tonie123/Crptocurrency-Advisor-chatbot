from flask import Flask, render_template, request, jsonify
from crypto_advisor import process_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('message', '')
    response = process_query(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)