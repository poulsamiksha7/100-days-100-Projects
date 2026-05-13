# Build a simple Flask portfolio site:

# Pages:
# 1. / → Home page (name, tagline, photo placeholder)
# 2. /about → About page (skills, education)
# 3. /projects → Projects page (list your 3 projects)
# 4. /contact → Contact page (email, LinkedIn, GitHub)

# Requirements:
# - Base template with navbar (template inheritance)
# - CSS in static folder
# - Clean Bootstrap 5 styling
# - All pages working

# File structure:
# portfolio/
#   app.py
#   templates/
#     base.html
#     index.html
#     about.html
#     projects.html
#     contact.html
#   static/
#     style.css

# Commit: "feat: personal portfolio Flask app"

from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('base.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)
