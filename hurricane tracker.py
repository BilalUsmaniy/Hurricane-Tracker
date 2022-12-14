import turtle

def graphical_setup():
    import tkinter
    turtle.setup(965, 600)
    wn = turtle.Screen()
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")
    return t, wn, map_bg_img


def track_storm(filename):
    (t, wn, map_bg_img) = graphical_setup()

    with open(f'data/{filename}.csv', 'r') as oFile:
        lines = [line.strip() for line in oFile.readlines()]
        lines = lines[1:]
        lines = [line.split(',') for line in lines]
        lines = [line[2:5] for line in lines]

    t.penup()
    start = lines[0]

    yStart = start[0]
    xStart = start[1]
    xStart = float(xStart)
    yStart = float(yStart)

    t.hideturtle()
    t.setx(xStart)
    t.sety(yStart)

    elements = len(lines)

    for i in range(elements):
        update = lines[i]
        y = update[0]
        x = update[1]
        cat = update[2]
        cat = int(cat)
        x = float(x)
        y = float(y)

        if cat < 74:
            t.width(1)
            t.pencolor("white")
        elif cat >= 74 and cat <= 95:
            t.width(2)
            t.pencolor("blue")
            t.write("1", font=('Arial', 15, 'normal'))
        elif cat >= 96 and cat <= 110:
            t.width(3)
            t.pencolor("green")
            t.write("2", font=('Arial', 15, 'normal'))
        elif cat >= 110 and cat <= 129:
            t.width(7)
            t.pencolor("yellow")
            t.write("3", font=('Arial', 15, 'normal'))
        elif cat >= 130 and cat <= 156:
            t.width(11)
            t.pencolor("orange")
            t.write("4", font=('Arial', 15, 'normal'))
        elif cat >= 158:
            t.width(15)
            t.pencolor("red")
            t.write("5", font=('Arial', 15, 'normal'))

        i += 3
        t.showturtle()
        t.pendown()
        t.goto(x, y)
    wn.exitonclick()
    return wn, map_bg_img


def main():
    storm_name = ['cindy', 'don', 'emily', 'franklin', 'gert', 'harvey', 'ian', 'irma', 'jose', 'katia', 'lee', 'maria',
                  'nate', 'ophelia']
    filename = input("Select file name: ").lower()
    if filename in storm_name:
        track_storm(filename)
    else:
        print(f'Invalid storm name. Please try again.')
        turtle.Screen().bye()


if __name__ == "__main__":
    main()

