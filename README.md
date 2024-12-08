# python-cricket-api
This is simple API that provides list of top Cricket Teams in the world

## Methods

### GET - Teams
This method returns list of teams.
http://127.0.0.1:5000/teams

### GET - Team
This method retrieves a team based on the provided name.
http://127.0.0.1:5000/team?name=Australia

### Post - Team
This method creates a new team
http://127.0.0.1:5000/team

{
    "name": "South Africa",
    "nickname": "Proteas",
    "players": [
      { "name": "Quinton de Kock", "role": "Batsman/Wicketkeeper" },
      { "name": "David Miller", "role": "Batsman" },
      { "name": "Aiden Markram", "role": "Batsman/All-rounder" },
      { "name": "Marco Jansen", "role": "Bowler/All-rounder" },
      { "name": "Heinrich Klaasen", "role": "Batsman/Wicketkeeper" }
    ]
}