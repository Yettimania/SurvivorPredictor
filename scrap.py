'''
The scrap file will go the the following address on five thirty eight to pull the latest win probabilities.
It is broken down into weeks and subdivided further in to games within that week. Lastly you can take each game
and split the two teams. Within the 'tr' class. The teams name and probability exist.

Week Class: 'week'
Games Class: 'game-body'
Teams Class: 'tr'
Each week, game and team is stored in a list.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def scrap():

	row_list = ['Atlanta','Philadelphia','Buffalo','Baltimore','Cincinnati','Indianapolis',
		'Houston','New England','Jacksonville','N.Y. Giants','Pittsburgh','Cleveland',
		'San Francisco','Minnesota','Tampa Bay','New Orleans','Tennessee','Miami','Kansas City',
		'L.A. Chargers','Dallas','Carolina','Seattle','Denver','Washington','Arizona','Chicago',
		'Green Bay','N.Y. Jets','Detroit','L.A. Rams','Oakland']
	column_list = ['Week 1','Week 2', 'Week 3', 'Week 4', 'Week 5',
		'Week 6','Week 7', 'Week 8','Week 9','Week 10','Week 11', 'Week 12', 'Week 13',
		'Week 14','Week 15','Week 16','Week 17']

	df = pd.DataFrame(index=row_list,columns=column_list)

	page = requests.get("https://projects.fivethirtyeight.com/2018-nfl-predictions/games/")
	#page.status_code
	soup = BeautifulSoup(page.content, 'html.parser')

	season = soup.find_all('section',class_='week')

	for i in range(len(season)):
		week_header = season[i].find(class_='h3').get_text().strip()
		game = season[i].find_all('table',class_='game-body')
		
		for x in range(len(game)):
			split_team = game[x].find_all(class_='tr')

			team_1 = split_team[0]
			team_2 = split_team[1]

			name_1 = team_1.find(True,{'class':['td text team','td text team winner','td text team loser']}).get_text().strip()
			chance_1 = team_1.find(class_='td number chance').get_text()
			name_2 = team_2.find(True,{'class':['td text team','td text team winner','td text team loser']}).get_text().strip()
			chance_2 = team_2.find(class_='td number chance').get_text()

			df.at[name_1,week_header] = chance_1
			df.at[name_2,week_header] = chance_2
	
	df.fillna(value='0%',inplace=True)

	return(df)
	
if __name__ == "__main__":
	dataframe = scrap()
	print(dataframe)
