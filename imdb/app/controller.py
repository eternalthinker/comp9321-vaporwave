from flask import jsonify
from flask_restful import reqparse

from app.database import  init_db, db_session
from app.models import *

from app import app

# init_db()


@app.route('/episode', methods=['GET'])
def episode():
    parser = reqparse.RequestParser()
    parser.add_argument("EID", type=str)
    args = parser.parse_args()
    eid = args.get("EID")

    for r in Episode.query.filter(Episode.EID == '0101'):

        print(r)

        if r:
            record = dict(r.__dict__)
            return record
            # return jsonify(dict(eps)), 200

    return "", 404
