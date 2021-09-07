from flask import Flask




app = Flask(__name__) #create a flask object

@app.route('/')
def hello_words():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug= False ) #debug enabled is creating warning and error

