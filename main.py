from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, word!'


if __name__ == '__main__':
    app.run()

# flask --app main.py run
