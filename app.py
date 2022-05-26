# Flask Setup
from flask import Flask, jsonify

app = Flask(__name__)


# Flask Routes
@app.route('/')
def homepage():
    return(
        f'Welcome!<br/>'
        f"Available Routes:<br/>"
    )

if __name__ == "__main__":
    app.run(debug=True)