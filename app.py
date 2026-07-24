from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Flask automatically looks inside the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
