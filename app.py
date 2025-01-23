from flask import Flask, session
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dirwin'
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

app.route('/clear-session', methods=['POST'])
def clear_session():
    session.clear()
    return 'Session cleared'