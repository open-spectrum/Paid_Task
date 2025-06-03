from flask import  render_template, request, redirect, session, flash, url_for
from models.user_model import Users
from models.research_model import Research
from config import db
from models.payment_model import Payment
import json
class AdminController:
    @staticmethod 
    def index_admin():

        users = Users.query.all()
        return render_template("admin/index.html",users=users),200
    
    @staticmethod
    def create_task():
        #Verifica se a requisição é get
        if request.method == "GET":
            return render_template("admin/create_task.html"),200
        else:
            #Cadastra a Tarefa
            name = request.form["task_name"]
            pricing = request.form["task_pricing"]
            description = request.form["task_description"]
            questions = request.form["task_question"]
            img = request.form["img"]

           
           
            questions = json.loads(questions)


            new_task = Research(task_name = name, description = description,task_pricing = pricing,questions = questions,img=img)

            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("home"),code=302)
    @staticmethod
    def create_user():
        if request.method == "POST":
            username =  request.form.get("username")
            password = request.form.get("password")
            sald = request.form.get("sald")

            if username and password and sald:
                new_user = Users(username=username,password=password,sald=sald,roleId=0)
                db.session.add(new_user)
                db.session.commit()
                flash("Sucesso Ao criar usuario")
        else:
            return render_template("admin/create_user.html")

        return redirect(url_for("admin"),code=302)
    
    @staticmethod
    def pay():
        payments = Payment.query.all()

        not_pay = []

        for pay in payments:
            if pay.status == "pendente":
                not_pay.append(pay)

        payments.reverse()

        return render_template("admin/payment.html",list_pay=not_pay)
    
    @staticmethod
    def pay_user():
        id_payment = request.args.get("id")
        payment = Payment.query.get(id_payment)

        payment.status = "pago"

        db.session.commit()

        flash(f"Status De {id_payment} Atualizado Para Pago")

        return redirect(url_for("pay"),code=302)

    @staticmethod
    def reject_pay():
        id_payment = request.args.get("id")
        
        payment = Payment.query.get(id_payment)
        id_user = payment.id_user

        user = Users.query.get(id_user)

        user.sald += payment.quantity

        payment.status = "rejeitado"
        
        db.session.commit()

        flash(f"Status De {id_payment} Atualizado Para Rejeitado")


     
        return redirect(url_for("pay"),code=302)
    @staticmethod
    def edit_user():
        id_user = request.args.get("id")
        if request.method == "GET":
            user = Users.query.get(id_user)
            return render_template("admin/edit_user.html",user=user)
        else:
           id_user =   request.form.get("id")
           user = Users.query.get(id_user)
           username =  request.form.get("username")
           password =  request.form.get("password")
           sald =   request.form.get("sald")

           user.username = username
           user.password = password
           user.sald = sald

           db.session.commit()
           flash("Usuario Atualizado!")
           return redirect(url_for("admin"),code=302)
