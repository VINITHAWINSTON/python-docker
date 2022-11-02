from flask import Flask, render_template
import flask
app = Flask(__name__)

@app.route('/')
def index():
    print("Hello World, from Vector Victors.")

if __name__ == '__main__':
    app.run(debug=True)
