from flask import Flask, redirect, request, render_template, flash, url_for, session, jsonify, make_response
from dbconnect import connection
from flask_mail import Mail, Message
from random import randint
from smtplib import SMTP
from flask_mysqldb import MySQL
import os
from datetime import datetime
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'appussrh@gmail.com',
	MAIL_PASSWORD = 'wdpbxdfyoxfkpelk'
	)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = '2628'
app.config['MYSQL_DB'] = 'pes_students'

mysql = MySQL(app)


app.config['UPLOAD_FOLDER'] = 'static/blog_photos/'


mail = Mail(app)
app.secret_key = 'some_secret'
global res, av, country_name_new,cdelectricity, cdlpg, cdcng,cdpng, cdsmallcar, cdmediumcar, cdlargecar, cdbike, cdtaxi, cdtrain, cdauto, cdbus,cddomflight,cdintflight,cdwaste,maxfal


@app.route('/background_process_new')
def background_process_new():
    global res,av, country_name_new, cdelectricity, cdlpg, cdcng,cdpng, cdsmallcar, cdmediumcar, cdlargecar, cdbike, cdtaxi, cdtrain, cdauto, cdbus,cddomflight,cdintflight,cdwaste,maxfal
    country_name_new = str(request.args.get('country_name_new', 0))
    no_people_input_new = request.args.get('no_people_input_new', 1, type=int)
    electricity_input_new = request.args.get('electricity_input_new', 0, type=float)
    lpg_new = request.args.get('lpg_new', 0, type=float)
    cng_new = request.args.get('cng_new', 0, type=float)
    png_new = request.args.get('png_new', 0, type=float)
    smallcar_new = request.args.get('smallcar_new', 0, type=float)
    mediumcar_new = request.args.get('mediumcar_new', 0, type=float)
    largecar_new = request.args.get('largecar_new', 0, type=float)
    bike_new = request.args.get('bike_new', 0, type=float)
    taxi_new = request.args.get('taxi_new', 0, type=float)
    auto_new = request.args.get('auto_new', 0, type=float)
    train_new = request.args.get('train_new', 0, type=float)
    bus_new = request.args.get('bus_new', 0, type=float)
    domflight_new = request.args.get('domflight_new', 0, type=float)
    intflight_new = request.args.get('intflight_new', 0, type=float)
    waste_new = request.args.get('waste_new', 0, type=float)
    smallfuel = str(request.args.get('smallfuel', 0))
    mediumfuel = str(request.args.get('mediumfuel', 0))
    largefuel = str(request.args.get('largefuel', 0))
    # year month select
    yrmnthslct_electricity = str(request.args.get('yrmnthslct_electricity', 0))
    yrmnthslct_lpg = str(request.args.get('yrmnthslct_lpg', 0))
    yrmnthslct_cng = str(request.args.get('yrmnthslct_cng', 0))
    yrmnthslct_png = str(request.args.get('yrmnthslct_png', 0))
    yrmnthslct_smallcar = str(request.args.get('yrmnthslct_smallcar', 0))
    yrmnthslct_mediumcar = str(request.args.get('yrmnthslct_mediumcar', 0))
    yrmnthslct_largecar = str(request.args.get('yrmnthslct_largecar', 0))
    yrmnthslct_bike = str(request.args.get('yrmnthslct_bike', 0))
    yrmnthslct_taxi = str(request.args.get('yrmnthslct_taxi', 0))
    yrmnthslct_auto = str(request.args.get('yrmnthslct_auto', 0))
    yrmnthslct_train = str(request.args.get('yrmnthslct_train', 0))
    yrmnthslct_bus = str(request.args.get('yrmnthslct_bus', 0))
    yrmnthslct_dom = str(request.args.get('yrmnthslct_dom', 0))
    yrmnthslct_int = str(request.args.get('yrmnthslct_int', 0))
    yrmnthslct_waste = str(request.args.get('yrmnthslct_waste', 0))
    c, conn = connection()
    c.execute("select emission from cef where country_name ='%s'" % country_name_new)
    cef = c.fetchone()[0]

    #res = no_people_input_new + electricity_input_new + lpg_new# + cng_new + png_new + smallcar_new + mediumcar_new+ largecar_new + bike_new + taxi_new + auto_new + train_new + bus_new + domflight_new + intflight_new + waste_new
    if yrmnthslct_electricity == "month":
        cdelectricity = (electricity_input_new * cef * 12) / no_people_input_new
    elif yrmnthslct_electricity == "year":
        cdelectricity = (electricity_input_new * cef) / no_people_input_new
    if yrmnthslct_lpg == "month":
        cdlpg = (lpg_new * 2.9910628 * 12) / no_people_input_new
    elif yrmnthslct_lpg == "year":
        cdlpg = (lpg_new * 2.9910628) / no_people_input_new
    if yrmnthslct_cng == "month":
        cdcng = (cng_new * 1.8895296 * 12 * 1.25) / no_people_input_new
    elif yrmnthslct_cng == "year":
        cdcng = (cng_new * 1.8895296 * 1.25) / no_people_input_new
    if yrmnthslct_png == "month":
        cdpng = (png_new * 1.8895296 * 12 * 1.33) / no_people_input_new
    elif yrmnthslct_png == "year":
        cdpng = (png_new * 1.8895296 * 1.333) / no_people_input_new


    if smallfuel == "petrol" and yrmnthslct_smallcar == "month":
        cdsmallcar = smallcar_new * 0.16061 * 12
    elif smallfuel == "diesel" and yrmnthslct_smallcar == "month":
        cdsmallcar = smallcar_new * 0.14701 * 12
    elif smallfuel == "cng" and yrmnthslct_smallcar == "month":
        cdsmallcar = smallcar_new * 0.18672 * 12
    elif smallfuel == "petrol" and yrmnthslct_smallcar == "year":
        cdsmallcar = smallcar_new * 0.16061
    elif smallfuel == "diesel" and yrmnthslct_smallcar == "year":
        cdsmallcar = smallcar_new * 0.14701
    elif smallfuel == "cng" and yrmnthslct_smallcar == "year":
        cdsmallcar = smallcar_new * 0.18672
    else:
        cdsmallcar = 0


    if mediumfuel == "petrol" and yrmnthslct_mediumcar == "month":
        cdmediumcar = mediumcar_new * 0.20088 * 12
    elif mediumfuel == "diesel" and yrmnthslct_mediumcar == "month":
        cdmediumcar = mediumcar_new * 0.1772 * 12
    elif mediumfuel == "cng" and yrmnthslct_mediumcar == "month":
        cdmediumcar = mediumcar_new * 0.16484 * 12
    elif mediumfuel == "petrol" and yrmnthslct_mediumcar == "year":
        cdmediumcar = mediumcar_new * 0.20088
    elif mediumfuel == "diesel" and yrmnthslct_mediumcar == "year":
        cdmediumcar = mediumcar_new * 0.1772
    elif mediumfuel == "cng" and yrmnthslct_mediumcar == "year":
        cdmediumcar = mediumcar_new * 0.16484
    else:
        cdmediumcar = 0


    if largefuel == "petrol" and yrmnthslct_largecar == "month":
        cdlargecar = largecar_new * 0.29014 * 12
    elif largefuel == "diesel" and yrmnthslct_largecar == "month":
        cdlargecar = largecar_new * 0.23049 * 12
    elif largefuel == "cng" and yrmnthslct_largecar == "month":
        cdlargecar = largecar_new * 0.23748 * 12
    elif largefuel == "petrol" and yrmnthslct_largecar == "year":
        cdlargecar = largecar_new * 0.29014
    elif largefuel == "diesel" and yrmnthslct_largecar == "year":
        cdlargecar = largecar_new * 0.23049
    elif largefuel == "cng" and yrmnthslct_largecar == "year":
        cdlargecar = largecar_new * 0.23748
    else:
        cdlargecar = 0

    if yrmnthslct_bike == "month":
        cdbike = (bike_new * 0.11955 * 12)
    elif yrmnthslct_bike == "year":
        cdbike = (bike_new * 0.11955)

    if yrmnthslct_taxi == "month":
        cdtaxi = (taxi_new * 0.142915729 * 12)
    elif yrmnthslct_taxi == "year":
        cdtaxi = (taxi_new * 0.142915729)

    if yrmnthslct_auto == "month":
        cdauto = (auto_new * 0.2547 * 12)
    elif yrmnthslct_auto == "year":
        cdauto = (auto_new * 0.2547)

    if yrmnthslct_train == "month":
        cdtrain = (train_new * 0.101283756 * 12)
    elif yrmnthslct_train == "year":
        cdtrain = (train_new * 0.101283756)

    if yrmnthslct_bus == "month":
        cdbus = (bus_new * 0.066486883 * 12)
    elif yrmnthslct_bus == "year":
        cdbus = (bus_new * 0.066486883)

    if yrmnthslct_dom == "month":
        cddomflight = (domflight_new * 0.17147 * 12)
    elif yrmnthslct_dom == "year":
        cddomflight = (domflight_new * 0.17147)

    if yrmnthslct_int == "month":
        cdintflight = (intflight_new * 0.105095 * 12)
    elif yrmnthslct_int == "year":
        cdintflight = (intflight_new * 0.105095)

    if yrmnthslct_waste == "month":
        cdwaste = (waste_new * 0.2898355136 * 12) / no_people_input_new
    elif yrmnthslct_waste == "year":
        cdwaste = (waste_new * 0.2898355136) / no_people_input_new


    res = (cdelectricity + cdlpg + cdcng + cdpng + cdsmallcar + cdmediumcar + cdlargecar + cdbike + cdtaxi + cdtrain + cdauto + cdbus + cddomflight + cdintflight + cdwaste)*0.001
    c, conn = connection()
    c.execute("select average from cef where country_name='%s'"%country_name_new)
    d = c.fetchall()[0][0]
    av = (res/d)*100
	
    maxfal = max(cdelectricity *0.001, cdlpg*0.001, cdcng*0.001, cdpng*0.001, cdsmallcar*0.001, cdmediumcar*0.001, cdlargecar*0.001, cdbike*0.001, cdtaxi*0.001, cdtrain*0.001, cdauto*0.001, cdbus*0.001,cddomflight*0.001,cdintflight*0.001,cdwaste*0.001)

    resultjason = [res,cdelectricity *0.001, cdlpg*0.001, cdcng*0.001, cdpng*0.001, cdsmallcar*0.001, cdmediumcar*0.001, cdlargecar*0.001, cdbike*0.001, cdtaxi*0.001, cdtrain*0.001, cdauto*0.001, cdbus*0.001,cddomflight*0.001,cdintflight*0.001,cdwaste*0.001,maxfal, av, d]
    return jsonify(result=resultjason)

