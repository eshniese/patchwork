from graphix import Window, Circle, Rectangle, Polygon, Point, Text

def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.outline_colour = colour
    circle.draw(win)

def draw_rectangle(win, tl, br, colour):
    rectangle = Rectangle(tl,br)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)

def draw_rectangle2(win, tl, br, colour):
    rectangle = Rectangle(tl,br)
    rectangle.fill_colour = colour
    rectangle.outline_colour = "black"
    rectangle.draw(win)

def draw_rectangle3(win, tl, br, border):
    rectangle = Rectangle(tl,br)
    rectangle.fill_colour = ""
    rectangle.outline_colour = "black"
    rectangle.outline_width = border
    rectangle.draw(win)

def patch_1(win, tl, colour):
    screens = 100
    square = 5
    X = tl.x
    Y = tl.y
    for y in range(Y, Y + screens, 100):
        for x in range(X, X + screens, 100):
            for i in range(10):
                # Determine the color based on even/odd number 'i'
                colour_1 = colour if i % 2 == 0 else "white"  # Alternates red and white

                # Draws a rectangle based on parameter starting points
                p1 = Point(X, Y)
                # Gets the point from the loop and adds by the width of the screen then subtracts by space between each square which is then increased after every loop
                p2 = Point(x + screens - square, y + screens - square)

                draw_rectangle(win, p1, p2, colour_1)

                # Increments the co-ordinates after every loop
                X += 5
                Y += 5

                square += 5



