from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "localhost"
        user = "admin"
        password = "password"
        db = "iss"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def get_member(self, member_id):
        self.cur.execute("""
        SELECT * FROM members 
        INNER JOIN auth_tokens a ON members.id = a.member_id
        WHERE id = {}
        """.format(member_id))

        result = self.cur.fetchall()
        return result


@app.route('/open', methods=["POST"])
def post():
    auth_token = request.headers['x-auth-token']
    team_id = request.headers['team_id']
    member_id = request.headers['member_id']

    def db_query():
        db = Database()
        members_list = db.get_member(member_id)
        return members_list

    members = db_query()
    if db_query() is not None:
        final_member = []
        for member in members:
            if member.get('token') == auth_token:
                final_member = member
                break

        if (final_member['id'] is int(member_id)) and final_member['team_id'] is int(team_id):
            return jsonify({'status': 'opened'})
        else:
            return jsonify({'status': 'not opened'})
    else:
        return jsonify({'status': 'not opened'})


app.run(host='0.0.0.0', port=8090)
