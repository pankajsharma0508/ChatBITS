from flask import Flask, render_template

# Initialize the app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1>"

# Define another route
@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask web application.</p>"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
