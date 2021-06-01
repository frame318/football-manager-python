import random
pos = ["ST","AMC","AML","AMR","MC","ML","MR","DMC","DML","DMR",
        "DC","DL","DR","GK"]
p1 = {
    "name":"frame",
    "Pos":(random.choice(pos)),
    "Condition":92,  #ความฟิต
    "Morale":"Poor", #ความมั่นใจ 
    "Experience":10, #ประสบการณ์
    "Technique":{
        "Set Pieces":(random.randint(1,20)), #ลูกตั้งเตะ
        "Crossing":(random.randint(1,20)), #โยนบอลจากริมเส้น
        "Dribbing":(random.randint(1,20)), #เลี้ยงบอล
        "Finishing":(random.randint(1,20)), #การยิงประตู
        "Heading":(random.randint(1,20)), #การโหม่ง
        "Long shots":(random.randint(1,20)), #ยิงไกล
        "Marking":(random.randint(1,20)), #ประกบตัวคู่ต่อสู้
        "Passing":(random.randint(1,20)), #ส่งบอล
        "Tackling":(random.randint(1,20)), #การเข้าปะทะ
        "Technique":(random.randint(1,20)), #ความสามารถเฉพาะตัว
    },
    "Mental":{
        "Aggression":(random.randint(1,20)), #ความรุนแรง
        "Creativity":(random.randint(1,20)), #ความคิดสร้างสรรค์
        "Decisions":(random.randint(1,20)), #การตัดสินใจ
        "Determination":(random.randint(1,20)), #ความมุ่งมั่น
        "Influence":(random.randint(1,20)), #ความเป็นผู้นำ
        "Positioning":(random.randint(1,20)), #การยืนตำแหน่ง
        "Off the ball":(random.randint(1,20)), #หาช่องว่าง
        "Teamwork":(random.randint(1,20)), #เล่นเป็นทีม           
    },"Physical":{
        "Acceleration":(random.randint(1,20)), #การวิ่งออกตัว
        "Aglilty":(random.randint(1,20)), #ความคล่องแคล่ว
        "Balance":(random.randint(1,20)), #สมดุลร่างกาย
        "Jumping":(random.randint(1,20)), #กระโดด
        "Pace":(random.randint(1,20)), #ความเร็วในการวิ่ง
        "Stamina":(random.randint(1,20)), #ความอึด
        "Strength":(random.randint(1,20)), #ความแข็งแกร่ง
    }}

p2 = {
    "name":"TEST",
    "Pos":(random.choice(pos)),
    "Condition":92,  #ความฟิต
    "Morale":"Poor", #ความมั่นใจ 
    "Experience":10, #ประสบการณ์
    "Technique":{
        "Set Pieces":(random.randint(1,20)), #ลูกตั้งเตะ
        "Crossing":(random.randint(1,20)), #โยนบอลจากริมเส้น
        "Dribbing":(random.randint(1,20)), #เลี้ยงบอล
        "Finishing":(random.randint(1,20)), #การยิงประตู
        "Heading":(random.randint(1,20)), #การโหม่ง
        "Long shots":(random.randint(1,20)), #ยิงไกล
        "Marking":(random.randint(1,20)), #ประกบตัวคู่ต่อสู้
        "Passing":(random.randint(1,20)), #ส่งบอล
        "Tackling":(random.randint(1,20)), #การเข้าปะทะ
        "Technique":(random.randint(1,20)), #ความสามารถเฉพาะตัว
    },
    "Mental":{
        "Aggression":(random.randint(1,20)), #ความรุนแรง
        "Creativity":(random.randint(1,20)), #ความคิดสร้างสรรค์
        "Decisions":(random.randint(1,20)), #การตัดสินใจ
        "Determination":(random.randint(1,20)), #ความมุ่งมั่น
        "Influence":(random.randint(1,20)), #ความเป็นผู้นำ
        "Positioning":(random.randint(1,20)), #การยืนตำแหน่ง
        "Off the ball":(random.randint(1,20)), #หาช่องว่าง
        "Teamwork":(random.randint(1,20)), #เล่นเป็นทีม           
    },"Physical":{
        "Acceleration":(random.randint(1,20)), #การวิ่งออกตัว
        "Aglilty":(random.randint(1,20)), #ความคล่องแคล่ว
        "Balance":(random.randint(1,20)), #สมดุลร่างกาย
        "Jumping":(random.randint(1,20)), #กระโดด
        "Pace":(random.randint(1,20)), #ความเร็วในการวิ่ง
        "Stamina":(random.randint(1,20)), #ความอึด
        "Strength":(random.randint(1,20)), #ความแข็งแกร่ง
    },"Goalkeeping":{
        "Handling":(random.randint(1,20)), #การจับบอล
        "Reflex":(random.randint(1,20)), #การตอบสนอง
        "Kicking":(random.randint(1,20)), #การแตะบอล
        "One on ones":(random.randint(1,20)), #ดวลตัวต่อตัว
        "Rushing out":(random.randint(1,20)), #ออกมาตัดบอล
        "Aerial ability":(random.randint(1,20)), #ล่นบอลกลางอากาศ 	
    }}

