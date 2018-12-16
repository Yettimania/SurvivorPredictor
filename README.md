# Survivor Predictor Program	

I've never been a huge fan of fantasy football; I am a huge fan of Survivers pool though. I've been pretty impressive over the years usually making it into the top 100 survivors out of roughly 7000 every year. This year I really felt like it was my year. I was in the top 54 and selected Pittsburg and the Chargers in the same week. Steelers had a nailbiting finish with Jacksonville and I felt much more confident in the Chargers defeating Denver later that afternoon. The later game did not go as planned and I suffered the consequences. Case Keenum drove 80 yards on three plays to setup the game winning field goal as time expired. In true charger fashion, they choked big time. At one point they were even up I belive 18 points. This was the end of my run. Had the Chargers pulled this off, I would have been top 14 with the taste of victory lingurering on my tongue. 

The survivor pool I participate in utilizes 26 of 32 teams if you were to go the entire season. That has never happened in my experience but you have to make challenging choices on when to use 'mediocre' teams. Up till now its been all intution for me. I'll brag a little in saying that in the 2018 season, I did **NOT** select Minnesota at home to defeat the Bills knowing Josh Allen was going to make his debute game. I had zero information on this guy and wasn't going to risk it. That week over 2000 people were knocked out after the Bills throttled the Vikings. Needless to say you need to bank on some gut feelings in Survivor Pool. I did want to improve my chances using statistics however. 

FiveThirtyEight.com generates a lot of statistical information including probabilites on who will win each game of the entire NFL season. This is a complex model that I'm sure utilizes a number of variables. Typically they are pretty accurate but there is always that conflict of statistics versus intuition. Given that, I generated a program to assist me in making better decisions throughout the series by aggrigating and manipulating the data into a format that Is more helpful for me.

I utilized pythons BeautifulSoup library to pull all the statistics on win probabilites and stored them in a Pandas dataframe. This is done whenever the program is ran so every week I get a table of updated statistics. For every team, it has their win probability Week 1 thru 17. 

After collecting the data, I find each teams top 3 weeks to fin and structure that into another dataframe. I then sort it by week to determine what sequence the teams should be utilized in. With survivor, once you use a team, they can not be utilized again.

I created a pythong command line interface with Click to manage and clear a list of teams that I've utilized. So lets look at the 2018 season to date to see how well it would have went. 

The program is run by the command:

	python survivor.py predict
	
Which outputs

	python selector.py predict
	              Best Better Good
	Detroit          1      5    8
	New Orleans      2     17   12
	Washington       2     14   11
	Philadelphia     3     12   10
	Miami            3      9   16
	Minnesota        3      1    6
	Jacksonville     4      7    3
	Oakland          4      8    1
	Carolina         5      9   16
	N.Y. Jets        6     10    3
	Atlanta          7     10   15
	Tampa Bay        7     12   17
	Pittsburgh       8     17    1
	San Francisco   10      5    9
	N.Y. Giants     11     15    1
	Arizona         11      1    7
	Indianapolis    12      4   16
	Cincinnati      12     15    5
	Baltimore       12     17   15
	Green Bay       13      6    1
	Houston         13     17   14
	Tennessee       13     16    2
	Buffalo         14     12    2
	L.A. Chargers   14     12   11
	Denver          15     14    2
	Chicago         15     16   13
	Cleveland       16     14    3
	Dallas          16      2    9
	New England     17     16    1
	Seattle         17     13   15
	Kansas City     17     10    9
	L.A. Rams       17      8   16

First thing you'll notice is that Detroit had best chance to win in Week 1 when they got destroyed by the Jets 48-17. Again, this is a TOOL to help select teams. There was a reason I did not pick this game in Week 1 even if statistically it was the best option. 

1. Detroit had brand new head coach
2. Jets had a early 1st round pick QB who I had no idea how he'd perform.

There were a significant amount of people who chose Detroit probably due to the high probability but I had more security in choosing Minnesota Week 1 which was that teams second best win chance in the season. Week 3 when they played the Bills, I survived soley due to the intution. At least with this, I can figure out when I have the best odds to use the Bengals or the Browns.

This was a fun project that balance some web scraping using BeautifulSoup, some data science  and the development of a command line interface using Click. The complete CLI looks as follows:

	python selector.py --help
	Usage: selector.py [OPTIONS] COMMAND [ARGS]...
	
	Options:
	  --help  Show this message and exit.
	
	Commands:
	  clear-selections  Removes the list of used teams in the pool.
	  predict           Print season predictions
	  used-team         Add used team to list

You'll notice a few other small features, as teams get used or a week goes by, it will reorganize the data to bump up teams who have good chances remaining. If I wanted to see the teams after week 9, you'll notice you have more teams in the later weeks now given the top 3 chances are used to organize this table.

	Miami            9      9   16
	Carolina         9      9   16
	Atlanta         10     10   15
	N.Y. Jets       10     10    3
	San Francisco   10      5    9
	Arizona         11      1    7
	N.Y. Giants     11     15    1
	Indianapolis    12      4   16
	Cincinnati      12     15    5
	Baltimore       12     17   15
	Tampa Bay       12     12   17
	Philadelphia    12     12   10
	Green Bay       13      6    1
	Tennessee       13     16    2
	Houston         13     17   14
	Washington      14     14   11
	Buffalo         14     12    2
	L.A. Chargers   14     12   11
	Denver          15     14    2
	Chicago         15     16   13
	Dallas          16      2    9
	Cleveland       16     14    3
	New Orleans     17     17   12
	Kansas City     17     10    9
	Pittsburgh      17     17    1
	New England     17     16    1
	Seattle         17     13   15
	L.A. Rams       17      8   16
	
