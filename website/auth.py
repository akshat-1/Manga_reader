from flask import Blueprint, render_template, request, flash,redirect,url_for,session
from scrapper import *
result = None
auth = Blueprint('auth' , __name__)

result = []

@auth.route('/home')
def home():
    return render_template('home.html')

@auth.route('/search',  methods = ['GET','POST'])
def sumbit():
    if request.method == 'POST':
        user_input = str(request.form.get('search'))
        url = search_(user_input)
        result = get_search_result(url)
        if(len(result) >=1):
            return redirect(url_for('auth.results'))
        else:
            flash('NO RESULTS FOUND! TRY SEARCHING SOMETHING ELSE')


    return render_template('sumbit.html')

@auth.route('/results')
def results():
    # if request.method == 'POST':
    return render_template("results.html", result =result)

# @auth.route('/sign-up')
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         firstname = request.form.get('firstname')
#         password1 = request.form.get('passowrd1')
#         password2 = request.form.get('passowrd2')

#         if (len(email)) <4:
#             flash('EMAIL MUST BE GREATER THAN 4 CHAR', category='error')
#         elif len(firstname) <2:
#            flash('first name must be greater than 2 char', category='error')
#         elif len(password1 < 7):
#             flash('password too short must be greater than 7 chars', category='error')
#         elif password1 != password2:
#             flash('passwords no not match', category='error')
#         else:
#             flash('SUCCESS!!!', category='success')


#     return render_template("signup.html")

