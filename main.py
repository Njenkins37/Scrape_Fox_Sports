from bs4 import BeautifulSoup
import json
import requests


sec_strings = ['alabama-crimson-tide', 'arkansas-razorbacks', 'auburn-tigers', 'florida-gators', 'georgia-bulldogs',
               'kentucky-wildcats', 'lsu-tigers', 'mississippi-state-bulldogs', 'missouri-tigers', 'oklahoma-sooners',
               'ole-miss-rebels', 'south-carolina-gamecocks', 'tennessee-volunteers', 'texas-longhorns',
               'texas-am-aggies', 'vanderbilt-commodores']
sec_list = {
    'Alabama': '',
    'Arkansas': '',
    'Auburn': '',
    'Florida': '',
    'Georgia': '',
    'Kentucky': '',
    'LSU': '',
    'Mississippi State': '',
    'Missouri': '',
    'Oklahoma': '',
    'Ole Miss': '',
    'South Carolina': '',
    'Tennessee': '',
    'Texas': '',
    'Texas A&M': '',
    'Vanderbilt': ''

}

stat_list = ['Passing Yards', 'Passing Touchdowns', 'Rushing Yards', 'Rushing Touchdowns', 'Receiving Yards',
             'Receiving Touchdown', 'Kicking Points', 'Kick Return Yards', 'Punt Return Yards',
             'Defensive Interceptions', 'Defensive Tackles', 'Sacks', 'Points', 'All Purpose Yards',
             'Passing Yards/Game', 'Rushing Yards/Game', 'Team Kicking Points', 'Kick Return Avg', 'Punt Return Avg',
             'Team Sacks', 'Third Down Pct', 'Yards/Game', 'Turnover Plus/Minus']


for item in sec_strings:
    website = f'https://www.foxsports.com/college-football/{item}-team-stats'
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_yards = soup.find_all(name='div', class_='stat-leader-data')
    team_stats = [item.find(name='div', class_='fs-54 fs-sm-40').getText() for item in all_yards]

    stat_dictionary = {key: value for key, value in zip(stat_list, team_stats)}
    print(stat_dictionary)

    sec_list[f'{item}'] = stat_dictionary


json_string = json.dumps(sec_list)

with open(file='team_stats.txt', mode='a') as file:
    file.write(json_string)


