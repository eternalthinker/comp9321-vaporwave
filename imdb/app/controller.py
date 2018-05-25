from flask import jsonify
from flask_restful import reqparse

from app import app
from app.models import *


def seid(sid, eid):
    eid = eid if len(eid) == 2 else '0' + eid
    sid = sid if len(sid) == 2 else '0' + sid
    return sid + eid


@app.route('/season/<sid>/episode/<eid>', methods=['GET'])
def episode(sid, eid):
    e = Episode.query.filter(Episode.EID == seid(sid, eid))[0]
    if e:
        e = dict(e.__dict__)
        e.pop('_sa_instance_state')
        return jsonify(e), 200
    return "Episode Not Found", 404


@app.route('/character/<cid>', methods=['GET'])
def character(cid):
    c = Character.query.filter(Character.CID == cid)[0]
    if c:
        c = dict(c.__dict__)
        c.pop('_sa_instance_state')
        return jsonify(c), 200
    return "Character Not Found", 404


@app.route('/season/<sid>/episode/<eid>/characters', methods=['GET'])
def episode_characters(sid, eid):
    ceid = seid(sid, eid)
    cs = Character.query.outerjoin(EpisodeCharacters).filter(EpisodeCharacters.EID == ceid)

    if cs:
        ep_characters = []
        for c in cs:
            c = dict(c.__dict__)
            c.pop('_sa_instance_state')
            ep_characters.append(c)
        return jsonify(ep_characters), 200
    return "Complete and Catastrophic Failure"