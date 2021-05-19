
def batting(runs, four, six, balls, field):

    strike_rate = (runs/balls)*100
    points = (1/2)*runs
    if(runs>=50):
        points = points+5
    if(runs>=100):
        points = points+10
    if(strike_rate>=80 and strike_rate<=100):
        points = points+2
    if(strike_rate>100):
        points = points+4
    if(four>=1):
        points = points+(four*1)
    if(six>=1):
        points = points+(six*2)
    if(field>=1):
        points = points+(field*10)
    return (points)



def bowling(wkts, overs, runs, field):

    eco_rate = (runs/overs)
    points = (wkts*10)
    if(wkts>2 and wkts<5):
        points = points+5
    if(wkts>5):
        points = points+10
    if(eco_rate>=3.5 and eco_rate<=4.5):
        points = points+4
    if(eco_rate>=2 and eco_rate<=3.5):
        points = points+7
    if(eco_rate<2):
        points = points+10
    if(field>=1):
        points = points+(field*10)
    return (points)

if __name__ == '__main__':
    p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0,
          'balls': 119, 'field': 0}
    p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2,
          'balls': 112, 'field': 0}
    p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10,
          'runs': 71, 'field': 1}
    p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10,
          'runs': 45, 'field': 0}
    p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34,
          'field': 0}

    players_list = [p1,p2,p3,p4,p5]
    score_list = []

    for p in players_list:
        if(p.get('role')=='bat'):
            points = batting(p.get('runs'),p.get('4'),p.get('6'),p.get('balls'),p.get('field'))
            score_list.append({'name': p.get('name'), 'batscore': points})
        if(p.get('role')=='bowl'):
            points = bowling(p.get('wkts'),p.get('overs'),p.get('runs'),p.get('field'))
            score_list.append({'name': p.get('name'), 'bowlscore': points})

    for winner in score_list:
        print(winner)

