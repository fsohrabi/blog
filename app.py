from flask import render_template, Flask
from storage.storage_json import StorageJson

app = Flask(__name__)
storage = StorageJson()


@app.route('/')
def index():
    blogs = storage.list_blogs()
    return render_template('index.html', blogs=blogs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
