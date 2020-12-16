from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = 'your secret key'
@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/purchase')
def purchase():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    purchase = db.execute(
        "select * from purchase_info"
    ).fetchall()
    db.commit()
    db.close()
    return render_template('purchase.html',purchase=purchase)

#main
@app.route('/')
def main_home():
    return render_template('main.html')

#유저들의 정보 삽입
@app.route('/edit')
def formpage():
    return render_template('form.html')

@app.route('/view', methods=['post'])
def view():
    userOrder = request.form['userOrder']
    userName = request.form['userName']
    userAge = request.form['userAge']
    userSSN = request.form['userSSN']
    userNum = request.form['userNum']
    userAddr = request.form['userAddr']
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    print(userOrder)
    db.execute(
        'insert into customer_info (c_name,c_age,c_SSN,c_Num,c_Addr) values (?,?,?,?,?)', (userName,userAge,userSSN,userNum,userAddr)
    )
    db.execute(
        'insert into purchase_info (p_SSN, p_name, p_num, p_addr) values (?,?,?,?)', (userOrder,userName,userNum,userAddr)
    )
    product=db.execute(
        "select name from phone_info where SSN == ?", (1,)
    ).fetchone()
    print(product)
    db.commit()
    db.close()
    return render_template('ViewData.html',product=product, userOrder=userOrder,userName=userName, userNum=userNum, userAddr=userAddr)

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

#clear 주문하여 이제 파는 상품을 삭제해줘야함.
@app.route('/clear', methods=['post'])
def clear():
    userOrder = request.form['userOrder']
    # userName = request.form['userName']
    # userNum= request.form['userNum']
    # userAddr= request.form['userAddr']
    # print(userOrder)
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    db.execute("DELETE from phone_info where SSN like ?", (f'%{userOrder}%',))
    db.commit()
    db.close()
    flash("주문이 완료되었습니다!")
    return render_template("main.html")
# 제조사별

#LG 최신순, 가격별
@app.route('/LG' ,methods=['get','post'])
def showLG():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    LG = db.execute(
        "select SSN, name, price, b_data from phone_info where manufacturer == 'LG'"
    ).fetchall()
    RECENT_LG = db.execute(
        "select * from phone_info where manufacturer='LG' order by b_data desc"
    ).fetchall()
    PRICE_LG = db.execute(
        "select * from phone_info where manufacturer='LG' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    db.close()
    select=request.form.get('degree')
    if (str(select))=='1':
        return render_template('RECENT_LG.html',RECENT_LG=RECENT_LG)
    elif (str(select))=='2':
        return render_template('PRICE_LG.html',PRICE_LG=PRICE_LG)
    else:
        return render_template('LG.html', LG=LG)

#LG 가격 높은순, 낮은순
@app.route('/LG_', methods=['get','post'])
def showPRICE1():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    PRICE_LG = db.execute(
        "select * from phone_info where manufacturer='LG' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    PRICE_LG_L = db.execute(
        "select * from phone_info where manufacturer='LG' order by cast(replace(price,',','')as deciaml)"
    ).fetchall()
    db.close()
    select2=request.form.get('degree2')
    if(str(select2))=='1':
        return render_template('PRICE_LG.html',PRICE_LG=PRICE_LG)
    elif(str(select2))=='2':
        return render_template('PRICE_LG_L.html',PRICE_LG_L=PRICE_LG_L)

#삼성 최신순, 가격별
@app.route('/SAMSUNG', methods=['get','post'])
def showSAMSUNG():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    SAMSUNG = db.execute(
        "select SSN, name, price, b_data from phone_info where manufacturer == '삼성'"
    ).fetchall()
    RECENT_SAMSUNG = db.execute(
        "select * from phone_info where manufacturer='삼성' order by b_data desc"
    ).fetchall()
    PRICE_SAMSUNG = db.execute(
        "select * from phone_info where manufacturer='삼성' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    db.close()
    select=request.form.get('degree')
    if (str(select))=='1':
        return render_template('RECENT_SAMSUNG.html',RECENT_SAMSUNG=RECENT_SAMSUNG)
    elif (str(select))=='2':
        return render_template('PRICE_SAMSUNG.html',PRICE_SAMSUNG=PRICE_SAMSUNG)
    else:
        return render_template('SAMSUNG.html', SAMSUNG= SAMSUNG)
    
#삼성 가격 높은순, 낮은순
@app.route('/SAMSUNG_' ,methods=['get','post'])
def showPRICE2():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    PRICE_SAMSUNG = db.execute(
        "select * from phone_info where manufacturer='삼성' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    PRICE_SAMSUNG_L = db.execute(
        "select * from phone_info where manufacturer='삼성' order by cast(replace(price,',','')as deciaml)"
    ).fetchall()
    db.close()
    select2=request.form.get('degree2')
    if(str(select2))=='1':
        return render_template('PRICE_SAMSUNG.html',PRICE_SAMSUNG=PRICE_SAMSUNG)
    elif(str(select2))=='2':
        return render_template('PRICE_SAMSUNG_L.html',PRICE_SAMSUNG_L=PRICE_SAMSUNG_L)

#애플 최신순, 가격별
@app.route('/APPLE', methods=['get','post'])
def showAPPLE():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    APPLE = db.execute(
        "select SSN, name, price, b_data from phone_info where manufacturer == '애플'"
    ).fetchall()
    RECENT_APPLE = db.execute(
        "select * from phone_info where manufacturer='애플' order by b_data desc"
    ).fetchall()
    PRICE_APPLE = db.execute(
        "select * from phone_info where manufacturer='애플' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    db.close()
    select=request.form.get('degree')
   
    if (str(select))=='1':
        return render_template('RECENT_APPLE.html',RECENT_APPLE=RECENT_APPLE)
    elif (str(select))=='2':
        return render_template('PRICE_APPLE.html',PRICE_APPLE=PRICE_APPLE) 
    else:
        return render_template('APPLE.html', APPLE= APPLE)

#애플 가격 높은순, 낮은순
@app.route('/APPLE_', methods=['get','post'])
def showPRICE6():
    db = sqlite3.connect("phone_info.db")
    db.row_factory = sqlite3.Row
    PRICE_APPLE_L = db.execute(
        "select * from phone_info where manufacturer='애플' order by cast(replace(price,',','')as deciaml)"
    ).fetchall()
    PRICE_APPLE = db.execute(
        "select * from phone_info where manufacturer='애플' order by cast(replace(price,',','')as deciaml)desc"
    ).fetchall()
    db.close()
    select2=request.form.get('degree2')
    if(str(select2))=='1':
        return render_template('PRICE_APPLE.html',PRICE_APPLE=PRICE_APPLE)
    elif(str(select2))=='2':
        return render_template('PRICE_APPLE_L.html',PRICE_APPLE_L=PRICE_APPLE_L)
        
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
