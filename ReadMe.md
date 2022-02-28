Shot Chart Documentation
Data Points:
Shot_num		shot number of data sheet (starts at 0)
Shooter 		Number of shooter
Goalie_hand 		Hand of goalie
(right=0, left=1)
shot_hand		hand of shot
(right=0, left=1)
Type_shot_0		type of shot
Over hand = 0 ; side arm = 1 ; under hand = 2 ; back hand = 3 ; behind the back = 4
type_shot_1 		type of shot
Stationary = 0 ; on the run = 1 ; quick stick = 2 ; MORE?
Loc_x			location of shot horizontally from goal in yards
(-20,20)
Loc_y			location of shot vertically from goal in yards
(0,20)
Dist			distance from goal in yards
(loc x)2+(loc y)2
Loc_goal		location of shot on goal (SUBJECT TO CHANGE)
Bounce		bouncer shot?
0 = yes ; 1 = no
Result			result of shot
0 = goal ; 1 = save ; 2 = miss ; 3 = pipe ; 4 = blocked
Screen			Was the shot screened?
0 = yes ; 1 = no
HUDLtime		timestamp in HUDL
Notes			extra notes pertaining to the shot










Field dimensions for manual data collection

Data and Plots Example:
Example Data
shot_num
shooter
goalie_hand
shot_hand
type_shot_0
type_shot_1
loc_x
loc_y
dist
loc_goal
bounce
result
screen
HUDLtime
Notes:
0
6
0
0
0
2
-2
4
4.47
9
1
2
1
21.45


1
4
0
1
0
0
-4
6
7.21
14
1
3
1
24.27


2
5
0
0
0
1
4
3
5
17
1
0
1
25.32


3
4
0
0
1
0
-1
13
13.04
5
1
0
0
32.35


4
6
0
0
0
2
0
5
5
6
0
4
0
34.04


5
5
0
0
0
1
-4
12
12.65
13
1
1
0
36.32


6
6
0
1
0
0
-5
5
7.07
11
1
1
1
N/A








Example Plots
Can get shot charts for specific players
From example data charts are shown for player #4,5,6 and whole team
		
		
Order of extra data if wanted on chart:
Goal location [0,29] N for NA (see Goal Location section below)
Hand shot (L,R)
Type_shot_0
Over hand = 0 ; side arm = 1 ; under hand = 2 ; back hand = 3 ; 
behind the back = 4
Type_shot_1
Stationary = 0 ; on the run = 1 ; quick stick = 2 ; MORE?
Distance from goal






Goal Location
Done by sectioning the goal into 16 boxes and extending boxes to the outside area of the goal.
Orange is the goal space, green is miss. 

0
5
10
15
20
25
1
6
11
16
21
26
2
7
12
17
22
27
3
8
13
18
23
28
4
9
14
19
24
29



