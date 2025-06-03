
import config

from controllers.user_controller import UserController
from controllers.research_controller  import ResearchController 
from controllers.admin_controller import AdminController
from controllers.task_controller import TaskController
from middleware.auth import login_required,login_required_admin
app = config.app
db = config.db



@app.route("/",methods=["GET"])
def index():
    return UserController.index()

@app.route("/login",methods=["GET"])
def login():
    return UserController.login()


@app.route("/auth",methods=["POST"])
def auth():
    return UserController.auth()

@app.route("/home")
@login_required
def home():
    return UserController.home()


@app.route("/task/<int:id>")
@login_required
def task(id):
   return ResearchController.task(id)


@app.route("/question")
@login_required
def questions():
  return ResearchController.questions()

@app.route("/logout")
@login_required
def logout():
    return UserController.logout()


@app.route("/create_task",methods=["GET","POST"])
@login_required_admin
def create_task():
  
  return AdminController.create_task()

@app.route("/reward")
@login_required
def reward():
   return TaskController.reward()


@app.route("/profile")
@login_required
def profile():
   return UserController.profile()

@app.route("/edit_profile",methods=['POST'])
@login_required
def edit_profile():
    return UserController.edit_profile()


@app.route("/admin")
@login_required_admin
def admin():
   return AdminController.index_admin()

@app.route("/withdraw")
@login_required
def withdraw():
   return UserController.withdraw()


@app.route("/create_user",methods=['POST','GET'])
@login_required_admin
def create_user():
    return AdminController.create_user()

@app.route("/payment",methods=['POST'])
@login_required
def payment():
    return UserController.payment()

@app.route('/research')
@login_required
def research():
   return ResearchController.research()
@app.route("/pay")
@login_required_admin
def pay():
   return AdminController.pay()
 

@app.route("/pay_user")
@login_required_admin
def pay_user():
   return AdminController.pay_user()
 

@app.route("/pay_user_reject")
@login_required_admin
def pay_user_reject():
   return AdminController.reject_pay()
 

@app.route("/edit_user",methods=['POST','GET'])
@login_required_admin
def edit_user():
   return AdminController.edit_user()
  
@app.route("/video")
@login_required
def video():
   return UserController.video()
   
@app.route("/reward_video")
@login_required
def reward_video():
   return TaskController.reward_video()
   
@app.route("/ads_view")
@login_required
def ads_view():
   return UserController.ads_view()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)


