from flask import Flask, render_template, request, url_for, redirect

import wiki

app = Flask(__name__)

@app.route('/')
def home():
    titles = wiki.list_topics()
    return render_template('home.html', page_titles=titles)

@app.route('/<title>/')
def view_page(title):
    content = wiki.load_page(title)
    return render_template('page.html', page_title=title, page_content=content)

@app.route('/write/', methods=['GET', 'POST'])
def write_page():
    if request.method == 'GET':
        return render_template('write.html')
    else:
        title = request.form['page_title']
        content = request.form['page_content']
        wiki.save_page(title, content)
        return redirect(url_for('view_page', title=title))
if __name__ == '__main__':
    app.run(debug=True)
