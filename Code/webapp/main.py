import os
import config as c
from flask import Flask,render_template,url_for,redirect,request,flash,session
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Upload, Search, SongInfo

app = Flask(__name__)
app.secret_key="surya"
app.config['UPLOAD_FOLDER'] = c.UPLOAD_FOLDER

engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
db = DBSession()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['GET','POST'])
def search():
    #handle search form submission
    if request.method == 'POST':
        # add search to db
        # search online for that item
        pass
    # display page directly
    return render_template('search.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in c.ALLOWED_EXTENSIONS

@app.route('/handleupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files.get('file')
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            session['uploadpath']=path 
            return redirect(url_for('index',filename=filename))
    return redirect('/') 
@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')
@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')
if __name__ == "__main__":
    app.run(debug=True)