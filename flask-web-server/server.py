from flask import Flask, render_template

app = Flask(__name__)


def main():
    @app.route('/<name>', methods=['GET'])
    def hello(name):
        return render_template("home/index.html", myname=name.upper())

    @app.route('/get', methods=['GET'])
    def get():
        return render_template("home/index.html")


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0',
            port=3000,
            debug=True)
