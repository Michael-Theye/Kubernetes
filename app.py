from flask import Flask, jsonify, request
from models.player import Player
from models.quest import Quest
from models.merchant import Merchant

app = Flask(__name__)

# Game Initialization
@app.route('/init', methods=['POST'])
def initialize_game():
    player = Player(name=request.json['name'])
    return jsonify(player.to_dict())

# Quest system
@app.route('/quest/start', methods=['POST'])
def start_quest():
    quest = Quest.start_quest(request.json['quest_id'], request.json['player_id'])
    return jsonify(quest.to_dict())

# Merchant system
@app.route('/merchant/buy', methods=['POST'])
def buy_item():
    merchant = Merchant()
    result = merchant.buy_item(request.json['item_id'], request.json['player_id'])
    return jsonify(result)

# Battle system (common enemies & bosses)
@app.route('/battle/attack', methods=['POST'])
def attack_enemy():
    # Player attacking an enemy logic
    return jsonify({"status": "success", "damage": 20, "enemy_hp": 50})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
