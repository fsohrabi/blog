import json
import os
import uuid
from storage.istorage import IStorage


def generate_simple_uuid():
    return str(uuid.uuid4())


class StorageJson(IStorage):
    file_path = 'blogs.json'

    def __init__(self):
        self.blogs = self.load_data()  # Load existing data

    def list_blogs(self):
        """Retrieve and optionally filter or sort posts from the database."""
        return self.blogs

    def fetch_blog_by_id(self, id):
        """Retrieve and optionally post from the database by id."""
        for blog in self.blogs:
            if blog['id'] == id:
                return blog
        return None

    def add_blog(self, title, content, author):
        """Add a new blog to the database."""

        self.blogs.append(
            {"id": generate_simple_uuid(), 'title': title, 'content': content, 'author': author})
        self.rewrite_data()
        return True

    def update_blog(self, id, title, author, content):
        """update blog from the database."""
        for blog in self.blogs:
            if blog['id'] == id:
                blog['title'] = title
                blog['content'] = content
                blog['author'] = author
                self.rewrite_data()
                return True
        return False

    def delete_blog(self, id):
        """Delete a blog from the database by title."""
        for blog in self.blogs:
            if blog['id'] == id:
                self.blogs.remove(blog)
                self.rewrite_data()  # Persist changes
                return True
        return False

    def load_data(self):
        """Loads blogs data from a JSON file."""
        folder_name = 'data'
        StorageJson.file_path = os.path.join(folder_name, StorageJson.file_path)
        directory = os.path.dirname(StorageJson.file_path)
        # Check if the directory exists, if not, create it
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        if os.path.exists(StorageJson.file_path):
            try:
                with open(StorageJson.file_path, "r") as handle:
                    return json.load(handle)  # Directly load from the file
            except json.JSONDecodeError:
                # Handle the case where the file exists but contains invalid JSON
                print(f"Error: Corrupted JSON file at {StorageJson.file_path}. Resetting data.")
                return []
        else:
            with open(StorageJson.file_path, "w") as handle:
                json.dump([], handle)  # Write an empty list to the file
            return []

    def rewrite_data(self):
        """Write the updated blog data back to the JSON storage."""
        try:
            with open(StorageJson.file_path, "w") as handle:
                json.dump(self.blogs, handle, indent=4)  # Indentation for readability
        except Exception as e:
            print(f"Error writing to file: {e}")
