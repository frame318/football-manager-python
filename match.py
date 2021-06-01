import time
import random
import player
import team
from event import Score


teamA = team.teamA
teamB = team.teamB

def calculate(teamA,teamB,teamA_football,teamB_football):
    if teamA_football == 1: # ทีม A ได้บอล
        player1 = teamA["players"][1]
        player2 = teamB["players"][1]
        god = "A"
        print("** TEAM A **")
    if teamB_football == 1: # ทีม B ได้บอล
        player1 = teamB["players"][1]
        player2 = teamA["players"][1]
        god = "B"
        print("** TEAM B **")

    #pass_ball = Score.pass_ball(player1,player2,god) #ส่งบอลเรียด
    #pass_high_ball = Score.pass_high_ball(player1,player2,god) # ส่งบอลโด่ง
    #drill_cross = Score.drill_cross(player1,player2,god) #เปิดเรียดจากริมเส้น
    #float_cross = Score.float_cross(player1,player2,god) #เปิดโด่งจากริมเส้น
    #dribbling = Score.dribbling(player1,player2,god) #เลี้ยงบอล
    #finding_score = Score.finding_score(player1,player2,god) #หาจังหวะยิง
    #heading = Score.heading(player1,player2,god) # แย่งโหม่ง
    #defenders_drill_cross = Score.defenders_drill_cross(player1,player2,god) # เข้าชาร์จลูกเปิดเรียด
    shot = Score.shot(player1,player2,god) #ยิง(ประตูเป็นประตูหรือไม่)
    print(shot)
    return shot


def matchStart(teamA,teamB):
    teamA_football = None  #ค่าการครองบอล
    teamB_football = None  #ค่าการครองบอล

    score_teamA = 0
    score_teamB = 0
    match_time = 0
    rd = random.randint(0,1) # random ทีมเริ่มบุก
    if rd == 1:
        teamA_football = 1
        teamB_football = 0
        print("ทีม A ได้บุกก่อน")
    else:
        teamA_football = 0
        teamB_football = 1
        print("ทีม B ได้บุกก่อน")
    while match_time < 10:
        results = calculate(
            teamA,teamB,
            teamA_football,teamB_football
            )
        print(results)
        teamA_football = results[0]
        teamB_football = results[1]
        if teamA_football == 1:
            print("ทีม A ได้บอล")
        if teamB_football == 1:
            print("ทีม B ได้บอล")
        time.sleep(1)
        match_time += 1
matchStart(teamA,teamB)