@app.route('/', methods=['GET','POST'])
def qhome1():
    if session.get('email'):
        global country_name_new,res
        c, conn = connection()
        c.execute("select country_name from cef")
        country_fetch = c.fetchall()
        country_list = []
        for i in country_fetch:
            country_list.append(i[0])
        #c.execute("select average from cef where country_name='%s'"%country_name_new)
        #d = c.fetchall()[0][0]
        data = {'country': country_list}
        # return render_template('home1.html', data=data)
        return render_template('home1.html', data=data)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if request.form.get('repassword') == request.form.get('password'):

            # fetch data from HTML form
            # set() - empty set
            global user_data
            user_data = {} #empty dictionary
            # user_data[new_key] = new_value # adding key value
            user_data['full_name'] = request.form.get('full_name')
            user_data['email'] = request.form.get('email')
            user_data['password'] = request.form.get('password')
            

            # generate OTP
            global c_otp
            c_otp = randint(100_000,999_999)
            message = f"Hello {user_data['full_name']}, your OTP is {c_otp}"


            # send OTP mail
            mail_obj = SMTP('smtp.gmail.com', 587)
            mail_obj.starttls()
            mail_obj.login('appussrh@gmail.com','wdpbxdfyoxfkpelk')
            mail_obj.sendmail('appussrh@gmail.com', user_data['email'], message)

            # render OTP page
            return render_template('otp.html')
        else:
            return render_template('otp.html', message="Both OTPs didn't match")


