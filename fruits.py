import stddraw
import picture
#THIS MODULE IS MADE FOR: p2-taffy.py 

stddraw.setXscale(-16.0, 16.0)
stddraw.setYscale(-22.0, 25.0)

def pic1(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic1.png"), x, y)
    stddraw.show(0.0)

def pic2(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic2.png"), x, y)
    stddraw.show(0.0)

def pic3(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic3.png"), x, y)
    stddraw.show(0.0)

def pic4(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic4.png"), x, y)
    stddraw.show(0.0)

def pic5(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic5.png"), x, y)
    stddraw.show(0.0)

def pic6(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\pic6.png"), x, y)
    stddraw.show(0.0)

def picwhite(x, y):
    stddraw.picture(picture.Picture("picsfortaffytangle\picwhite.png"), x, y)
    stddraw.show(0.0)

#pictures were from https://www.pinterest.ca/pin/204632376798360136/ or https://goo.gl/images/9QCGoH then I cropped it and made the background transparent with http://resizeimage.net/ found website from piazza

#drawing a not filled box 
def draw_box(x, y):
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.setPenRadius(0.005)
    stddraw.square(x, y, 2.0)
    stddraw.show(50.0)
#clearing the not filled box (draw a not filled white square)
def clear_box(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setPenRadius(0.005)
    stddraw.square(x, y, 2.0)
    stddraw.show(50.0)

#draw a filled white square
def clear_taffy(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setPenRadius(0.005)
    stddraw.filledSquare(x, y, 1.5)
    stddraw.show(20.0)

#detecting if there was a mouse click
def mouse_pressed():
    if stddraw.mousePressed():
        return True

#finding the coordinates of the mouse click
def mouse_coordinates():
    mx=stddraw.mouseX()
    my=stddraw.mouseY()
    return mx, my

#show 
def show_time(time):
    stddraw.show(time)

def player_score(score):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(-9.5, 20.0, "Current Score:")
    stddraw.setPenColor(stddraw.DARK_GREEN)
    stddraw.text(-5.5, 20.0, str(score))

def moves_remaining(moves):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(4.5, 20.0, "Moves Remaining:")
    stddraw.setPenColor(stddraw.DARK_BLUE)
    stddraw.text(9.5, 20.0, str(moves))

def clear_message(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setPenRadius(0.005)
    stddraw.filledRectangle(x, y, 12.0, 3.0)

def need_to_reach(target):
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(-9.6, 23.0, "Target Score: ")
    stddraw.setPenColor(stddraw.BOOK_RED)
    stddraw.text(-6.0, 23, str(target))

def show_forever():
    stddraw.show()

def win_message():
    stddraw.clear()
    stddraw.setPenColor(stddraw.PINK)
    stddraw.setFontSize(50)
    stddraw.text(0.0, 2.0, "You WON!!")

def lose_message():
    stddraw.clear()
    stddraw.setPenColor(stddraw.DARK_RED)
    stddraw.setFontSize(50)
    stddraw.text(0.0, 2.0, "Sorry you lost!")