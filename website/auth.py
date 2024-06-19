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
        user_input = user_input.replace(" ", "_")
        url = search_(user_input)
        text,links,imgs = get_search_result(url)
      
        if(len(text) >=1):
            return redirect(url_for('auth.results' , texts = text ,img = imgs , link = links , n = len(text)))
        else:
            flash('NO RESULTS FOUND! TRY SEARCHING SOMETHING ELSE')


    return render_template('sumbit.html')

@auth.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        clicked_btn = list(request.form.keys())[0]
        clicked_btn = str(clicked_btn[:-1])
        lst,title = get_chapters(clicked_btn)
        lst = lst[::-1]
        title = title[::-1]
        return redirect(url_for('auth.chapters', chap = lst,title = title ,n = len(lst)))

    
   
    return render_template("results.html", text = request.args.getlist('texts') , img = request.args.getlist('img') , link = request.args.getlist('link'), n = int(request.args.get('n')))
   

@auth.route('/chapters', methods=['GET', 'POST'])
def chapters():
    if request.method == 'POST':
        url_manga = list(request.form.keys())[0]
        manga = get_images(url_manga)
        #encode here to reduce size of url
        
        return redirect(url_for('auth.read_manga', images = manga, n = len(manga), url = url_manga))
    

    return render_template("chapters.html", link = request.args.getlist('chap'),title= request.args.getlist('title'), n = int(request.args.get('n')))

@auth.route('/readmanga')
def read_manga():
    url = request.args.get('url')
  
    return render_template("read.html", img = request.args.getlist('images'), n = int(request.args.get('n')), url = request.args.get('url'))