from flask import Flask, Markup
application = Flask(__name__)

@application.route("/")
def test_escaping(self):
        text = '<p>Hello World!'
        app = flask.Flask(__name__)
        @app.route('/')
        def index():
            return flask.render_template('escaping_template.html', text=text,
                                         html=flask.Markup(text))
        lines = app.test_client().get('/').data.splitlines()
        self.assert_equal(lines, [
            b'&lt;p&gt;Hello World!',
            b'<p>Hello World!',
            b'<p>Hello World!',
            b'<p>Hello World!',
            b'&lt;p&gt;Hello World!',
            b'<p>Hello World!'
        ]) 

if __name__ == "__main__":
    application.run()
