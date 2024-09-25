from flask import render_template, Flask, request, redirect, url_for
from storage.storage_json import StorageJson

app = Flask(__name__)
storage = StorageJson()


@app.route('/')
def index():
    blogs = storage.list_blogs()
    return render_template('index.html', blogs=blogs)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        storage.add_blog(title, content, author)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
