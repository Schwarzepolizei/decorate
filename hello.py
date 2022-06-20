from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is the paragraph</p>" \
           "<img src='https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif'>"


# def bold_decorate(bye_decorate):
#     def wrapper_bold():
#         return "<h1>"
#         bye_decorate()
#         return "</h1>"
#     return wrapper_bold


# @app.route("/bye")
@bold_decorate
def bye():
    return "Bye"


@app.route("/<username>/name")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
