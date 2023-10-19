#### SER594: Exploratory Data Munging and Visualization
#### Football results prediction
#### Rahul Balulmath
#### 10/18/2023

## Basic Questions
**Dataset Author(s):** Football-Data.co.uk
After doing some research, I landed on this site: https://datahub.io/collections/football, which contained structured datasets for a variety of football competitions ranging from national leagues to world cups.

For this project, I decided to select the datasets for the top 5 European Leagues that contained the match results for the last 9 years.

Here are the links to the datasets that I used:

https://datahub.io/sports-data/english-premier-league
https://datahub.io/sports-data/spanish-la-liga
https://datahub.io/sports-data/italian-serie-a
https://datahub.io/sports-data/german-bundesliga
https://datahub.io/sports-data/french-ligue-1  

**Dataset Construction Date:** The dataset contains data from various seasons ranging from 1993 to 2024 and last updated is 15/10/23.

**Dataset Record Count:** It has 380 records every year so for 30 years it is 11400 records.

**Dataset Field Meanings:** 
Div = League Division
Date = Match Date (dd/mm/yy)
Time = Time of match kick off
HomeTeam = Home Team
AwayTeam = Away Team
FTHG and HG = Full Time Home Team Goals
FTAG and AG = Full Time Away Team Goals
FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

Match Statistics
Attendance = Crowd Attendance
Referee = Match Referee
HS = Home Team Shots
AS = Away Team Shots
HST = Home Team Shots on Target
AST = Away Team Shots on Target
HHW = Home Team Hit Woodwork
AHW = Away Team Hit Woodwork
HC = Home Team Corners
AC = Away Team Corners
HF = Home Team Fouls Committed
AF = Away Team Fouls Committed
HFKC = Home Team Free Kicks Conceded
AFKC = Away Team Free Kicks Conceded
HO = Home Team Offsides
AO = Away Team Offsides
HY = Home Team Yellow Cards
AY = Away Team Yellow Cards
HR = Home Team Red Cards
AR = Away Team Red Cards
HBP = Home Team Bookings Points (10 = yellow, 25 = red)
ABP = Away Team Bookings Points (10 = yellow, 25 = red)

Note that Free Kicks Conceeded includes fouls, offsides and any other offense commmitted and will always be equal to or higher than the number of fouls. Fouls make up the vast majority of Free Kicks Conceded. Free Kicks Conceded are shown when specific data on Fouls are not available (France 2nd, Belgium 1st and Greece 1st divisions).

Note also that English and Scottish yellow cards do not include the initial yellow card when a second is shown to a player converting it into a red, but this is included as a yellow (plus red) for European games.


Key to 1X2 (match) betting odds data:

B365H = Bet365 home win odds
B365D = Bet365 draw odds
B365A = Bet365 away win odds
BSH = Blue Square home win odds
BSD = Blue Square draw odds
BSA = Blue Square away win odds
BWH = Bet&Win home win odds
BWD = Bet&Win draw odds
BWA = Bet&Win away win odds
GBH = Gamebookers home win odds
GBD = Gamebookers draw odds
GBA = Gamebookers away win odds
IWH = Interwetten home win odds
IWD = Interwetten draw odds
IWA = Interwetten away win odds
LBH = Ladbrokes home win odds
LBD = Ladbrokes draw odds
LBA = Ladbrokes away win odds
PSH and PH = Pinnacle home win odds
PSD and PD = Pinnacle draw odds
PSA and PA = Pinnacle away win odds
SOH = Sporting Odds home win odds
SOD = Sporting Odds draw odds
SOA = Sporting Odds away win odds
SBH = Sportingbet home win odds
SBD = Sportingbet draw odds
SBA = Sportingbet away win odds
SJH = Stan James home win odds
SJD = Stan James draw odds
SJA = Stan James away win odds
SYH = Stanleybet home win odds
SYD = Stanleybet draw odds
SYA = Stanleybet away win odds
VCH = VC Bet home win odds
VCD = VC Bet draw odds
VCA = VC Bet away win odds
WHH = William Hill home win odds
WHD = William Hill draw odds
WHA = William Hill away win odds

