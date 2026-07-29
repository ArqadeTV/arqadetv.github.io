from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # Flask automatically looks inside the 'templates' folder
    return render_template('index.html')

@app.route('/index.html')
def redirect_to_root():
    return redirect(url_for('home'), code=301)

if __name__ == '__main__':
    app.run(debug=False)
