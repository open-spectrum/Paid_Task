from flask import  render_template, request, redirect, session, flash, url_for
from models.user_model import Users
from models.research_model import Research
from models.task_history_model import TaskHistoryResearch
from config import db
from models.payment_model import  Payment
from models.ads_model import Ads

class UserController:
   
    Users()
    @staticmethod
    def index():
        return render_template("index.html"),200
    
    @staticmethod
    def login():

        return render_template("user/login.html",method="GET"),200
    

    @staticmethod
    def auth():
        username_form = request.form.get("user")

        password_form = request.form.get("pass")

        user = Users.query.filter_by(username=username_form).first()
        if not user:
             flash("Senha Ou Nome De Usuario Incorreto")
             return redirect(url_for("login"),code=302)
        
        if user.username == username_form and user.password == password_form:
            session["username"] = user.username
            session["id"] = user.id
            session["roleId"] = user.roleId
            flash("Login Realizado Com Sucesso!")
            if session.get("roleId") == 1:
                 return redirect(url_for("admin"),code=302)
            else:
                 return redirect(url_for("home"),302)
        else:
            flash("Senha Ou Nome De Usuario Incorreto")
            return redirect(url_for("login"),code=302)
        
    @staticmethod
    def home():
        username = session.get("username")
        # Saldo do usuário
        sald = Users.query.filter_by(id=session['id']).first()

        return render_template("user/home.html", username=username, sald=sald.sald), 200

    

    @staticmethod
    def logout():

        flash(f"Logout Realizado Com Sucesso Volte Sempre.")
        session["id"] = None
        session["username"] = None
        session["roleID"] = None

        return redirect("/login"),302
    @staticmethod
    def history():
        return  
    @staticmethod
    def profile():
        user = Users.query.get(session.get("id"))
       
        return render_template("user/profile.html",username=user.username,pix_key=user.pix_key)
    
    @staticmethod 
    def edit_profile():
        id = session.get("id") 
        user = Users.query.get(id)
        if request.form.get("username") :   user.username =  request.form.get("username")
        if request.form.get("pix_key"): user.pix_key =  request.form.get("pix_key")
        db.session.commit()
        flash("Sucesso!")
        return redirect(url_for("profile"),code=302)

       
    @staticmethod
    def withdraw():
        pix = Users.query.get(session.get("id")).pix_key
        sald =  Users.query.get(session.get("id")).sald
        payments = Payment.query.filter_by(id_user=session.get("id")).all()
        payments.reverse()
        return render_template("user/withdraw.html",pix_key=pix,sald=sald,payments=payments)

    @staticmethod
    def payment():
        user_id = session.get("id")
        quantity = float(request.form.get("quantity"))
        pix_key = request.form.get("pix_key")

        if user_id and quantity and pix_key:

         
            user = Users.query.get(user_id)
            if quantity <= user.sald and quantity > 0:

                new_payment = Payment(id_user=user_id,quantity=quantity,pix_key=pix_key,status="pendente")

                user.sald -= quantity

                db.session.add(new_payment)
                db.session.commit()
                flash("Saqur Realizado Com Sucesso")
            else:
                flash("Saldo Insuficiente!")

        return redirect(url_for("withdraw"),code=302)
    
    @staticmethod
    def video():
          sald = Users.query.get(session.get('id')).sald
          return render_template("tasks/video/video.html",sald=sald),200
    @staticmethod
    def ads_view():
        sald = Users.query.get(session.get('id')).sald
        ads = Ads.query.all()
   
        return render_template("tasks/video/video_ads.html",sald=sald,ads=ads),200
    




