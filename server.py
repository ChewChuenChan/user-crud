from flask import Flask,render_template,request,redirect

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read_all():
    return render_template("readall.html",user_list = User.get_all())

@app.route('/users/<int:id>')
def read_one(id):
    data ={
            'id': id
        }
    return render_template("readone.html",user=User.get_one(data))

@app.route('/users/<int:id>/edit')
def edit(id):
    data ={
            'id': id
        }

    return render_template("edit.html",user=User.get_one(data))

@app.route('/update/<int:id>',methods=["POST"])
def updated_user(id):
    print("+++++++++++++++++",request.form)
    data = {
        "id":id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.update(data)
    return redirect(f"/users/{id}")

@app.route('/new')
def new_user():
    return render_template ("create.html")

@app.route('/create',methods=["POST"])
def create():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    id=User.save(data)
    return redirect(f"/users/{id}")

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)