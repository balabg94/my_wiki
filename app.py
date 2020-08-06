from flask import Flask, render_template

import wiki

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<title>')
def view_page(title):
    content = wiki.load_page(title)
    return render_template('page.html', page_content=content, page_title=title)

if __name__ == '__main__':
    app.run(debug=True)