@app.route('/otp', methods=['POST', 'GET'])
def otp():
    if request.method == 'POST':
        if str(c_otp) == request.form.get('u_otp'):
            # create a row in our database
            cur = mysql.connection.cursor()
            sql_query = f"insert into student values ({c_otp},'{user_data['full_name']}', '{user_data['email']}', '{user_data['password']}');"
            cur.execute(sql_query) # SQL query
            cur.connection.commit()
            cur.close()
            return render_template('register.html', message='successfully created!!!')
        else:

            return render_template('otp.html', message='Invalid OTP')
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u_email = request.form.get('email')
        u_password = request.form.get('password')

        query = f"select full_name, email, password from student where email = '{u_email}'"
        cur = mysql.connection.cursor()
        cur.execute(query)
        one_record = cur.fetchone()
        if one_record:
            # yes that email EXISTS
            if one_record[2] == u_password:
                #start a session
                session['email'] = u_email

                return redirect(url_for('qhome1'))

                
            else:
                return render_template('login.html', message='incorrect password!!')
        else:
            # it does not exist
            return render_template('login.html', message='Invalid Email ID')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    del session['email']
    return render_template('login.html')

@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'GET':
        return render_template('add_blog.html')
    else:
        #upload a blog
        # CREATE TABLE blogs (blog_id int NOT NULL AUTO_INCREMENT, blog_title varchar(255), blog_des text(65535), blog_image varchar(255), blog_owner int, PRIMARY KEY(blog_id), FOREIGN KEY(blog_owner) REFERENCES students(id) );
        b_title = request.form.get('title')
        b_des = request.form.get('des')
        b_file_obj = request.files['blog_pic']
        b_filename = b_file_obj.filename
        #below line will save image file in the folder
        b_file_obj.save(os.path.join(app.config['UPLOAD_FOLDER'], b_filename))

        cur = mysql.connection.cursor()
        #fetch current time
        current_dt = str(datetime.now())

        #fetch current user ID(session user)
        session_user_email = session['email']
        cur.execute(f"select id from student where email = '{session_user_email}'")
        session_user_li = cur.fetchone()
        session_user_id = session_user_li[0]

        #saving info in the db/ creating a record in blogs
        sql_query = f"insert into blogs (blog_title, blog_des, blog_image, blog_owner, datetime ) values ('{b_title}','{b_des}', '{b_filename}', {session_user_id}, '{current_dt}');"
        cur.execute(sql_query) # SQL query
        cur.connection.commit()
        cur.close()

        return render_template('add_blog.html', message='Blog has been successfully added!!')


