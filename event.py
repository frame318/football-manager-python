import random
class Score():
    pass
    def pass_ball(player1,player2,god): #ส่งบอลเรียด

        p1_name = player1["name"]
        p1_Creativity = player1["Mental"]["Creativity"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Passing = player1["Technique"]["Passing"]
        p1_Technique = player1["Technique"]["Technique"]
        p1_Teamwork = player1["Mental"]["Teamwork"]
        p1 = p1_Creativity + p1_Off_the_ball + p1_Passing + p1_Technique + p1_Teamwork
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/100) + p1_Experience
        
        p2_name = player2["name"]
        p2_Decisions = player2["Mental"]["Decisions"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Marking = player2["Technique"]["Marking"]
        p2 = p2_Decisions + p2_Positioning + p2_Tackling + p2_Marking
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/80) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {} ส่งบอลสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {} ส่งบอลไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 

    def pass_high_ball(player1,player2,god): #ส่งบอลโด่ง
        p1_name = player1["name"]
        p1_Creativity = player1["Mental"]["Creativity"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Passing = player1["Technique"]["Crossing"]
        p1_Technique = player1["Technique"]["Technique"]
        p1_Teamwork = player1["Mental"]["Teamwork"]
        p1 = p1_Creativity + p1_Off_the_ball + p1_Passing + p1_Technique + p1_Teamwork
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/100) + p1_Experience
        
        p2_name = player2["name"]
        p2_Decisions = player2["Mental"]["Decisions"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Marking = player2["Technique"]["Marking"]
        p2 = p2_Decisions + p2_Positioning + p2_Tackling + p2_Marking
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/80) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {} ส่งบอลโด่งสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {} ส่งบอลโด่งไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 



    def drill_cross(player1,player2,god): #เปิดเรียดจากริมเส้น
        p1_name = player1["name"]
        p1_Acceleration = player1["Physical"]["Acceleration"]
        p1_Pace = player1["Physical"]["Pace"]
        p1_Aglilty = player1["Physical"]["Aglilty"]
        p1_Dribbing = player1["Technique"]["Dribbing"]
        p1_Technique = player1["Technique"]["Technique"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Crossingl = player1["Technique"]["Crossing"]
        p1_Passing = player1["Technique"]["Passing"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1 = p1_Acceleration + p1_Pace + p1_Aglilty + p1_Dribbing + p1_Technique \
            + p1_Off_the_ball + p1_Crossingl + p1_Passing + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/200) + p1_Experience
        
        p2_name = player2["name"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Acceleration = player2["Physical"]["Acceleration"]
        p2_Pace = player2["Physical"]["Pace"]
        p2_Aglilty = player2["Physical"]["Aglilty"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Decisions = player2["Mental"]["Decisions"]
        p2 = p2_Positioning + p2_Marking + p2_Acceleration + p2_Pace + p2_Aglilty + p2_Strength \
            + p2_Balance + p2_Tackling +p2_Decisions
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/180) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {} เปิดเรียดจากริมเส้นสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {} เปิดเรียดจากริมเส้นไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 

    def float_cross(player1,player2,god): #เปิดโด่งจากริมเส้น
        p1_name = player1["name"]
        p1_Acceleration = player1["Physical"]["Acceleration"]
        p1_Pace = player1["Physical"]["Pace"]
        p1_Aglilty = player1["Physical"]["Aglilty"]
        p1_Dribbing = player1["Technique"]["Dribbing"]
        p1_Technique = player1["Technique"]["Technique"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Crossingl = player1["Technique"]["Crossing"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1 = p1_Acceleration + p1_Pace + p1_Aglilty + p1_Dribbing + p1_Technique \
            + p1_Off_the_ball + p1_Crossingl + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/180) + p1_Experience
        
        p2_name = player2["name"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Acceleration = player2["Physical"]["Acceleration"]
        p2_Pace = player2["Physical"]["Pace"]
        p2_Aglilty = player2["Physical"]["Aglilty"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Decisions = player2["Mental"]["Decisions"]
        p2 = p2_Positioning + p2_Marking + p2_Acceleration + p2_Pace + p2_Aglilty + p2_Strength \
            + p2_Balance + p2_Tackling +p2_Decisions
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/180) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {} เปิดโด่งจากริมเส้นสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {} เปิดโด่งจากริมเส้นไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 


    def dribbling(player1,player2,god): #เลี้ยงบอล

        p1_name = player1["name"]
        p1_Dribbing = player1["Technique"]["Dribbing"]
        p1_Technique = player1["Technique"]["Technique"]
        p1_Aglilty = player1["Physical"]["Aglilty"]
        p1_Acceleration = player1["Physical"]["Acceleration"]
        p1_Pace = player1["Physical"]["Pace"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]

        p1 = p1_Acceleration + p1_Pace + p1_Aglilty + p1_Dribbing + p1_Technique \
             + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/140) + p1_Experience
        
        p2_name = player2["name"]
        p2_Decisions = player2["Mental"]["Decisions"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Acceleration = player2["Physical"]["Acceleration"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]

        p2 =  p2_Marking + p2_Acceleration + p2_Strength \
            + p2_Balance + p2_Tackling +p2_Decisions
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/120) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {} เลี้ยงบอลสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {} เลี้ยงบอลไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 


    def finding_score(player1,player2,god): #หาจังหวะยิง(มีบอลกับตัว)
        
        p1_name = player1["name"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Dribbing = player1["Technique"]["Dribbing"]
        p1_Acceleration = player1["Physical"]["Acceleration"]
        p1_Pace = player1["Physical"]["Pace"]
        p1_Aglilty = player1["Physical"]["Aglilty"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1_Technique = player1["Technique"]["Technique"]

        p1 = p1_Off_the_ball + p1_Acceleration + p1_Pace + p1_Aglilty + p1_Dribbing + p1_Technique \
             + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/160) + p1_Experience
        
        p2_name = player2["name"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Decisions = player2["Mental"]["Decisions"]

        p2 =  p2_Marking + p2_Positioning + p2_Strength \
            + p2_Balance + p2_Tackling +p2_Decisions
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/120) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {}  หาจังหวะยิงสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {}  หาจังหวะยิงไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} สะกัดบอลสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} สะกัดบอลไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 


    def heading(player1,player2,god): # แย่งโหม่ง

        p1_name = player1["name"]
        p1_Jumping = player1["Physical"]["Jumping"]
        p1_Heading = player1["Technique"]["Heading"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1_Technique = player1["Technique"]["Technique"]

        p1 = p1_Off_the_ball + p1_Jumping + p1_Heading + p1_Technique \
             + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/120) + p1_Experience
        
        p2_name = player2["name"]
        p2_Jumping = player2["Physical"]["Jumping"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Heading = player2["Technique"]["Heading"]
        p2_Positioning = player2["Mental"]["Positioning"]


        p2 =  p2_Marking + p2_Positioning + p2_Strength \
            + p2_Balance + p2_Jumping +p2_Heading
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/120) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {}  แย่งโหม่งสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {}  แย่งโหม่งไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} แย่งโหม่งสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} แย่งโหม่งไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 

    def defenders_drill_cross(player1,player2,god): # เข้าชาร์จลูกเปิดเรียด
        p1_name = player1["name"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]
        p1_Acceleration = player1["Physical"]["Acceleration"]
        p1_Pace = player1["Physical"]["Pace"]
        p1_Aglilty = player1["Physical"]["Aglilty"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1_Technique = player1["Technique"]["Technique"]

        p1 = p1_Off_the_ball + p1_Acceleration + p1_Pace + p1_Aglilty + p1_Technique \
             + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/140) + p1_Experience
        

        p2_name = player2["name"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Positioning = player2["Mental"]["Positioning"]
        p2_Tackling = player2["Technique"]["Tackling"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Acceleration = player2["Physical"]["Acceleration"]

        p2 =  p2_Marking + p2_Positioning + p2_Strength \
            + p2_Balance + p2_Tackling + p2_Acceleration
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/120) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {}  เปิดเรียดสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {}  เปิดเรียดไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {}  เข้าชาร์จลูกเปิดเรียดสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} ข้าชาร์จลูกเปิดเรียดไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 


    def heading(player1,player2,god): # แย่งโหม่ง

        p1_name = player1["name"]
        p1_Off_the_ball = player1["Mental"]["Off the ball"]


        p1_Jumping = player1["Physical"]["Jumping"]
        p1_Heading = player1["Technique"]["Heading"]
        p1_Strength = player1["Physical"]["Strength"]
        p1_Balance = player1["Physical"]["Balance"]
        p1_Technique = player1["Technique"]["Technique"]

        p1 = p1_Off_the_ball + p1_Jumping + p1_Heading + p1_Technique \
             + p1_Strength +p1_Balance
        p1_Experience = player1["Experience"]
        sum1 = ((p1*100)/120) + p1_Experience
        
        p2_name = player2["name"]
        p2_Jumping = player2["Physical"]["Jumping"]
        p2_Marking = player2["Technique"]["Marking"]
        p2_Strength = player2["Physical"]["Strength"]
        p2_Balance = player2["Physical"]["Balance"]
        p2_Heading = player2["Technique"]["Heading"]
        p2_Positioning = player2["Mental"]["Positioning"]


        p2 =  p2_Marking + p2_Positioning + p2_Strength \
            + p2_Balance + p2_Jumping +p2_Heading
        p2_Experience = player2["Experience"]
        sum2 = ((p2*100)/120) + p2_Experience

        if sum1 > sum2:
            results = 100-((sum2*100)/sum1)
            Total = results + 50
            print("ทีมบุก win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมบุก {}  แย่งโหม่งสำเร็จ".format(p1_name))
            else:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมบุก {}  แย่งโหม่งไม่สำเร็จ".format(p1_name))
        elif sum2 > sum1:
            results = 100-((sum1*100)/sum2)
            Total = results + 50
            print("ทีมรับ win ที่ {} \n โอกาศชนะ {}".format(results,Total))
            Competition = random.randrange(100.00) < Total
            print(Competition)
            if Competition == True:
                teamA_football  = 0
                teamB_football  = 1
                print("ทีมรับ {} แย่งโหม่งสำเร็จ".format(p2_name))
            else:
                teamA_football  = 1
                teamB_football  = 0
                print("ทีมรับ {} แย่งโหม่งไม่สำเร็จ".format(p2_name))
        else:
            print("always")
        print(sum1,sum2)
        if god == "A":
            return teamA_football ,teamB_football 
        if god == "B":
            return teamB_football,teamA_football 


    def shot(player1,player2,god): # ยิง(ประตูเป็นประตูหรือไม่)
        return player2
    def long_shot(a): # ยิงไกล(ประตูเป็นประตูหรือไม่)
        return a
    def Heading_goal(a): # โหม่งทำประตู
        return a
    def one_on_one_Shot(a): # ลูกหลุดเดี่ยว
        return a
    def offside(a): # ดักล้ำหน้า
        return a
    def corner(a): # เตะมุม
        return a
    def freekick(a): # ฟรีคลิก
        return a
    def penalty(a): # ลูกโทษ
        return a
    def counter_attack_short(a): # โต้กลับ (เล่นสั้นๆ)
        return a
    def counter_attack_long(a): # โต้กลับ (เล่นบอลยาว)
        return a

class Ball_possession():
    pass
    def team_formation(a): # ระบบที่เล่น 
        return a
    def ability_players(a): # ความสามารถของผู้เล่นทุกคนยกเว้นผู้รักษาประตู
        return a
    def home_game(a): # ความได้เปรียบของเจ้าบ้าน (เฉพาะเกมในลีก)
        return a
    def strategy(a): # รูปแบบการเล่น
        return a
    def defensive_line(a): # แนวรับ 
        return a
    def creative_freedom(a): # อิสระในการสร้างสรรค์ 
        return a
    def tackling(a): # เข้าปะทะ
        return a
    def marking(a): # ประกบตัว
        return a
    def closing_down(a): # การไล่บอล
        return a
    def roaming(a): # การรักษาตำแหน่ง
        return a
    def having_player(a): # กัปตันที่มีความเป็นผู้นำสูงส่งผลดีกับทีม
        return a