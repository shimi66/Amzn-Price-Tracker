from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['Get', 'Post'])
def home():
    query = request.args.get('query')
    results = []
    if query:
        # todo search database and store results

        # Example: generating random time series data for demo
        start_date = datetime.now() - timedelta(days=50)
        results = [{'date': (start_date + timedelta(days=i)).strftime('%Y-%m-%d'),
                    'value': random.randint(50, 150)} for i in range(50)]

    return render_template('home.html', query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)