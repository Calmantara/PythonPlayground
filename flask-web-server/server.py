from flask import Flask

app = Flask(__name__)


def main():
    @app.route('/', methods=['GET'])
    def hello():
        return "Hello Ganteng"


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0',
            port=3000,
            debug=True)
