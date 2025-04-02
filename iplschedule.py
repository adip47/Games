import random
from itertools import combinations

def generate_ipl_schedule(teams, total_matches):
    """Generates a random IPL schedule given a list of teams and total matches."""
    schedule = []
    matchups = list(combinations(teams.keys(), 2)) * 2  # Home & Away fixtures
    random.shuffle(matchups)  # Shuffle the fixtures randomly
    
    points_table = {team: {"Played": 0, "Won": 0, "Lost": 0, "Points": 0} for team in teams.keys()}  # Initialize points table
    
    for i in range(min(total_matches, len(matchups))):
        home_team = matchups[i][0]
        away_team = matchups[i][1]
        winner = random.choice([home_team, away_team])  # Randomly choose a winner
        
        points_table[home_team]["Played"] += 1
        points_table[away_team]["Played"] += 1
        
        if winner == home_team:
            points_table[home_team]["Won"] += 1
            points_table[away_team]["Lost"] += 1
        else:
            points_table[away_team]["Won"] += 1
            points_table[home_team]["Lost"] += 1
        
        points_table[winner]["Points"] += 2  # Award 2 points for a win
        
        match = {
            "Match Number": i + 1,
            "Team 1": home_team,
            "Team 2": away_team,
            "Location": teams[home_team],  # Home team's city as location
            "Winner": winner  # Random winner
        }
        schedule.append(match)
    
    return schedule, points_table

def print_schedule(schedule):
    """Prints the IPL match schedule in a tabular format."""
    print("\nIPL Schedule:")
    print("{:<10} {:<25} {:<25} {:<20} {:<25}".format("Match No.", "Team 1", "Team 2", "Location", "Winner"))
    print("-" * 110)
    for match in schedule:
        print("{:<10} {:<25} {:<25} {:<20} {:<25}".format(match["Match Number"], match["Team 1"], match["Team 2"], match["Location"], match["Winner"]))

def print_points_table(points_table):
    """Prints the IPL points table sorted by points."""
    print("\nIPL Points Table:")
    sorted_teams = sorted(points_table.items(), key=lambda x: x[1]["Points"], reverse=True)
    print("{:<25} {:<10} {:<10} {:<10} {:<10}".format("Team", "Played", "Won", "Lost", "Points"))
    print("-" * 60)
    for team, stats in sorted_teams:
        print("{:<25} {:<10} {:<10} {:<10} {:<10}".format(team, stats["Played"], stats["Won"], stats["Lost"], stats["Points"]))

def determine_playoffs(points_table):
    """Determines the top 4 teams for playoffs and simulates playoffs."""
    sorted_teams = sorted(points_table.items(), key=lambda x: x[1]["Points"], reverse=True)
    top_4 = [team[0] for team in sorted_teams[:4]]
    
    print("\nIPL Playoffs:")
    qualifier_1_winner = random.choice([top_4[0], top_4[1]])
    eliminator_winner = random.choice([top_4[2], top_4[3]])
    qualifier_2_winner = random.choice([qualifier_1_winner, eliminator_winner])
    final_winner = random.choice([qualifier_1_winner, qualifier_2_winner])
    
    print(f"Qualifier 1: {top_4[0]} vs {top_4[1]} -> Winner: {qualifier_1_winner}")
    print(f"Eliminator: {top_4[2]} vs {top_4[3]} -> Winner: {eliminator_winner}")
    print(f"Qualifier 2: {qualifier_1_winner} vs {eliminator_winner} -> Winner: {qualifier_2_winner}")
    print(f"Final: {qualifier_1_winner} vs {qualifier_2_winner} -> IPL Winner: {final_winner}")

# Define teams with their home cities
teams = {
    "Mumbai Indians": "Mumbai",
    "Chennai Super Kings": "Chennai",
    "Royal Challengers Bangalore": "Bangalore",
    "Kolkata Knight Riders": "Kolkata",
    "Sunrisers Hyderabad": "Hyderabad",
    "Rajasthan Royals": "Jaipur",
    "Delhi Capitals": "Delhi",
    "Punjab Kings": "Mohali",
    "Lucknow Super Giants": "Lucknow",
    "Gujarat Titans": "Ahmedabad"
}

total_matches = 94

# Generate and print the schedule
ipl_schedule, points_table = generate_ipl_schedule(teams, total_matches)
print_schedule(ipl_schedule)
print_points_table(points_table)
determine_playoffs(points_table)