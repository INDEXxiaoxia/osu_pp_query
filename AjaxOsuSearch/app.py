from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import Osu_clean,Osu_paqu
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:234567@localhost:3306/OSUer'
#自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#为session设置key
app.config['SECRET_KEY'] = 'OnePageOfLifeInMyStory'
db=SQLAlchemy(app)
#创建Users类映射users表
class Users(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    uname=db.Column(db.String(30),nullable=False,unique=True)
    upwd=db.Column(db.String(10),nullable=False)
    osuid=db.Column(db.String(20))
    def __init__(self,uname,upwd,osuid):
        self.uname=uname
        self.upwd=upwd
        self.osuid=osuid
    def __repr__(self):
        return "<Users:%r>"%self.uname

db.create_all()
#初始页面
@app.route('/')
def hello_world():
    return 'Hello World!' \
           '<hr><a href="/registerO">进入注册</a>' \
           '<hr><a href="/loginO">进入登陆</a>'
#注册页面
@app.route('/registerO',methods=['GET','POST'])
def registerO():
    '''
    注册页面
    获取uname、upwd、osuid
    '''
    if request.method =="GET":
        return render_template('registerIt.html')
    else:
        #接收前端数据
        uname=request.form.get('uname')
        upwd=request.form.get('upwd')
        osuid=request.form.get('osuid')
        #用接收到的值创建对象
        user=Users(uname,upwd,osuid)
        #将对象插入数据库
        db.session.add(user)
        #登陆成功自动重定向到登陆
        return redirect('/loginO')
#登陆页面--------------------------------
@app.route('/loginO',methods=['GET','POST'])
def loginO():
    if request.method=="GET":
        return render_template('logIt.html')
    else:
        uname=request.form['uname']
        upwd=request.form['upwd']
        #查询从前端获取到uname的upwd
        user=db.session.query(Users).filter_by(uname=uname,upwd=upwd).first()
        if user:
            #先将信息存储进session
            session['id']=user.id
            session['uname']=user.uname
            #登陆成功后跳转到查询
            return redirect('/searchO')
        else:
            errMsg="输入信息有误"
            return render_template('logIt.html',errMsg=errMsg)

#进入查询界面
@app.route('/searchO',methods=['GET','POST'])
def searchO():
    '''
    直接跳转到查询界面
    :return:
    '''
    #从session中获取登陆信息
    if 'id' in session and 'uname' in session:
        user=Users.query.filter_by(id=session.get('id')).first()
    return render_template('searchIt.html',user=user)
#服务器返回查询结果
@app.route('/serverO')
def serverO():
    '''
    查询结果并返回成一个字典并插入表格
    :return:
    '''
    # userid=request.args.get('userid')
    # html=Osu_paqu.Get_OsuHtml(userid)
    # dict0=Osu_clean.Get_OSUlist(html)
    dict0 = Osu_clean.Get_OSUlist(Osu_paqu.Get_OsuHtml(request.args.get('userid')))
    if dict0:
        return render_template('table-data-clean.html',dict0=dict0)
    else:
        return "NULL"
if __name__ == '__main__':
    app.run(debug=True)
