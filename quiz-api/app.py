from flask import Flask, request,jsonify
from flask_cors import CORS
from utils.jwt_utils import build_token
import hashlib
from routes.questions import questions 
from routes.participations import participations 
from datetime import datetime
import sqlite3
from database.db import create_tables


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return "Application was launched."

@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    db_connection = sqlite3.connect('./quiz.db')
    cur = db_connection.cursor()

    cur.execute("SELECT COUNT(*) FROM question")
    quiz_size = cur.fetchone()[0]

    cur.execute("""
        SELECT p.player_name, p.score, pr.date 
        FROM participation p
        JOIN participationResult pr ON p.id = pr.participation_id
        ORDER BY p.score DESC, pr.date DESC
    """)
    participation_results = cur.fetchall()

    scores = [{
        "playerName": player_name,
        "score": score,
        "date": datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
    } for player_name, score, date in participation_results]

    db_connection.close()

    return jsonify({"size": quiz_size, "scores": scores}), 200

@app.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    access_token = request.headers.get('Authorization')

    if not access_token: 
        return jsonify({"error": "Unauthorized"}), 401

    try:
        create_tables('quiz.db')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return 'Ok', 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	tried_password_hash = hashlib.md5(tried_password).hexdigest()
	password = "94c0d1d9d64e6b31743ed1fbf685539c"
	if tried_password_hash == password : 
		token = build_token()
		return {'token': token}, 200
	else : 
		return 'Unauthorized', 401 
	
	
app.register_blueprint(questions)
app.register_blueprint(participations)

if __name__ == "__main__":
    app.run()