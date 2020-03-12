from flask import Flask, render_template, request
from Output import predict

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    input=[]
    search=request.form['search']
    if(search==''):
        return render_template('index.html',message='please enter text Review')
    else:
        input.append(search)
        Prediction,percentage=predict(input)
        return render_template('index.html',message='Prediction: %s <br> Probability: %.2f%%' %(Prediction,percentage))

if __name__ == '__main__':
    app.run(debug=True)
