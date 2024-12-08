# python-cricket-api
This is a simple REST API that returns a list of top cricket teams. The data is stored in an in-memory dictionary and is not saved in any persistent datastore.

## Methods

| Method | Action | Sample endpoint |
|----------|----------|----------|
| GET   | Retrieve list of teams  | http://127.0.0.1:5000/teams   |
| GET   | Retrieves a team based on the provided name   | http://127.0.0.1:5000/team?name=Australia   |
| POST   | Create new team   | http://127.0.0.1:5000/team  |

### Sample payload to create a new team

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