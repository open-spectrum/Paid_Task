from flask import  render_template, request, redirect, session, flash, url_for
from models.research_model import Research
from models.task_history_model import TaskHistoryResearch
from models.user_model import Users
class ResearchController:

    @staticmethod 
    def research():
          # Todas as tarefas
          tasks = Research.query.order_by(Research.id).all()
          user = Users.query.get(session.get("id"))
          # Tarefas que o usuário já fez (por id)
          history_ids = {h.id_research for h in TaskHistoryResearch.query.filter_by(id_user=session['id']).all()}

          # Tarefas que ele ainda não fez
          tasks_not_done = [task for task in tasks if task.id not in history_ids]
          return render_template("user/research.html",tasks=tasks_not_done,sald=user.sald)
    
    @staticmethod
    def task(id):
         research = Research.query.filter_by(id=id).first()
         return render_template("tasks/task.html",task=research),200
    @staticmethod
    def questions():
            id = request.args.get("id")

            r = request.args.get("r")

            research = Research.query.filter_by(id=id).first()

            return render_template("tasks/research/research.html", research=research,r=r), 200
    
   
