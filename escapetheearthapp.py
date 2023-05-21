from flask import Flask, Request, request
import json


leaderboard = {
    "John": 500 ,
    "Alice": 400 ,
    "Bob": 300 ,
    "Emma": 200 ,
    "David": 100 
}

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    
    leaderboard_return = json.dumps(leaderboard)


    return leaderboard_return

@app.route('/data', methods=['POST'])
def post_data(): 
    global leaderboard   
    data = request.get_json()  # Access the data sent in the POST request
    data = json.loads(data)
    if (leaderboard[data['name']] < data['score']):
        leaderboard[data['name']] = data['score']
    leaderboard = dict(sorted(leaderboard.items(), key=lambda x: x[1], reverse=True))
    print(leaderboard)

    return 'Data received and processed successfully'

if __name__ == '__main__':
    app.run()
