# Flask Blog Application

A simple blog app built with Flask. Users can create, update, delete, and like blog posts.

## Setup

1. Clone the repo:  
   `git clone https://github.com/fsohrabi/blog.git`

2. Navigate to the directory:  
   `cd blog`

3. Create and activate a virtual environment:  
   `python3 -m venv venv && source venv/bin/activate`

4. Install dependencies:  
   `pip install -r requirements.txt`

5. Run the app:  
   `python app.py`

6. Open `http://127.0.0.1:5004` in your browser.

## Routes

- `/`: List all posts.
- `/add`: Add a new post.
- `/update/<post_id>`: Update a post.
- `/delete/<post_id>`: Delete a post.
- `/like/<post_id>`: Like a post.

## License

MIT License
