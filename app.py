from flask import Flask, render_template, url_for, request, redirect

import wiki

app = Flask(__name__)

@app.route('/')
def home():
    titles = wiki.list_topics()
    return render_template('home.html', page_titles=titles)

@app.route('/<title>/')
def view_page(title):
    content = wiki.load_page(title)
    return render_template('page.html', page_content=content, page_title=title)

@app.route('/write/', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        wiki.save_page(title, content)
        return redirect(url_for('view_page', title=title))

if __name__ == '__main__':
    app.run(debug=True)
