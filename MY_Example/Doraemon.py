import turtle as tt

# set th screen for draw 
screen = tt.Screen()
screen.bgcolor("white") #set background color

#create the drawing object
dora = tt.Turtle()
dora.speed(5)

#function for drawing circle with color
def draw_circle(color , radius, position) : #set the parameters
    dora.penup() #ยกปากกาขึ้นโดยไม่ทิ้งรอย
    dora.goto(position) #ย้ายไปยังตำแหน่งที่ระบุ
    dora.pendown() #วางปากกาลงเพื่อเริ่มวาด
    dora.begin_fill() #เริ่มต้นระบายสี  
    dora.fillcolor(color) #ตั้งค่าสีที่จะระบาย
    dora.circle(radius) #วาดวงกลมตามขนาด radius ที่กำหนด
    dora.end_fill() #สิ้นสุดการระบายสี

# function for the drawing circle of Doraemon
def draw_head() :
    draw_circle("skyblue", 100, (0,-100)) #วาดส่วนหัวด้วยสีฟ้า

# function for the drawing eyes
def draw_eyes() :
    # left eye
    draw_circle("white", 20, (-35, 35))
    draw_circle("black", 10, (-35, 35))
    # right eye
    draw_circle("white", 20, (35, 35))
    draw_circle("black", 10, (35, 35))

#darw nose
def draw_nose() :
    draw_circle("red", 10, (0 , 7))

#draw mouth

def draw_mouth() :
    dora.penup() #ยกปากกาขึ้น
    dora.goto(-40 , -10) #ย้ายไปตำแหน่งปาก
    dora.pendown() #วางปากกาลง
    dora.setheading(-60) #ตั้งมุมการวาด
    dora.circle(50, 120)

#วาดหนวด
def draw_whisker() :
    whisker_positions = [(-70, -10), (-70 , -30) , (-70 , -50) , (70 , -10), (70 , -30) , (70 , -50)]
    dora.penup() #ยกปากกาขึ้น
    for position in whisker_positions :
        dora.goto(position)
        dora.setheading(0) #กำหนดเป็น 0 องศาทางขวา
        dora.pendown()
        if position[0] < 0:
            dora.backward(20) #หนวดซ้าย
        else: 
            dora.forward(20) #หนวดขวา
        dora.penup() #ยกปากกาขึ้น

draw_head() #ส่วนหัว
draw_eyes() #ตา
draw_nose() #จมูก
draw_mouth() #ปาก
draw_whisker() #หนวด

dora.hideturtle() #ซ่อนตัววาด 
screen.exitonclick() #wait for user click exit