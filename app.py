import os
from flask import Flask, render_template
import re # Import regular expressions for sorting

app = Flask(__name__, static_folder='static', template_folder='templates')
IMAGE_FOLDER = os.path.join(app.static_folder, 'images')
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

def sort_key_natural(filename):
    name_part = os.path.splitext(filename)[0]
    parts = re.split('([0-9]+)', name_part)
    return [int(part) if part.isdigit() else part.lower() for part in parts]

@app.route('/')
def gallery():
    image_files = []
    try:
        all_files = os.listdir(IMAGE_FOLDER)
        valid_files = sorted(
            [f for f in all_files if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS],
            key=sort_key_natural,
            reverse=True
        )
        for filename in valid_files:
            date_str = os.path.splitext(filename)[0]
            image_files.append({'filename': filename, 'date': date_str})
    except FileNotFoundError:
        print(f"Error: Image folder not found at {IMAGE_FOLDER}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return render_template('index.html', images=image_files)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
