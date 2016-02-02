import os
import platform

from flask import Flask, render_template, request

app = Flask(__name__)


def shutdown():
    """Detect OS and run appropriate shutdown command"""
    if platform.system() == "Windows":
        os.system("shutdown /t 20 /f")
    else:
        os.system("shutdown now -h")


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        shutdown()
        return render_template('goodnight.html')
    else:
        return render_template('shutdown.html')


if __name__ == '__main__':
    app.run(port=9843, debug=True)
