from flask import Flask
import webbrowser
import os

from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    if request.method == 'POST':
        pass
    
    # gives back the link to the images such that it gets displayed
    # should test the image with request (or something else) first
    img_src = "test.png"
    return render_template('register.html', img_src=img_src)



def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:2000/')

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=2000)

if __name__ == "__main__":
    main()