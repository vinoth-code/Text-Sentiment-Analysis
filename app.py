from flask import Flask, request, jsonify
import mysql.connector
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",        # Change if your MySQL user is different
    password="09011",        # Add password if set
    database="sentiment_analysis"
)
cursor = db.cursor()

# Sentiment Analysis API
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text is required!"}), 400

    # Sentiment Analysis
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

    # Store in database
    sql = "INSERT INTO sentiments (input_text, sentiment_result) VALUES (%s, %s)"
    cursor.execute(sql, (text, sentiment))
    db.commit()

    return jsonify({"sentiment": sentiment})

# Run Flask Server
if __name__ == '__main__':
    app.run(debug=True)
