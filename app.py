import os
import difflib
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# PRODUCTION SECURITY: Kept for session validation on Render
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'fallback-local-dev-key')

# --- Core Application Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def redirect_to_root():
    return redirect(url_for('home'))

@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Merely serves the HTML layout; form processing is handled via frontend action
    return render_template('contact.html')

@app.route('/dashboard/settings')
def settings(): 
    return "Settings"

# --- Error Management Systems ---

@app.errorhandler(404)
def page_not_found(error):
    broken_path = request.path
    valid_routes = []
    for rule in app.url_map.iter_rules():
        if "static" not in rule.endpoint:
            valid_routes.append(rule.rule)
            
    suggestions = difflib.get_close_matches(broken_path, valid_routes, n=3, cutoff=0.4)
    return render_template('404.html', suggestions=suggestions), 404

if __name__ == '__main__':
    app.run(debug=False)
