# importing required librarues and modules
from flask import Flask
import watchdog

# importing required modules
import helpers.db_manage


import models.auth as user
import models.db_model






app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/register", methods=["GET"])
def register():
    return user.register
    

@app.route("/login", methods=["GET"])
def login():
    return user.login


@app.route("/logout", methods=["GET"])
def logout():
    return user.logout

if __name__ == "__main__":
    app.run()