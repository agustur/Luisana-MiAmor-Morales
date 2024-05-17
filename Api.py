from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    LM = "Luisana Morales te amoooooooooooooooo<3"
    return LM

if __name__ == '__main__':
    app.run()
