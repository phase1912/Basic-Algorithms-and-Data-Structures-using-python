import turtle

def draw_branch(t, branch_length, angle, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    t.right(2 * angle)
    draw_branch(t, branch_length * 0.7, angle, level - 1)

    t.left(angle)
    t.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії (рекомендується 5-10): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Фрактал: Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_branch(t, 100, 30, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()