from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
jinja2 = Environment()

template = """
    Hi, {}

    <form action="/" method="GET">
        <input type='text' name='name'>
        <button type='submit'>say_hello</button>
    </form>
"""

@app.route("/")
def index():
    name = request.values.get('name')
    if name == None:
        name = "Stranger"
    return jinja2.from_string(template.format(name)).render()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
