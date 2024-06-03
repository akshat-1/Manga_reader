from flask import Blueprint, render_template, request, flash,redirect,url_for,session
from scrapper import *
result = None
auth = Blueprint('auth' , __name__)

text =[]
links =[]
imgs =[]

@auth.route('/home')
def home():
    return render_template('home.html')

@auth.route('/search',  methods = ['GET','POST'])
def sumbit():
    if request.method == 'POST':
        user_input = str(request.form.get('search'))
        
        url = search_(user_input)
        text,links,imgs = get_search_result(url)
        if(len(text) >=1):
            return redirect(url_for('auth.results'))
        else:
            flash('NO RESULTS FOUND! TRY SEARCHING SOMETHING ELSE')


    return render_template('sumbit.html')

@auth.route('/results')
def results():
    
    return render_template("results.html", text = text , link = links , img = imgs, n = len(text))
   


