import difflib
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Define a few example routes
@app.route('/')
def home():
    # Flask automatically looks inside the 'templates' folder
    return render_template('index.html')

@app.route('/index.html')
def redirect_to_root():
    return redirect(url_for('home'))

@app.route('/about')
def about(): return "About"

@app.route('/contact-us')
def contact(): return "Contact"

@app.route('/dashboard/settings')
def settings(): return "Settings"

@app.errorhandler(404)
def page_not_found(error):
    # 1. Extract the typo path (e.g., "/abou" or "/contat")
    broken_path = request.path
    
    # 2. Collect all valid routes from the app, ignoring static files
    valid_routes = []
    for rule in app.url_map.iter_rules():
        if "static" not in rule.endpoint:
            valid_routes.append(rule.rule)
            
    # 3. Find up to 3 close matches (cutoff 0.4 allows looser matches)
    suggestions = difflib.get_close_matches(broken_path, valid_routes, n=3, cutoff=0.4)
    
    # 4. Pass the suggestions list to the template
    return render_template('404.html', suggestions=suggestions), 404
