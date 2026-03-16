from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re 

app=Flask(__name__)

app.secret_key='komal'


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='mysql'
app.config['MYSQL_DB']='project'

mysql=MySQL(app)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/admin')
def admin():
	return render_template('adminindex.html')

@app.route('/index2.html')
def index2():
	return render_template('index2.html')

@app.route('/index3.html')
def index3():
	return render_template('index3.html')		

@app.route('/about.html')
def about():
	return render_template('about.html')
	
@app.route('/blog.html')
def blog():
	return render_template('blog.html')
		
@app.route('/blog-single.html')
def blogsingle():
	return render_template('blog-single.html')
	
@app.route('/cart.html')
def cart():
	return render_template('cart.html')

@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/shop.html')
def shop():
	return render_template('shop.html')

@app.route('/leafy.html')
def leafy():
	return render_template('leafy.html')

@app.route('/fruite.html')
def fruite():
	return render_template('fruite.html')

@app.route('/root.html')
def root():
	return render_template('root.html')

@app.route('/flower.html')
def flower():
	return render_template('flower.html')


@app.route('/product-single.html')
def productsingle():
	return render_template('product-single.html')

@app.route('/wishlist.html')
def wishlist():
	return render_template('wishlist.html')

@app.route('/checkout.html')
def checkout():
	return render_template('checkout.html')		

@app.route('/login.html',methods=['POST','GET'])
def login():
	msg =' '
	if request.method=='POST' and 'email' in request.form and 'password' in request.form :
		email = request.form['email']
		password=request.form['password']
		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

		cursor.execute('SELECT * FROM user WHERE email=%S  AND password=%s',(fname,lname,password,))
		user=cursor.fetchone()
		
		if user:
			session['loggedin']=True
			session['userid']=user['userid']
			session['fname']=user['fname']
			session['lname']=user['lname']
			session['email'] = user['email']
			msg='Logged sucessfully'
			return redirect(url_for('home'))
			
		else:
			msg='Enter Correct Email /Password '	

	return render_template('login.html',msg=msg)	

@app.route('/register.html', methods =['GET', 'POST'])
def register():
	if request.method=='POST' and 'fname' in request.form and 'lname' in request.form and 'email' in request.form  and 'password' in request.form :
		fname=request.form['fname']
		lname=request.form['lname']
		email = request.form['email']
		password=request.form['password']
		cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE email=%s ',(email,))
		account = cursor.fetchone()
		if account:
			msg='Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg='Invalid email address !'
		elif not fname or not lname or not password or not email:
			msg='Please fill out the form !'
		else:
			cursor.execute('INSERT INTO user VALUES (NULL,%s,%s,%s,%s)', (fname,lname,email, password, ))
			mysql.connection.commit()
			msg='You have successfully registered !'
			return redirect(url_for('login'))
	elif request.method == 'POST':
		msg= 'Please fill out the form !'
	return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))



@app.route('/data.html',methods=['POST','GET'])
def data():
	
		cursor=mysql.connection.cursor()
		cursor.execute('SELECT * FROM project.user ;')
		data = cursor.fetchall()
		cursor.close()
		return render_template('data.html',user=data)