from flask import Flask

main = Flask(__name__)


@main.route('/')
def index():
  return "Mahesh"


if __name__ == '__main__':
  main.run('0.0.0.0', debug=True)
