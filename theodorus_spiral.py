import turtle
import math

scale = 40  # هر واحد = 40 پیکسل
# Each unit = 40 pixels

# درخواست تعداد مراحل از کاربر
n = int(input("Enter the number of steps (n ≥ 2): "))
# Ask the user for number of steps

if n < 2:
    print("n must be at least 2")
    turtle.done()
    exit()

t = turtle.Turtle()
t.speed(1)
t.width(2)
turtle.colormode(255)
turtle.tracer(1, 10)

# نقطه شروع
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)  # افقی راست
# Starting point
# Facing right horizontally

# ----------------------
# رسم مثلث قائم‌الزاویه 1x1
# Draw a 1x1 right triangle
# ----------------------
# ضلع افقی (قاعده)
t.forward(scale)
# Horizontal side (base)

# ضلع قائم
t.left(90)
t.forward(scale)
# Vertical side

current_pos = t.position()
t.goto(0, 0)
# Move back to origin
# وتر
# Hypotenuse
for i in range(2, n):
    t.goto(current_pos)
    t.pendown()

    angle = 90 - math.degrees(math.atan(math.sqrt(i-1)))
    print(f"مرحله {i}: زاویه = {angle}")
    # Step {i}: angle = {angle}

    # -------- رنگ تدریجی --------
    # Gradually changing color
    ratio = i / n
    r = int(255 * ratio)
    g = 50
    b = int(255 * (1 - ratio))
    t.pencolor(r, g, b)
    # ----------------------

    t.left(angle)
    t.forward(scale)
    current_pos = t.position()

    t.goto(0, 0)

    # ---------- نوشتن رادیکال ----------
    # Write square root
    t.penup()
    t.goto(current_pos[0] + 5, current_pos[1] + 5)
    t.write(f"\u221a{i+1}", font=("Arial", 10, "normal"))
    t.penup()
    # -----------------------------------

# پایان
turtle.done()
# End
