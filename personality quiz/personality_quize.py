
from ra8y import (thinker_d, socialbutterfly_d, explorer_d, relaxer_d)
from ra8y import (q1_prompt, q2_prompt, q3_prompt)
pta = "pls try enter a valed answer"

x = ['1','2','3','4']
# the Qustions 

q_1 = input(q1_prompt)
while True :
    
    if q_1 in x :

        q_1 = int(q_1)
        break

    print (pta)
    q_1 = input(q1_prompt)


q_2 = input(q2_prompt)
while True:

    if q_2 in x:

        q_2 = int(q_2)
        break

    print (pta)
    q_2 = input(q2_prompt)


q_3 = input(q3_prompt)
while True:

    if q_3 in x:

        q_3 = int(q_3)
        break
    
    print (pta)
    q_3 = input(q3_prompt)

# the variable for u
thinker = 0
social_butterfly = 0
explorer = 0
relaxer = 0

# ifat ktera 3shan tba mesh mabsot :)
if q_1 == 1:
    thinker += 1
elif q_1 == 2:
    social_butterfly += 1
elif q_1 == 3:
    explorer += 1
elif q_1 == 4:
    relaxer += 1

if q_2 == 1:
    relaxer += 1
elif q_2 == 2:
    social_butterfly += 1
elif q_2 == 3:
    explorer += 1
elif q_2 == 4:
    thinker += 1

if q_3 == 1:
    thinker += 1
elif q_3 == 2:
    social_butterfly += 1
elif q_3 == 3:
    explorer += 1
elif q_3 == 4:
    relaxer += 1

# a5er ifat 5las 
if thinker > social_butterfly and thinker > explorer and thinker > relaxer:
    print(thinker_d)
elif social_butterfly > thinker and social_butterfly > explorer and social_butterfly > relaxer:
    print(socialbutterfly_d)
elif explorer > thinker and explorer > social_butterfly and explorer > relaxer:
    print(explorer_d)
elif relaxer > thinker and relaxer > explorer and relaxer > social_butterfly:
    print(relaxer_d)
elif thinker == explorer:
    print("anta  mix")
else:
    print('- you are a balanced person! go make a friend xd')

    
