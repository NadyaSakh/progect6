"""

Представить информацию о ТОП-5 популярных чемпионатах.
По каждому чемпионату вывести первые 5 команд
с наибольшим числом забитых голов.

"""

import urllib.request
import json


def sort_by_team(i):
    return i['numberOfTeams']


def sort_by_goals(i):
    return i['goals']


ids =[]
match_names = []
newurls = []
i = 0

url = "http://api.football-data.org/v1/competitions/"
response = urllib.request.urlopen(url)
competitions = json.loads(response.read().decode())
competitions.sort(key=sort_by_team)
competitions1 = competitions[-5:]
for competition in competitions1:
    ids.append(competition['id'])
    match_names.append(competition['caption'])

#вывод соревнований
print("TOP-5 matches:")
for match_name in match_names:
    print(match_name)

#вывод команд
for id in ids:
    newurl = url +str(id)+'/'+'leagueTable'
    if id == 458:
        print("No league table for it competition yet.")
    elif id == 464:
        new_response = urllib.request.urlopen(newurl)
        league_table = json.loads(new_response.read().decode())
        teams = league_table['standings']['A']
        teams.sort(key=sort_by_goals)
        teams1 = teams[-5:]
        print("The first 5 teams with max number of goals "
              "at championship: ", match_names[i])
        for team in teams1:
            print(team['team'])
    else:
        new_response = urllib.request.urlopen(newurl)
        league_table = json.loads(new_response.read().decode())
        teams = league_table['standing']
        teams.sort(key=sort_by_goals)
        teams1 = teams[-5:]
        print("The first 5 teams with max number of goals "
              "at championship:", match_names[i])
        for team in teams1:
            print(team['teamName'])
    i += 1