def patch_2(win, tl, colour):

    screens = 100
    radius = 5
    X = tl.x
    Y= tl.y

    for y in range(Y, Y + screens, 100):
        for x in range(X, X + screens, 100):

                for y1 in range(Y, Y + screens, 40):
                   for x1 in range(X, X + screens, 100):
                     # Drawing 3 red rectangles
                     p1 = Point(x1, y1)
                     p2 = Point(x1 + screens, y1 + 20)
                     draw_rectangle(win, p1, p2, colour)

                # Drawing white circles on top of red rectangles
                for cx in range(X + 10, X + screens, 20):
                    for cy in range(Y + 10, Y + screens, 40):
                      # Keeps y the same, but loops variables based on parameter positioning inside loop
                      new_centre = Point(cx, cy)
                      draw_circle(win, new_centre, radius, "white")

                
                # Drawing rhombus
                point_lst = [Point(X + 0, Y + 30),Point(X + 10, Y + 20), Point(X + 20, Y + 30), Point(X + 10, Y + 40)]
                for x2 in range(X, X + screens, 40):
                    for y2 in range(Y, X + (screens - 20), 40):
                      new_points = [Point(pt.x + (x2 - X), pt.y + (y2 - Y)) for pt in point_lst]
                      rhombus = Polygon(new_points)
                      rhombus.fill_colour = colour
                      rhombus.outline_colour = colour
                      rhombus.draw(win)
                      


                # 'Colour' and white alternating circles
                center1 = Point(X + 10, Y + 30)
                for x3 in range(center1.x, center1.x + screens, 20):
                    for y3 in (Y + 30, Y + 70):
                        # Keeps y the same, but loops variables based on parameter positioning inside loop
                        new_centre = Point(x3, y3)
                        #Alternates the colour based on the index number in the loop (even or odd)
                        if (x3 // 20 + y3 // 20) % 2 == 0:
                            colour_2 = colour
                        else:
                            colour_2 = "white"
                        draw_circle(win, new_centre, radius, colour_2)


def main():

    screen = 100
    tile = 100
    colour_list = ["red", "blue", "orange", "green", "purple", "magenta"]
    while True:
      size = int(input("Enter the size of the window (Choose between 5, 7, 9): "))
      colour_1 = str(input("Enter 1/3 of your desired colour: "))
      colour_2 = str(input("Enter 2/3 of your desired colour: "))
      colour_3 = str(input("Enter 3/3 of your desired colour: "))

    


      if size in [5, 7, 9]:
         #For all the colours in the colour list, if the colours are in the list...
          if all(colour in colour_list for colour in [colour_1, colour_2, colour_3]):  #Returns True if all elements in statement are True
             win = Window("Patchwork Coursework 2024",screen * size, screen * size)

             display = screen * size

             for y in range(0, display, tile):


                 # Creating the white rectangle grid behind the patchwork
                 for x in range(0, display, tile):
                     p1 = Point(x, y)
                     p2 = Point(x + tile, y + tile)
                     if x ==y:
                        bg_colour = "white"
                     elif  display - 100 >= x >= 100 and display - 100 > y >= 100:
                        bg_colour = colour_3
                     else:
                        bg_colour = "white"
                     draw_rectangle2(win, p1, p2, bg_colour)





                 for x in range(0, display, display - tile):
                    p1 = Point(x, y)
                    p2 = Point(x + tile, y + tile)
                    if (x // 20 + y // 20) % 2 == 0:
                      new_colour = "white"
                    else:
                      new_colour = colour_2

                    draw_rectangle(win, p1, p2, new_colour)


               # Prints every other line of the final patch 'P'
                 for x in range(0, display, tile):

                     if x == y:  # Prints diagonal line (going left to right) of penultimate patch 'F'
                         patch_2(win, Point(x, y), colour_1)
                         if display - 100 >= x >= 100 and  display - 100 > y >= 100:
                          patch_2(win, Point(x, y), colour_3)



                     elif y // tile in [0, 2, 4, 6, 8]:
                         if  display - 100 > x >= 100 and  display - 100 > y > 100:
                             patch1_colour = colour_3
                         elif (x // 20 + y // 20) % 2 == 0:
                             patch1_colour = colour_1
                         else:
                             patch1_colour = colour_2

                         patch_1(win, Point(x, y), patch1_colour)

             #Challenge Feature

             def highlight_patch(point):

                 click = Point((point.x// tile) * tile, (point.y// tile) * tile) #Converts the point to the nearest grid point

                 clickp1 = Point(click.x, click.y)
                 clickp2 = Point(click.x + tile, click.y + tile)
                 border_width = 6
                 draw_rectangle3(win, clickp1, clickp2, border_width)

                 return click   #Returns the coordinates of the bordered patch

             def delete_patch(point):
                 clickp1 = Point(point.x, point.y)
                 clickp2 = Point(point.x + tile, point.y + tile)
                 draw_rectangle2(win, clickp1, clickp2, "white")


             while True:
                click_point = win.get_mouse()
                highlighted_patch = highlight_patch(click_point)

                #If user selects a certain button
                key = win.check_key()
                if key == "X":
                    if highlighted_patch:
                        delete_patch(highlighted_patch)
                if key == "7":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        draw_rectangle(win,Point(click.x, click.y),Point(click.x+ 100, click.y + 100),  colour_1)
                if key == "8":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        draw_rectangle(win,Point(click.x, click.y),Point(click.x+ 100, click.y + 100),  colour_2)
                if key == "9":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        draw_rectangle(win,Point(click.x, click.y),Point(click.x+ 100, click.y + 100),  colour_3)
                if key == "4":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        for x in range(click.x , click.x + tile, tile):
                            for y in range(click.y , click.y + tile, tile):
                               patch_1(win, Point(x,y), colour_1)
                if key == "5":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        for x in range(click.x , click.x + tile, tile):
                            for y in range(click.y , click.y + tile, tile):
                               patch_1(win, Point(x,y), colour_2)
                if key == "6":
                    if highlighted_patch:
                        click = Point((click_point.x // tile) * tile, (click_point.y // tile) * tile)
                        for x in range(click.x , click.x + tile, tile):
                            for y in range(click.y , click.y + tile, tile):
                               patch_1(win, Point(x,y), colour_3)
             win.get_mouse()
             win.close()
             break
          if not all(colour in colour_list for colour in [colour_1, colour_2, colour_3]):
            print("NOTICE: Invalid colour")
      else:
          print("NOTICE: Invalid size")

main()