@app.route('/my_blogs')
def my_blogs():
    # exctract only session user's blogs
    session_user_email = session['email']
    cur = mysql.connection.cursor()
    sql_query = f"SELECT blogs.blog_title, blogs.blog_des, blogs.blog_image, student.full_name, blogs.datetime FROM blogs INNER JOIN student ON blogs.blog_owner=student.id WHERE student.email = '{session_user_email}';"
    cur.execute(sql_query)
    my_blogs = cur.fetchall()
    cur.close()
    return render_template('my_blogs.html', all_my_blogs = my_blogs)


@app.route('/contact')
def contact():
    if session.get('email'):
        return render_template('contact.html')
    else:
        return render_template('login.html')

@app.route('/about')
def about():
    if session.get('email'):
        return render_template('about.html')
    else:
        return render_template('login.html')


# @app.route('/status/',methods=['GET','POST'])
# def status():
#     if session.get('email'):
#         return render_template('status.html')
#     else:
#         return render_template('login.html')


# @app.route('/about', methods=['GET', 'POST'])
# def about():
#     if session.get('email'):
#         return render_template('about.html')
#     else:
#         return render_template('login.html')
    


@app.route('/pledge/',methods=['GET','POST'])
def pledge():
    global country_name_new,av, res,cdelectricity, cdlpg, cdcng,cdpng, cdsmallcar, cdmediumcar, cdlargecar, cdbike, cdtaxi, cdtrain, cdauto, cdbus,cddomflight,cdintflight,cdwaste,maxfal
    if request.method == 'POST':
        c, conn = connection()
        c.execute("select average from cef where country_name='%s'"%country_name_new)
        d = c.fetchall()[0][0]
        household = (cdelectricity + cdlpg + cdcng + cdpng)*0.001
        transport = (cdsmallcar + cdmediumcar + cdlargecar + cdbike + cdtaxi + cdtrain + cdauto + cdbus + cddomflight + cdintflight)*0.001
        waste = (cdwaste)*0.001
        per = (res / d)*100
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO per (value) VALUES (%s)", (res,))
        cur.connection.commit()
        cur.close()
        # c.execute("INSERT INTO per VALUES (%s)", (per,))
        writtn = [round(household,2), round(transport,2), round(waste,2),round(per,2)]
        maildata = [round(res,2), d]
        emailid = "appussrh@gmail.com"
        msg = Message("Your Carbon Footprint Results !!",
                      sender="appussrh@gmail.com",
                      recipients=[emailid])
        msg.html = render_template('mailtest.html', data=maildata)
        mail.send(msg)
        reslst=[d, cdelectricity *0.001, cdlpg*0.001, cdcng*0.001, cdpng*0.001, cdsmallcar*0.001, cdmediumcar*0.001, cdlargecar*0.001, cdbike*0.001, cdtaxi*0.001, cdtrain*0.001, cdauto*0.001, cdbus*0.001,cddomflight*0.001,cdintflight*0.001,cdwaste*0.001,maxfal, round(res,2),av]
        return render_template('pledge.html',result=reslst, writtendata=writtn)

    return redirect(url_for('qhome1'))


