from flask import render_template, Flask, request, redirect, url_for
from storage.storage_json import StorageJson

app = Flask(__name__)
storage = StorageJson()


@app.route('/')
def index():
    """
    Route for the index page. Displays the list of all blog posts.
    """
    blogs = storage.list_blogs()
    return render_template('index.html', blogs=blogs)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Route for adding a new blog post.
    Handles both GET (display the form) and POST (submit the form) requests.
    """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        storage.add_blog(title, content, author)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<string:post_id>')
def delete(post_id):
    """
    Route for deleting a blog post by its post ID.
    """
    storage.delete_blog(post_id)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom handler for 404 errors. Renders a custom 404 page.
    """
    return render_template('404.html'), 404


@app.route('/update/<string:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """
    Route for updating a blog post.
    Handles both GET (display the current post info) and POST (submit the update) requests.
    """
    post = storage.fetch_blog_by_id(post_id)
    if post is None:
        # Post not found
        return render_template('404.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        storage.update_blog(post_id, title, author, content)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


@app.route('/like/<string:post_id>', methods=['POST'])
def like(post_id):
    """
    Route for liking a blog post. Increments the like counter for the post by its post ID.
    """
    post = storage.fetch_blog_by_id(post_id)
    if post is None:
        # Post not found
        return render_template('404.html')
    if request.method == 'POST':
        storage.update_like(post_id)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