p3 = {
    "name":"messi",
    "Pos":"ST",
    "Condition":100,  #ความฟิต
    "Morale":"Poor", #ความมั่นใจ 
    "Experience":10, #ประสบการณ์
    "Technique":{
        "Set Pieces":10, #ลูกตั้งเตะ
        "Crossing":20, #โยนบอลจากริมเส้น
        "Dribbing":10, #เลี้ยงบอล
        "Finishing":10, #การยิงประตู
        "Heading":10, #การโหม่ง
        "Long shots":10, #ยิงไกล
        "Marking":10, #ประกบตัวคู่ต่อสู้
        "Passing":20, #ส่งบอล
        "Tackling":10, #การเข้าปะทะ
        "Technique":20, #ความสามารถเฉพาะตัว
    },
    "Mental":{
        "Aggression":10, #ความรุนแรง
        "Creativity":15, #ความคิดสร้างสรรค์
        "Decisions":10, #การตัดสินใจ
        "Determination":10, #ความมุ่งมั่น
        "Influence":10, #ความเป็นผู้นำ
        "Positioning":10, #การยืนตำแหน่ง
        "Off the ball":15, #หาช่องว่าง
        "Teamwork":15, #เล่นเป็นทีม           
    },"Physical":{
        "Acceleration":10, #การวิ่งออกตัว
        "Aglilty":10, #ความคล่องแคล่ว
        "Balance":10, #สมดุลร่างกาย
        "Jumping":10, #กระโดด
        "Pace":10, #ความเร็วในการวิ่ง
        "Stamina":10, #ความอึด
        "Strength":10, #ความแข็งแกร่ง
    },"Goalkeeping":{
        "Handling":10, #การจับบอล
        "Reflex":10, #การตอบสนอง
        "Kicking":10, #การแตะบอล
        "One on ones":10, #ดวลตัวต่อตัว
        "Rushing out":10, #ออกมาตัดบอล
        "Aerial ability":10, #ล่นบอลกลางอากาศ 	
    }}

p4 = {
    "name":"Rolnado",
    "Pos":"ST",
    "Condition":100,  #ความฟิต
    "Morale":"Poor", #ความมั่นใจ 
    "Experience":5, #ประสบการณ์
    "Technique":{
        "Set Pieces":10, #ลูกตั้งเตะ
        "Crossing":10, #โยนบอลจากริมเส้น
        "Dribbing":15, #เลี้ยงบอล
        "Finishing":10, #การยิงประตู
        "Heading":10, #การโหม่ง
        "Long shots":10, #ยิงไกล
        "Marking":20, #ประกบตัวคู่ต่อสู้
        "Passing":10, #ส่งบอล
        "Tackling":15, #การเข้าปะทะ
        "Technique":10, #ความสามารถเฉพาะตัว
    },
    "Mental":{
        "Aggression":10, #ความรุนแรง
        "Creativity":10, #ความคิดสร้างสรรค์
        "Decisions":10, #การตัดสินใจ
        "Determination":10, #ความมุ่งมั่น
        "Influence":10, #ความเป็นผู้นำ
        "Positioning":20, #การยืนตำแหน่ง
        "Off the ball":11, #หาช่องว่าง
        "Teamwork":10, #เล่นเป็นทีม           
    },"Physical":{
        "Acceleration":10, #การวิ่งออกตัว
        "Aglilty":10, #ความคล่องแคล่ว
        "Balance":10, #สมดุลร่างกาย
        "Jumping":10, #กระโดด
        "Pace":10, #ความเร็วในการวิ่ง
        "Stamina":10, #ความอึด
        "Strength":10, #ความแข็งแกร่ง
    },"Goalkeeping":{
        "Handling":10, #การจับบอล
        "Reflex":10, #การตอบสนอง
        "Kicking":10, #การแตะบอล
        "One on ones":10, #ดวลตัวต่อตัว
        "Rushing out":10, #ออกมาตัดบอล
        "Aerial ability":10, #ล่นบอลกลางอากาศ 	
    }}
