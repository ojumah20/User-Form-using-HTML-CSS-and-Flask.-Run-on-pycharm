from flask import Flask, flash, render_template,request, session
from flask_session import Session 
app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

sess = Session()
sess.init_app(app)


""" This is the route that loads the form template
"""
@app.route('/')
def index():
    return render_template('index.html')


"""
This is the route that accepts the user data from the posted form, and writes it to a text file
"""
@app.route('/getvalue', methods = ['POST'])
def getvalue():

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    company = request.form['company']
    email = request.form['email']
    area_code = request.form['area_code']
    phone = request.form['phone']
    subject = request.form.get("user_subject")

    with open('result.txt', 'w') as f:
        f.write('################ User Registration Form ###################')
        f.write('\n\n')
        f.write(f'The Users firstname is: {firstname}')
        f.write('\n')
        f.write(f'The Users lastname is: {lastname}')
        f.write('\n')
        f.write(f'The Users company is: {company}')
        f.write('\n')
        f.write(f'The Users email is: {email}')
        f.write('\n')
        f.write(f'The Users area_code is: {area_code}')
        f.write('\n')
        f.write(f'The Users phone_number is: {phone}')
        f.write('\n')
        f.write(f'The Users selected subject is: {subject}')
        f.write('\n\n')
        f.write('############### User Registration Complete! ############### ')
    flash(f" Dear {firstname}, Your details was registered successfully", "success")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)