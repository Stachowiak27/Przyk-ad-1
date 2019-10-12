
from flask import Flask, requests
from exam import movies

app = Flask(__name__)

@app.route('/movies', metods = ['GET', 'POST'])
def movie():
    if requests == "GET":
        f ="""
        <label>
        title:
            <input type = "text" name = "wprowadź tytuł>
        """
        return f




if __name__ == '__main__':
    app.run()
