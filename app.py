from flask import Flask, render_template
import os

app = Flask(__name__)
APP_MESSAGE = os.getenv('APP_MESSAGE', 'Default Message')
APP_HEALTH = os.getenv('APP_HEALTH', 'Healthy')

@app.route('/')
def home():
    return render_template('home.html', message=APP_MESSAGE)

@app.route('/health')
def health():

    return render_template('health.html', health=APP_HEALTH)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
