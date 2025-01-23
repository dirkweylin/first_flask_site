from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session 

views = Blueprint(__name__, "views")
views.secret_key = 'dirwin'


@views.route("/", methods = ["GET", "POST"])
def name_input():
    if request.method == "POST":
        session['first_name'] = request.form.get("fname")
        session['last_name'] = request.form.get("lname")
        return redirect(url_for("views.profile"))
    return render_template("index.html")

@views.route("/profile")
def profile():
    if 'first_name' in session and 'last_name' in session:
        return render_template("profile.html", first_name=session['first_name'], last_name=session['last_name'])
    else:
        return redirect(url_for("views.name_input"))

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.name_input"))

views.route('/clear-session', methods=['POST'])
def clear_session():
    session.clear()
    return 'Session cleared'