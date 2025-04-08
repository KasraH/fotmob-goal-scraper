import requests
import pandas as pd

# API URL for league matches
league_url = 'https://www.fotmob.com/api/leagues'

# Replace with your desired league ID and season
league_params = {
    'id': None,  # League ID goes here, e.g., 47 for Premier League
    'season': ''  # Season format: '2023/2024'
}

# API URL for match details
match_url = 'https://www.fotmob.com/api/matchDetails'

# Headers for the request
headers = {
    'x-mas': ''  # Required header, replace with actual value
}


def main():
    if not league_params['id'] or not league_params['season']:
        print("Please provide a valid league ID and season in league_params.")
        return

    # Step 1: Fetch all match IDs
    response = requests.get(league_url, params=league_params, headers=headers)

    if response.status_code == 200:
        league_data = response.json()

        # Extract match IDs
        match_ids = []
        all_matches = league_data.get('matches', {}).get('allMatches', [])
        for match in all_matches:
            match_id = match.get('id')
            if match_id:
                match_ids.append(match_id)

        print(
            f"Found {len(match_ids)} matches for the {league_params['season']} season.")
        print(match_ids)

        # Initialize an empty list to store all goals
        all_goals = []

        # Step 2: Loop through each match ID and extract goal data
        for match_id in match_ids:
            print(f"Processing match ID: {match_id}")

            # Make the API request for match details
            match_params = {'matchId': match_id, 'showNewUefaBracket': 'true'}
            response = requests.get(
                match_url, params=match_params, headers=headers)

            if response.status_code == 200:
                match_data = response.json()

                # Extract general match information
                general = match_data.get('general', {})
                home_team = general.get('homeTeam', {}).get('name')
                away_team = general.get('awayTeam', {}).get('name')
                final_score = f"{general.get('homeTeam', {}).get('score')}-{general.get('awayTeam', {}).get('score')}"

                # Extract goal events
                events = match_data.get('header', {}).get('events')

                if events:
                    # Home team goals
                    for player, goal_list in events.get('homeTeamGoals', {}).items():
                        for goal in goal_list:
                            all_goals.append({
                                'matchId': match_id,
                                'team': home_team,
                                'player': goal.get('player', {}).get('name'),
                                'timeStr': goal.get('timeStr'),
                                'assistStr': goal.get('assistStr'),
                                'isHome': True
                            })

                    # Away team goals
                    for player, goal_list in events.get('awayTeamGoals', {}).items():
                        for goal in goal_list:
                            all_goals.append({
                                'matchId': match_id,
                                'team': away_team,
                                'player': goal.get('player', {}).get('name'),
                                'timeStr': goal.get('timeStr'),
                                'assistStr': goal.get('assistStr'),
                                'isHome': False
                            })
                else:
                    print(f"No events data found for match ID {match_id}.")

            else:
                print(
                    f"Failed to retrieve data for match ID {match_id}: {response.status_code}")

        # Step 3: Save all goals to a CSV file
        goals_df = pd.DataFrame(all_goals)
        goals_df.to_csv(
            f"goals_{league_params['season'].replace('/', '_')}.csv", index=False)
        print(
            f"\n Data saved to goals_{league_params['season'].replace('/', '_')}.csv.")

    else:
        print(f"Failed to retrieve league data: {response.status_code}")


if __name__ == "__main__":
    main()
