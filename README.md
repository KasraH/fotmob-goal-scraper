# FotMob Goal Scraper

A Python script for extracting goal data from football matches using the FotMob API.

## Overview

This script fetches goal data from all matches in a specified league and season. It collects information such as goal scorers, time of goals, assists, and the teams involved, then exports the data to a CSV file for analysis.

## Features

- Retrieves match IDs for an entire league season
- Extracts detailed goal information including:
  - Goal scorer name
  - Time of goal
  - Assist information
  - Home/away team status
- Exports data to CSV format for easy analysis

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - pandas

## Installation

1. Clone this repository or download the script
2. Install required packages:
   ```
   pip install requests pandas
   ```

## Usage

1. Open the script and modify the `league_params` dictionary:

   ```python
   league_params = {
       'id': 47,  # Example: 47 for Premier League
       'season': '2023/2024'  # Format: 'YYYY/YYYY'
   }
   ```

2. Fill in the `x-mas` header value in the script:

   ```python
   headers = {
       'x-mas': ''  # Required header, replace with your own value
   }
   ```

3. Run the script:

   ```
   python main.py
   ```

4. The script will generate a CSV file named `goals_SEASON.csv` in the same directory.

## League IDs

Some common league IDs:

- 47: Premier League (England)
- 87: La Liga (Spain)
- 54: Bundesliga (Germany)
- 55: Serie A (Italy)
- 53: Ligue 1 (France)

## Output Format

The CSV file contains the following columns:

- `matchId`: Unique identifier for the match
- `team`: Team that scored the goal
- `player`: Name of the goal scorer
- `timeStr`: Time when the goal was scored
- `assistStr`: Information about the assist (if available)
- `isHome`: Boolean indicating if the scoring team was playing at home

## Notes

- The script requires a stable internet connection to make API requests
- Consider implementing rate limiting if making many requests
- This tool is for educational purposes only
