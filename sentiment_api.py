from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Please provide a \"message\" field in JSON'}), 400

    message = data['message']
    sentiment = get_sentiment(message)

    return jsonify({'message': message, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
