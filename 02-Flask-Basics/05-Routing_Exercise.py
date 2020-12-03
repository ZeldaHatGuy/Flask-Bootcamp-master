from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return("<h1> Hello Puppy Lover! </h1>")

@app.route('/puppy/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] != 'y':
        puppyname = name + "y"
    elif name[-1] == "y":
        puppyname = name[:-1] + 'iful'
    return("Hello {}".format(puppyname))

if __name__ == '__main__':
    app.run(debug=True)