# =====================================
# GAME SNAKE SIMPEL MENGGUNAKAN PYTHON
# =====================================

import turtle
import time
import random
import winsound

# Mengatu Kecepatan Ular
delay = 0.1

# Mengatur Score
score = 0
high_score = 0


# Set up Layar
wn = turtle.Screen()
wn.title("Game Snake By pgrl")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)


# Head Snake
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop" # Ular akan diam ditempat sebelum dimainkan

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,120)


# Menyimpan bagian ekor ular , jika ular akan terus bertambah
segments = []


# Pengaturan UI pada bagian Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# Function Arah dan Gerak

def go_up():
    if head.direction != "down": # Fungsinya untuk mencegah agar ular tidak bisa berbalik 180 derajat secara langsung dst.
        head.direction = "up"
    
def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"
            
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Fungis untuk memindahkan ular ke arah sesuai titik koordinat (x dan y)
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) 
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
        
# Fungsi untuk menghubungkan controler ke keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
        
        

# Main game
while True:
    wn.update()
    
    # Memeriksa apakah ular menabrak batas layar (dinding) 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        
        # Sound Menabrak Dinding/Mati
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
        
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Menyembunyikan segmen ekor ke luar layar
        for segment in segments:
            segment.goto(1000, 1000)
            
        # Menghapus memori daftar ekor ular
        segments.clear()
            
        # Reset score 
        score = 0
            
        # Reset delay
        delay = 0.1
        
        # Tampilan Score di Layar
        pen.clear()    
        pen.write("Score: {}  High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    # Ular memakan Makanan nya
    if head.distance(food) < 20:
        
        # Memutar suara efek makan
        winsound.PlaySound("eat.wav", winsound.SND_ASYNC)
        
        # Memindahkan makanan ke tempat random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 200)
        food.goto(x, y)
         
        # Tambahkan Segments Ekor
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape ("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # Mempercepat laju pada game
        delay -= 0.001
        
        # Meningkatkan Score
        score += 10
        
        # Memperbarui High Score jika skor saat ini memecahkan rekor    
        if score > high_score:
            high_score = score
        
        # Tampilan Score di layar
        pen.clear()    
        pen.write("Score: {}  High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    
    # Memindahkan ekor dari urutan paling belakang ke posisi ekor di depannya
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Memindahkan segmen pertama (leher) persis ke posisi kepala ular saat ini
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    #Panggil fungsi move() agar kepala bergerak, lalu ekor (di atas) akan mengikutinya
    move()
    
    # Memeriksa apakah ular menabrak badan nya sendiri
    for segment in segments:
        if segment.distance(head) < 20:
            
            # Sound jika ular menabrak badan nya sendiri/mati
            winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
            
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Menyembunyikan segmen ekor ke luar layar
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Menghapus memori daftar ekor ular
            segments.clear()
            
            # Reset Score
            score = 0
            
            # Reset Delay
            delay = 0.1
        
            pen.clear()    
            pen.write("Score: {}  High Score:  {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
    # Waktu tunda (delay) sebelum loop mengulang dari awal            
    time.sleep(delay)


wn.mainloop()