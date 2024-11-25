from flask import Flask, render_template, request, jsonify, redirect
from model import db_connect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if(request.method == "POST"):
        username = request.form['username']
        email = request.form['email']

        con = db_connect.db_connect()
        cursor = con.cursor()
        cursor.execute(f""" 
                            INSERT INTO users(`username`, `email`)
                            VALUES('{username}', '{email}'); 
                        """)
        con.commit()
        con.close()
        cursor.close()

        return f"usrname: {username}, email = {email} create successfully"


@app.route('/list-users')
def list_users():
    con = db_connect.db_connect()
    cursor = con.cursor()

    cursor.execute("""SELECT * FROM `users`;""")
    users = cursor.fetchall()

    return render_template('list_user.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')

# update user
@app.route("/update/<_id>", methods = ["GET", "POST"])
def update(_id):
    if request.method == "GET":

        # return jsonify({"id": _id})
        con = db_connect.db_connect()
        cursor = con.cursor()

        cursor.execute("""
            SELECT * FROM `users` WHERE `id` = %s 
        """, _id)
        user = cursor.fetchone()
        # return jsonify(user)
        return render_template("update.html", user=user)
    
    username = request.form['username']
    email    = request.form['email']

    con = db_connect.db_connect()
    cursor = con.cursor()
    sql = f"""
        UPDATE `users` SET `username` = '{username}', `email` = '{email}' WHERE `id` = '{_id}';
    """
    cursor.execute(sql)
    con.commit()
    return redirect('/list-users')

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        id = request.form['remove-val']
        connection = db_connect.db_connect()
        cursor = connection.cursor()
        cursor.execute(f""" DELETE FROM `users` WHERE `id` =  '{id}'; """)
        connection.commit()
        return redirect("/list-users")

if __name__ == '__main__':
    app.run(debug=True)