Bb1X2 = Number of BetBrain bookmakers used to calculate match odds averages and maximums
BbMxH = Betbrain maximum home win odds
BbAvH = Betbrain average home win odds
BbMxD = Betbrain maximum draw odds
BbAvD = Betbrain average draw win odds
BbMxA = Betbrain maximum away win odds
BbAvA = Betbrain average away win odds

MaxH = Market maximum home win odds
MaxD = Market maximum draw win odds
MaxA = Market maximum away win odds
AvgH = Market average home win odds
AvgD = Market average draw win odds
AvgA = Market average away win odds



Key to total goals betting odds:

BbOU = Number of BetBrain bookmakers used to calculate over/under 2.5 goals (total goals) averages and maximums
BbMx>2.5 = Betbrain maximum over 2.5 goals
BbAv>2.5 = Betbrain average over 2.5 goals
BbMx<2.5 = Betbrain maximum under 2.5 goals
BbAv<2.5 = Betbrain average under 2.5 goals

GB>2.5 = Gamebookers over 2.5 goals
GB<2.5 = Gamebookers under 2.5 goals
B365>2.5 = Bet365 over 2.5 goals
B365<2.5 = Bet365 under 2.5 goals
P>2.5 = Pinnacle over 2.5 goals
P<2.5 = Pinnacle under 2.5 goals
Max>2.5 = Market maximum over 2.5 goals
Max<2.5 = Market maximum under 2.5 goals
Avg>2.5 = Market average over 2.5 goals
Avg<2.5 = Market average under 2.5 goals



Key to Asian handicap betting odds:

BbAH = Number of BetBrain bookmakers used to Asian handicap averages and maximums
BbAHh = Betbrain size of handicap (home team)
AHh = Market size of handicap (home team) (since 2019/2020)
BbMxAHH = Betbrain maximum Asian handicap home team odds
BbAvAHH = Betbrain average Asian handicap home team odds
BbMxAHA = Betbrain maximum Asian handicap away team odds
BbAvAHA = Betbrain average Asian handicap away team odds

GBAHH = Gamebookers Asian handicap home team odds
GBAHA = Gamebookers Asian handicap away team odds
GBAH = Gamebookers size of handicap (home team)
LBAHH = Ladbrokes Asian handicap home team odds
LBAHA = Ladbrokes Asian handicap away team odds
LBAH = Ladbrokes size of handicap (home team)
B365AHH = Bet365 Asian handicap home team odds
B365AHA = Bet365 Asian handicap away team odds
B365AH = Bet365 size of handicap (home team)
PAHH = Pinnacle Asian handicap home team odds
PAHA = Pinnacle Asian handicap away team odds
MaxAHH = Market maximum Asian handicap home team odds
MaxAHA = Market maximum Asian handicap away team odds	
AvgAHH = Market average Asian handicap home team odds
AvgAHA = Market average Asian handicap away team odds

**Dataset File Hash(es):** 
season-0910_csv.csv: 012bcfb1099e3b83b2f40f80e4c59f36
season-1011_csv.csv: 12b75512cb321d6e7c57487d531c18ee
season-1112_csv.csv: 3b5f9d5afa8ef04b8ab98a3c3b9e96bc
season-1213_csv.csv: 0fe18939a74ff1cdbd73c95661794643
season-1314_csv.csv: dc4c8bb3fe2f7937feab70cf8960dcc8
season-1415_csv.csv: 33180a370db6d071e37bab8d6d52ff73
season-1516_csv.csv: 4048e54109fc798659daa6a59a5bcb9b
season-1617_csv.csv: 93c9926e3ef827f0e15439799f1ac6f5
season-1718_csv.csv: 8d03ef2868caebc916e307ad19589b28
season-1819_csv.csv: 62cea9db168699618f8a7f20e0d6389d
season-1920_csv.csv: 763d5f1a0785bf9e95782a5dfe6bcbde
season-2021_csv.csv: f8a6fc6922c8108bbba96e5e59f53aaa
season-2122_csv.csv: 5f2d9b96f2282d8e2c730fba4ef8b2fe
season-2223_csv.csv: 3375cf86180f975cc30632812b0305f2
season-2324_csv.csv: b63417562200a9da789180521b55e273


