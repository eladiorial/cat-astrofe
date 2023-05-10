from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    gato = os.environ["gato"]
    return render_template('index.html', gato=gato)

if __name__ == "__main__":
    app.run(host="0.0.0.0")