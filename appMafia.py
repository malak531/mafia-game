from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

roles = ["Mafia", "Detective", "Civilian"]
players = []

@app.route('/')
def index():
    return render_template('index.html', players=players, roles=roles)

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    if player_name:
        players.append({"name": player_name, "role": None, "alive": True})
    return redirect(url_for('index'))
    

@app.route('/assign_roles')
def assign_roles():
    random.shuffle(players)
    num =int(len(players)/3)
    if (num-1 <= 0):
        healNum = 1
    else:
        healNum=num-1
    rolesPlayers = []
    rolesPlayers.append('Detective')
    for i in range (num):
        rolesPlayers.append('Mafia')
    for i in range (healNum):
        rolesPlayers.append('Healer')
    for i in range(len(players)-num-num):
        rolesPlayers.append('Citizen')
    random.shuffle(rolesPlayers)
    for i, player in enumerate(players):
        player["role"] = rolesPlayers[i]
    return render_template('assign_roles.html', players=players, roles=rolesPlayers)

@app.route('/kill/<player_name>')
def kill(player_name):
    for player in players:
        if player["name"] == player_name:
            player["alive"] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
