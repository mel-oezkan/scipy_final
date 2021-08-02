from flask import Flask
import webbrowser
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:2000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=2000)

if __name__ == "__main__":
    main()