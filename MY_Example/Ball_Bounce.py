import pygame as py
import sys

# ตั้งค่าเริ่มต้น
py.init() #Start pygame

# กำหนดสี
White = (225,225,225)
Red = (225,0,0)
Yellow = (225,211,67)
Black = (0,0,0,0)

# กำหนดขนาดจอ
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

# สร้างจอแสดงผล
screen = py.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
py.display.set_caption("Ball Bounce Game") #Show This Game Name

# กำหนดความเร็วของเกมเฟรม
clock = py.time.Clock()

# กำหนดตำแน่งและความเร็วของลูกบอล
ball_pos = [SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2] #ตำแหน่งเริ่มต้นกลางจอ
ball_speed = [5,5] #ความเร็วในการเคลื่อนที่ แกน(x,y)
ball_radius = 20 # ขนาดรัศมีของลูกบอล

# ลูปของเกม

while True:
    # จัดการกับ Event ต่างๆ เช่นการปิดหน้าต่าง
    for event in py.event.get():
        if event.type == py.QUIT: #ถ้ากดปิดหน้าต่าง
            py.quit() #ปิดเกม
            sys.exit() #ปิดโปรแกรม

#การเคลื่อนที่ของลูกบอล

    ball_pos[0] += ball_speed[0] #change position X
    ball_pos[1] += ball_speed[1] #change position Y

# ตรวจสอบการชนของลูกบอลกับขอบหน้าจอ

    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]  #เปลี่ยนทิศทางในแกน X เมื่อชนกับขอบซ้ายขวา
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]  #เปลี่ยนทิศทางในแกน Y เมื่อชนกับขอบบนล่าง  
  
#เปลี่ยนสีพื้นหลัง    
    screen.fill(Black)

# วาดลูกบอลที่ตำแหน่งปัจจุบัน
    py.draw.circle(screen , Yellow, ball_pos , ball_radius)

#  update display 
    py.display.flip()

#กำหนด freamrate 
    clock.tick(144)
