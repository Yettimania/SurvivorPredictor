import pandas as pd
import numpy as np

current_week = 11

def sort_select(DataFrame):

	ts = pd.DataFrame(index=DataFrame.columns,columns=['Team','Chance'])
	ts.fillna(value='0',inplace=True)

	for q in range(len(DataFrame.index)):
		for k in range(len(DataFrame.columns)):
			if (DataFrame.loc[DataFrame.index[q]] == DataFrame.loc[DataFrame.index[q]].max())[k] == True:
				if ((DataFrame.loc[DataFrame.index[q]].max() > ts.loc[DataFrame.columns[k],'Chance'])):
					ts.at[DataFrame.columns[k],'Team'] = DataFrame.index[q]
					ts.at[DataFrame.columns[k],'Chance'] = DataFrame.loc[DataFrame.index[q]].max()
		
	print(ts)


	remove_list = ts['Team'].tolist()
	remove_list = [x for x in remove_list if x != '0']
	
	dd = DataFrame.drop(remove_list)
	print(dd)

	#Weeks that have '0'
	for p in range(len(ts.index)):
		if (ts['Chance'][p] == '0'):


			y = dd[ts.index[p]] == dd[ts.index[p]].max()
	
				#Returns the team with the max predicted chance for the week.
			for z in range(len(y)):
				if y[z] == True:
					team_max = dd.index[z]
	
			ts.at[ts.index[p],'Team'] = team_max
			ts.at[ts.index[p],'Chance'] = dd[ts.index[p]].max()

	#Teams less than 50%
	for p in range(len(ts.index)):
		if (int(ts['Chance'][p].strip('%')) < 50):
			y = dd[ts.index[p]] == dd[ts.index[p]].max()
			for z in range(len(y)):
				if y[z] == True:
					team_max = dd.index[z]
	
			ts.at[ts.index[p],'Team'] = team_max
			ts.at[ts.index[p],'Chance'] = dd[ts.index[p]].max()

	print()
	print(ts)

def team_chance(DataFrame,week):

	ts = pd.DataFrame(index=DataFrame.index,columns=['Best','Better','Good'])

	for q in range(len(DataFrame.index)):
		team_best = DataFrame.loc[DataFrame.index[q]].sort_values(ascending=False).head(3)

		ts.at[DataFrame.index[q],'Best'] = int(team_best.index[0].split()[1])
		ts.at[DataFrame.index[q],'Better'] = int(team_best.index[1].split()[1])
		ts.at[DataFrame.index[q],'Good'] = int(team_best.index[2].split()[1])

	with open('used.txt','r') as u:
		x = u.read().splitlines()

	ts = ts.drop(x)

	for i in range(len(ts.index)):
		if (ts.at[ts.index[i],'Best'] < week):
			ts.at[ts.index[i],'Best'] = ts.at[ts.index[i],'Better'] 

	for i in range(len(ts.index)):
		if (ts.at[ts.index[i],'Best'] < week):
			ts.at[ts.index[i],'Best'] = ts.at[ts.index[i],'Good']

	x_list = []
	for i in range(len(ts.index)):
		if (ts.at[ts.index[i],'Best'] < week):
			x_list.append(ts.index[i])

	ts = ts.drop(x_list)

	print(ts.sort_values(by='Best'))