from flask import Flask, request

app = Flask(__name__)

# Get default endpoint
@app.get("/")
def get():
    return "Welcome to Cricket API"

# Get list of teams
@app.get("/teams")
def get_teams():
    return {"teams": teams}

# Get a team
@app.get("/team")
def get_team():
    name = request.args.get('name', default="India")
    for team in teams:
        if team["name"].lower() == name.lower():
            return team,200
    return "Team not found", 404

# Create new team
@app.post("/team")
def create_team():
    request_data = request.get_json()
    print(request_data)
    new_team = {"name": request_data["name"], "nickname": request_data["nickname"], "players": request_data["players"]}
    teams.append(new_team)
    return new_team, 201

teams = [
    {
      "name": "India",
      "nickname": "Men in Blue",
      "players": [
        { "name": "Virat Kohli", "role": "Batsman" },
        { "name": "Rohit Sharma", "role": "Batsman" },
        { "name": "Jasprit Bumrah", "role": "Bowler" }
      ]
    },
    {
      "name": "Australia",
      "nickname": "Baggy Greens",
      "players": [
        { "name": "Steve Smith", "role": "Batsman" },
        { "name": "Pat Cummins", "role": "Bowler" },
        { "name": "David Warner", "role": "Batsman" }
      ]
    },
    {
      "name": "England",
      "nickname": "The Three Lions",
      "players": [
        { "name": "Joe Root", "role": "Batsman" },
        { "name": "Ben Stokes", "role": "All-rounder" },
        { "name": "Jofra Archer", "role": "Bowler" }
      ]
    },
    {
      "name": "Pakistan",
      "nickname": "Shaheens",
      "players": [
        { "name": "Babar Azam", "role": "Batsman" },
        { "name": "Shaheen Afridi", "role": "Bowler" },
        { "name": "Shadab Khan", "role": "All-rounder" }
      ]
    },
    {
      "name": "Sri Lanka",
      "nickname": "Lions",
      "players": [
        { "name": "Dimuth Karunaratne", "role": "Batsman" },
        { "name": "Wanindu Hasaranga", "role": "All-rounder" },
        { "name": "Dushmantha Chameera", "role": "Bowler" }
      ]
    },
    {
      "name": "West Indies",
      "nickname": "Windies",
      "players": [
        { "name": "Jason Holder", "role": "All-rounder" },
        { "name": "Nicholas Pooran", "role": "Batsman" },
        { "name": "Alzarri Joseph", "role": "Bowler" }
      ]
    },
    {
      "name": "New Zealand",
      "nickname": "Black Caps",
      "players": [
        { "name": "Kane Williamson", "role": "Batsman" },
        { "name": "Trent Boult", "role": "Bowler" },
        { "name": "Devon Conway", "role": "Batsman" }
      ]
    }
  ]

