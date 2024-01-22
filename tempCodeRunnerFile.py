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

