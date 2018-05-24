from flask import jsonify
from flask_restful import reqparse

from app.database import  init_db, db_session
from app.models import *

from app import app

@app.route('/episode', methods=['GET'])
def episode():
    parser = reqparse.RequestParser()
    parser.add_argument("EID", type=str)
    args = parser.parse_args()
    eid = args.get("EID")

    r = Episode.query.filter(Episode.EID == eid)[0]

    if r:
        record = dict(r.__dict__)
        record.pop('_sa_instance_state')
        return jsonify(record), 200

    return "Episode Not Found", 404
