from flask import jsonify

from app import app
from app.models import *


def seid(sid, eid):
    eid = eid if len(eid) == 2 else '0' + eid
    sid = sid if len(sid) == 2 else '0' + sid
    return sid + eid


@app.route('/character/<slug>', methods=['GET'])
def character(slug):

    c = Character.query.filter(Character.slug == slug)[0]
    if c:
        c = dict(c.__dict__)
        c.pop('_sa_instance_state')
        return jsonify(c), 200
    return "Character Not Found", 404


@app.route('/house/<slug>', methods=['GET'])
def house(slug):

    c = House.query.filter(House.slug == slug)[0]
    if c:
        c = dict(c.__dict__)
        c.pop('_sa_instance_state')
        return jsonify(c), 200
    return "House Not Found", 404