## Interpretable Records
### Record 1
**Raw Data:** 
League: E0 (English Premier League)
Date: 11/8/2023
Time: 20:00
Home Team: Burnley
Away Team: Manchester City
Full Time Home Team Goals (FTHG): 0
Full Time Away Team Goals (FTAG): 3
Full Time Result (FTR): A (Away Win)
Half Time Home Team Goals (HTHG): 0
Half Time Away Team Goals (HTAG): 2
Half Time Result (HTR): A (Away Win)
Referee: C Pawson
Home Team Shots (HS): 6
Away Team Shots (AS): 17
Home Team Shots on Target (HST): 1
Away Team Shots on Target (AST): 8
Home Team Fouls (HF): 11
Away Team Fouls (AF): 8
Home Team Corners (HC): 6
Away Team Corners (AC): 5
Home Team Yellow Cards (HY): 0
Away Team Yellow Cards (AY): 0
Home Team Red Cards (HR): 1
Away Team Red Cards (AR): 0
Betting Odds from various bookmakers

**Interpretation:** 
In this match, Manchester City visited Burnley on the 11th of August, 2023, for an English Premier League match. The game kicked off at 20:00 hours. By half-time, Manchester City was leading with 2 goals to nil, and the match ended with a 3-0 victory in favor of Manchester City. The referee for this match was C Pawson. Over the course of the match, Burnley managed to take 6 shots with only 1 being on target, while Manchester City had a total of 17 shots with 8 on target. Burnley committed 11 fouls, received one red card but no yellow cards, whereas Manchester City committed 8 fouls with no cards issued. Additionally, betting odds from various bookmakers are provided for different outcomes including match results, total goals over/under 2.5, and Asian handicap. This record is reasonable given it follows the typical format of soccer match data and includes various in-game statistics and betting odds.

### Record 2
**Raw Data:** 
League: E0 (English Premier League)
Date: 12/8/2023
Time: 12:30
Home Team: Arsenal
Away Team: Nottingham Forest
Full Time Home Team Goals (FTHG): 2
Full Time Away Team Goals (FTAG): 1
Full Time Result (FTR): H (Home Win)
Half Time Home Team Goals (HTHG): 2
Half Time Away Team Goals (HTAG): 0
Half Time Result (HTR): H (Home Win)
Referee: M Oliver
Home Team Shots (HS): 15
Away Team Shots (AS): 6
Home Team Shots on Target (HST): 7
Away Team Shots on Target (AST): 2
Home Team Fouls (HF): 12
Away Team Fouls (AF): 12
Home Team Corners (HC): 8
Away Team Corners (AC): 3
Home Team Yellow Cards (HY): 2
Away Team Yellow Cards (AY): 2
Home Team Red Cards (HR): 0
Away Team Red Cards (AR): 0
Betting Odds from various bookmakers

**Interpretation:** 
On the 12th of August, 2023, Arsenal hosted Nottingham Forest for a match in the English Premier League, which kicked off at 12:30 hours. By the end of the first half, Arsenal was leading with 2 goals, and Nottingham Forest had not scored. The match ended with a 2-1 victory for Arsenal. The referee for this game was M Oliver. Throughout the match, Arsenal took a total of 15 shots with 7 on target, while Nottingham Forest had 6 shots with 2 on target. Both teams committed 12 fouls each and received 2 yellow cards each with no red cards issued. Betting odds from various bookmakers are provided, covering different betting markets such as match results, total goals over/under 2.5, and Asian handicap. This record provides a detailed insight into the match events, in-game statistics, and betting odds, making it reasonable and typical of soccer match data.

