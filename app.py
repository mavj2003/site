import os
from flask import Flask, render_template, jsonify
import re

app = Flask(__name__, static_folder='static', template_folder='templates')
IMAGE_FOLDER = os.path.join(app.static_folder, 'images')
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

def sort_key_natural(filename):
    name_part = os.path.splitext(filename)[0]
    parts = re.split('([0-9]+)', name_part)
    return [int(part) if part.isdigit() else part.lower() for part in parts]

def get_gallery_images():
    image_data = []
    try:
        all_files = os.listdir(IMAGE_FOLDER)
        valid_files = [f for f in all_files if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS]
        # Ändrat till reverse=True för att sortera SENAST först
        valid_files.sort(key=sort_key_natural, reverse=True)
        for filename in valid_files:
            date_str = os.path.splitext(filename)[0]
            image_data.append({'filename': filename, 'date': date_str})
    except FileNotFoundError:
        print(f"Error: Image folder not found at {IMAGE_FOLDER}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return image_data

@app.route('/')
def gallery_page():
    images_list = get_gallery_images()
    return render_template('index.html', images=images_list)

@app.route('/api/images')
def gallery_api():
    images_list = get_gallery_images()
    return jsonify(images_list)

# Kommentera ut/ta bort raderna nedan för deployment till Render
#if __name__ == '__main__':
#     app.run(debug=True, port=5000)