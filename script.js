// Function to fetch leaderboard data from the backend
function fetchLeaderboard() {
  fetch("http://127.0.0.1:5000/data", {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.json())
    .then(data => {
      generateLeaderboard(data);
    })
    .catch(error => {
      console.error("Error fetching leaderboard:", error);
    });
}

// Function to dynamically generate leaderboard scores
function generateLeaderboard(leaderboardData) {
  const scoresList = document.getElementById("scoresList");
  scoresList.innerHTML = ""; // Clear previous leaderboard scores

  for (const [name, score] of Object.entries(leaderboardData)) {
    const listItem = document.createElement("li");
    listItem.innerHTML = `<span>${name}</span><span>${score}</span>`;
    scoresList.appendChild(listItem);
  }
}

// Invoke the fetch leaderboard function on page load
window.addEventListener("DOMContentLoaded", fetchLeaderboard);
