from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True)
    #add comments
for i in range([1, 5]):
    print(i)
    if i == 4:
        print('Hi i am the formth i!')