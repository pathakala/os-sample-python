from flask import Flask
application = Flask(__name__)

@application.route("/")
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, '''''!</h1>
    </body>
</html>'''

if __name__ == "__main__":
    application.run()
