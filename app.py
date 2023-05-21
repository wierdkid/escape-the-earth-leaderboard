from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
db = SQLAlchemy(app)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Integer)

    def __repr__(self):
        return f"<Leaderboard(name='{self.name}', score={self.score})>"

@app.route('/data', methods=['GET'])
def get_data():
    leaderboard = Leaderboard.query.all()
    leaderboard_data = {entry.name: entry.score for entry in leaderboard}
    leaderboard_return = json.dumps(leaderboard_data)
    return leaderboard_return

@app.route('/data', methods=['POST'])
def post_data(): 
    data = request.get_json()
    name = data['name']
    score = data['score']
    new_entry = Leaderboard(name=name, score=score)
    db.session.add(new_entry)
    db.session.commit()
    return 'Data received and processed successfully'

if __name__ == '__main__':
    app.run()