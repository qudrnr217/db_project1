from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

#main
@app.route('/')
def main_home():
    return render_template('main.html')

#회원가입
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

#회원가입 정보들
@app.route('/join',methods=['post'])
def join():
    s_name= request.form['s_name']
    s_id = request.form['s_id']
    s_pw = request.form['s_pw']
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    db.execute(
        'insert into sign_info (si_name, si_id, si_pwd) values (?,?,?)', (s_name, s_id, s_pw)
    )
    db.commit()
    db.close()
    return render_template("sign_up_alert.html")

#유저들의 정보 삽입
@app.route('/edit')
def formpage():
    return render_template('form.html')

@app.route('/view', methods=['post'])
def view():
    userName = request.form['userName']
    userAge = request.form['userAge']
    userSex = request.form['userSex']
    userSSN = request.form['userSSN']
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    db.execute(
        'insert into customer_info (c_name,c_age,c_sex,c_SSN) values (?,?,?,?)', (userName,userAge,userSex,userSSN)
    )
    db.commit()
    db.close()
    return render_template('ViewData.html',userName=userName,userAge=userAge,userSex=userSex,userSSN=userSSN)

# 검색
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/result', methods=['post'])
def result():
    _value = request.form['search_name']
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    result = db.execute(
        "select * from phone_info where name like ?", (f'%{_value}%',)
    ).fetchall()
    db.commit()
    db.close()
    return render_template('result_search.html', result=result)



# 제조사별
@app.route('/LG')
def showLG():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    LG = db.execute(
        "select name, price, b_data from phone_info where manufacturer == 'LG'"
    ).fetchall()
    db.close()
    return render_template('LG.html', LG= LG)

@app.route('/SAMSUNG')
def showSAMSUNG():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    SAMSUNG = db.execute(
        "select name, price, b_data from phone_info where manufacturer == '삼성'"
    ).fetchall()
    db.close()
    return render_template('SAMSUNG.html', SAMSUNG= SAMSUNG)

@app.route('/APPLE')
def showAPPLE():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    APPLE = db.execute(
        "select name, price, b_data from phone_info where manufacturer == '애플'"
    ).fetchall()
    db.close()
    return render_template('APPLE.html', APPLE= APPLE)

# 최신순
@app.route('/RECENT')
def showRecent():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    RECENT = db.execute(
        "select * from phone_info order by b_data desc"
    ).fetchall()
    db.close()
    return render_template('ALL.html', RECENT= RECENT)


#가격별
@app.route('/PRICE')
def showPRICE():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    PRICE = db.execute(
        "select * from phone_info order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    db.close()
    return render_template('PRICE.html', PRICE= PRICE)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
