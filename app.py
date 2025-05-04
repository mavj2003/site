# Import Flask and the render_template function
from flask import Flask, render_template

# Create an instance of the Flask class.
# The static_folder argument tells Flask where to find CSS, JS, images
# The template_folder argument tells Flask where to find HTML templates
app = Flask(__name__, static_folder='static', template_folder='templates')

# Define a route for the homepage ('/')
@app.route('/')
def home():
  """Renders the index.html template."""
  # Instead of returning a string, we now render the HTML file from the 'templates' folder
  return render_template('index.html')

# This block is for local testing ONLY. Comment out or remove before deploying.
#if __name__ == '__main__':
 # app.run(debug=True, port=5000)