## Background Domain Knowledge
Soccer, known as football outside of North America, is a beloved sport with a rich history dating back over 2,000 years. The modern version of soccer, governed by the Fédération Internationale de Football Association (FIFA), is played by 270 million people worldwide. The sport's popularity is largely attributed to its simplicity and the minimal equipment required to play.
Predicting soccer scores has become a topic of interest among fans, statisticians, and bettors. Accurate predictions can provide insights into team performance, player effectiveness, and coaching strategies. Moreover, they can also be financially lucrative in the betting market. However, soccer score prediction is complex due to the myriad of variables that can influence the outcome of a game. These include team strategies, player fitness levels, weather conditions, and even the morale of the teams.
Statistical modeling and machine learning have been extensively employed in attempts to predict soccer scores. Traditional statistical methods like Poisson regression have been used to model the number of goals scored by each team. More recently, machine learning and deep learning approaches have been employed to take into account a wider array of factors and potentially uncover complex patterns that might elude traditional methods.
There are various datasets available that provide a wealth of information for those interested in soccer score prediction. These datasets contain historical data on team performance, player statistics, and even minute-by-minute event data for individual matches. The utilization of this data in predictive modeling requires rigorous data munging to ensure that the data is in a usable format and free of errors.
Furthermore, the domain of soccer score prediction also intersects with the gambling industry, which has its own set of legal and ethical considerations. Accurate predictions can be used to set betting odds, and there is a large community of amateur and professional bettors looking to gain an edge.
In this project, the aim is to delve into the intricacies of soccer score prediction, leveraging historical data, statistical analysis, and machine learning techniques to build predictive models. The endeavor will involve extensive data exploration, cleaning, and transformation to ensure the data's quality and relevance to the task at hand. Through this project, a deeper understanding of the factors that influence soccer match outcomes will be sought, contributing to the broader knowledge base on soccer analytics and prediction.
References:
Hyndman, R.J. (2020). Forecasting: principles and practice. OTexts.
Strumbelj, E. (2014). On determining probability forecasts from betting odds. International Journal of Forecasting, 30(4), 934-943.
Kovalchik, S. (2016). Searching for the GOAT of tennis win prediction. Journal of Quantitative Analysis in Sports, 12(3), 127-138.

## Data Transformation

### Transformation 1: Handling Missing Data for Continuous Features
**Description:** 
For features such as 'HomeGoals' and 'AwayGoals', missing data was replaced with the mean value of the feature for the respective team using Pandas `fillna` method.

**Soundness Justification:** 
This transformation is reasonable as it helps in maintaining the data distribution and does not drastically affect the mean and variance of the dataset. Using the mean value is a common practice to impute missing values for continuous data and keeps the semantics of the data intact.

### Transformation 2: Handling Missing Data for Categorical Features
**Description:** 
For discrete features such as 'HomeTeam', 'AwayTeam', and 'League', rows with missing data were dropped from the dataset using Pandas `dropna` method.

**Soundness Justification:** 
This transformation is sound as it ensures the integrity and completeness of the dataset for these categorical features, where imputation may not be appropriate or straightforward. Given the small number of such rows (less than 20), dropping them should not significantly impact the representativeness of the data.

### Transformation 3: Label Encoding
**Description:** 
The categorical variables representing the home and away teams are transformed into numerical values using a custom label encoding function, as the sklearn's LabelEncoder is not among the allowed packages.

**Soundness Justification:** 
This transformation is sound as it converts categorical data into a numerical format without adding any erroneous information, which makes it suitable for machine learning algorithms. The semantics of the data remain intact as each unique category is mapped to a unique integer.

### Transformation 4: Feature Selection
**Description:** 
A specific set of columns are selected as features for the machine learning model based on domain knowledge and the data available using Pandas `loc` method.

**Soundness Justification:** 
This transformation is sound as it focuses the machine learning model on the relevant information and discards irrelevant data, which should lead to better predictive performance. It doesn't introduce errors or discard usable data, and the semantics of the data remain unchanged.

### Transformation 5: Data Splitting
**Description:** 
The dataset is split into training and testing sets using a custom split function, as sklearn's train_test_split is not among the allowed packages.

**Soundness Justification:** 
This transformation is sound as it follows common practice in machine learning to have separate data for training and evaluation to ensure the model generalizes well to unseen data. It does not introduce errors or outliers and retains the semantics and integrity of the data.


## Visualization

### Visual 1: Histogram for FTR (Full Time Result)
**Analysis:** 
It indicates that Most wins are at home compared to draws and losses.