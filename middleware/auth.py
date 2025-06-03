from functools import wraps
from flask import redirect, session, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      
       
        if not session.get("id"):

            return redirect(url_for('login'))
        
        return f(*args, **kwargs)
    return decorated_function


def login_required_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
       
        if session.get("roleId") != 1 or not session.get("id"):


            return redirect(url_for('home'),code=302)
        
        return f(*args, **kwargs)
    return decorated_function