# @app.route('/status/', methods=['GET', 'POST'])
# def status():
#     global res, writtn, value

#     if request.method == 'GET':
#         # Fetch top two records from per table
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM per ;")
#         top_records = cur.fetchall()
#         cur.close()

#         # Extracting values from the fetched records
#         values = [record[0] for record in top_records]

       

#         return render_template('status.html', top_values=values)

#     return redirect(url_for('qhome1'))


@app.route('/status/', methods=['GET', 'POST'])
def status():
    global res, writtn, value

    if request.method == 'GET':
        # Fetch all records from per table
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM per ;")
        all_records = cur.fetchall()
        cur.close()

        # Extracting values from the fetched records
        values = [record[0] for record in all_records]

        # Calculate the maximum value
        max_value = max(values)

        # Plot the graph
        plt.plot(values)
        plt.xlabel('Record Index')
        plt.ylabel('Value')
        plt.title('Carbon Footprint Status')
        plt.savefig('static/graph.png')  # Save the plot as an image file

        return render_template('status.html', top_values=values, max_value=max_value)

    return redirect(url_for('qhome1'))


@app.route('/rec/', methods=['GET', 'POST'])
def rec():
    if request.method == 'GET':
        
     
        return render_template('rec.html')
    return redirect(url_for('pledge'))



if __name__ == "__main__":
   app.run(debug =True)