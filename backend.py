from flask import Flask
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Create a metric to track request duration
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # Start up the server to expose metrics.
    start_http_server(8080)
    app.run(debug=True, host='0.0.0.0')
