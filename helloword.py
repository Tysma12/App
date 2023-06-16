from flask import Flask

 

app = Flask(__name__)

 


@app.route('/')
def hello_world():  # put application's code here
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>page</title>
</head>
<body>
<h1>C'est une page html</h1>
</body>
</html>"""

 


if __name__ == '__main__':
    app.run()

