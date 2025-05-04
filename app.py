# Import the Flask class from the flask library
from flask import Flask

# Create an instance of the Flask class.
# __name__ tells Flask where to look for resources like templates and static files.
app = Flask(__name__)

# Define a route for the homepage ('/')
# The @app.route() decorator tells Flask what URL should trigger our function.
@app.route('/')
def hello_world():
  """This function will run when someone visits the homepage."""
  # Return the HTML string to be displayed in the browser
  return '<h1>Hello, World!</h1><p>This is my first Python web app!</p>'

# Ensure the app.run() block is removed or commented out
# For example:
# if __name__ == '__main__':
#   # DO NOT include the line below when deploying to Render
#   # app.run(host='0.0.0.0', port=5000, debug=True)
#   pass # Or just remove the whole if block