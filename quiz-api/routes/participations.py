from flask import Blueprint, request,jsonify
import sqlite3
from database.db import removeAllParticipations , saveParticipation, calculateScore
from model.models import Participation

participations  = Blueprint('participations ', __name__)

@participations.route('/participations', methods=['POST'])
def post_participations():
    data = request.get_json()
    player_name = data.get('playerName')  
    answer_positions = data.get('answers')

    if not player_name or not answer_positions:
        return jsonify({"error": "Missing data"}), 400

    score, answers_summaries = calculateScore(answer_positions)

    participation = Participation(player_name, answer_positions, score)
    saveParticipation(participation)

    return jsonify({
        "answersSummaries": answers_summaries,
        "playerName": player_name,
        "score": score
    }), 200

@participations.route('/participations/all', methods=['DELETE'])
def delete_all_participations():
    acces_token = request.headers.get('Authorization')

    if not acces_token:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        removeAllParticipations()
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    return ('', 204)