from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return "hello world"

# @app.route('/my-link/')
# def my_link():
#   print ('I got clicked!')

#   return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)