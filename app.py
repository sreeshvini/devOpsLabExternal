from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    app.render_template(form.html) 
@app.route('/submit',methods=['POST'])
def submit():
    name = request.form('username')
    email = request.form('email')
    rollno = request.form('rollno')
    app.render_template('result.html',name,email,rollno) 
if __main__ == '__name__':
    app.run(debug = True) 

