from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['Get', 'Post'])
def hello():
    query = request.args.get('query')
    results = None
    if query:
        # todo search database and store results

        # temporary values for prototyping
        results = [f"Result {i} for '{query}'" for i in range(1, 6)]

    return render_template('home.html', query=query, results=results)

@app.route('/search')
def search():
    query = request.args.get('query')
    # todo search database

    # temporary return value
    return f"Search results for: {query}"

if __name__ == "__main__":
    app.run(debug=True)