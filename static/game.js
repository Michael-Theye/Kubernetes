// Fetch initial data
function startGame() {
    fetch('/init', {
        method: 'POST',
        body: JSON.stringify({ name: "Player1" }),
        headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
    .then(data => {
        console.log("Game Initialized:", data);
    });
}

// Quest system
function startQuest(questId) {
    fetch('/quest/start', {
        method: 'POST',
        body: JSON.stringify({ quest_id: questId, player_id: "player1" }),
        headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
    .then(data => {
        console.log("Quest Started:", data);
    });
}

// Battle system (common enemies)
function attackEnemy() {
    fetch('/battle/attack', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
    .then(data => {
        document.getElementById("battle-log").innerText = `You attacked for ${data.damage} damage. Enemy HP: ${data.enemy_hp}`;
    });
}

startGame();
