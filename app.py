from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>UVA SDS GPT</h1>'

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json() or {}
    text = data.get('text', '')
    return jsonify({'reply': text + '?'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
