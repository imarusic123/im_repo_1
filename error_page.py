from flask import Flask, render_template
app = Flask(__name__)


@app.route("/error")
def home():
    return render_template('error_html.html', test_var=5555)


if __name__ == '__main__':
    app.run(debug=True)
 