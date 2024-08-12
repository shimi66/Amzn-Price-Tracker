from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['Get', 'Post'])
def home():
    #render the HTML page
    return render_template('home.html')

@app.route('/data')
def data():
    # Placeholder time series data
    start_date = datetime.now() - timedelta(days=50)
    placeholder_data = {
        'labels': [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(50)],
        'dataValues': [random.randint(50, 150) for i in range(50)]
    }
    return jsonify(placeholder_data)

if __name__ == "__main__":
    app.run(debug=True)