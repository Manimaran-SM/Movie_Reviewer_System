from flask import Flask, render_template, request
from Output import predict

app = Flask(__name__)
inputs=[]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    search=request.form['search']
    if(search==''):
        return render_template('index.html',message='please enter text Review')
    else:
        Prediction,percentage=predict(search)
        input=append(search)
        return render_template('index.html',message='Prediction: %s <br> Probability: %.2f%%' %(Prediction,percentage))

if __name__ == '__main__':
    app.run(debug=True)
