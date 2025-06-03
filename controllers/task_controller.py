from flask import  render_template, request, redirect, session, flash, url_for
from models.user_model import Users
from models.research_model import Research
from models.task_history_model import TaskHistoryResearch
from config import db
class TaskController:
     @staticmethod
     def reward():
          user = Users.query.get(session['id'])

          research_id = request.args.get("id")
          task = Research.query.filter_by(id=research_id).first()

          if not task:
               flash("Tarefa não encontrada.")
               return redirect(url_for("home"), code=302)

          # Verifica se o usuário já fez essa tarefa
          task_done = TaskHistoryResearch.query.filter_by(
               id_user=user.id,
               id_research=task.id
          ).first()

          if task_done:
               flash("[Erro X] Você já concluiu essa tarefa.")
               return redirect(url_for("home"), code=302)

          # Atualiza saldo e histórico
          user.sald += task.task_pricing
          new_task_history = TaskHistoryResearch(id_user=user.id, id_research=task.id)

          db.session.add(new_task_history)
          db.session.commit()  # commit salva o saldo + histórico

          flash("Parabéns! Recompensa creditada.")
          return redirect(url_for("home"), code=302)

     
     @staticmethod
     def reward_video():
          user = Users.query.get(session['id'])
          user.sald += 0.01
          db.session.commit() 
          flash("Recompesa De R$ 0.01 Creditada!")
          return redirect(url_for("ads_view"), code=302)