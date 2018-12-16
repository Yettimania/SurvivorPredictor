from scrap import scrap
from optimize_teams import sort_select,team_chance
import click

@click.group()



def cli1():
	pass
@cli1.command()
@click.option('--week','-w',default=0,help='Set current week.')
def predict(week):
	'''Print season predictions'''
	dataframe = scrap()
	team_chance(dataframe,week)

@click.group()
def cli2():
	pass
@cli2.command()
@click.option('--used','-u',default='',help='Add team to used list.')
def used_team(used):
	'''Add used team to list'''
	with open('used.txt', 'a') as the_file:
		the_file.write(used+'\n')

@click.group()
def cli3():
	pass
@cli3.command()
def clear_selections():
	'''Removes the list of used teams in the pool. '''
	open('used.txt', 'w').close()

cli = click.CommandCollection(sources=[cli1, cli2,cli3])

if __name__=='__main__':
	cli()
