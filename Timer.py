import pygame, sys, time, random
pygame.display.init()
pygame.init()

# Declaring variables
screen_X = 1000
screen_Y = 800
screen = pygame.display.set_mode((screen_X, screen_Y))
# Declaring variables - rectangles
rectangles_x = [10, 300, 600]
rectangles_y = [60, 200, 400]
rectangles_width = [100, 49, 32]
rectangles_height = [100, 122, 67]
rectangles_red = [255, 193, 42]
rectangles_green = [30, 29, 146]
rectangles_blue = [187, 255, 46]
rectangles_dictionary = [1, 2, 3]
background_color = (0, 0, 0)
# Declaring variables - lines
# Declaring variables - Lines - location
lines_start_x = [90, 400, 26]
lines_start_y = [90, 400, 43]
lines_end_x = [180, 550, 98]
lines_end_y = [180, 600, 87]
# Declaring variables - Lines - apearence
lines_thickness = [3, 1, 2]
lines_color_red = [255, 0, 127]
lines_color_green = [127, 0, 63]
lines_color_blue = [0, 255, 31]
# Declaring variables - Lines - Dictionary
lines_dictionary = [1, 2, 3]
# Declaring variables - Text
# Declaring variables - Text - Fonts
text_fonts = []
# Declaring variables - Text - Text/General
text_text_color = []
text_text_red = [30, 46]
text_text_green = [90, 83]
text_text_blue = [140, 72]
text_text = ["Smwall", "Bw-w-wig"]
text_rendertracking = []
text_backround_red = [None, 47]
text_backround_green = [None, 96]
text_backround_blue = [None, 129]
text_backround_color = []
text_font = ["Fonts/Arial Unicode.ttf", "Fonts/Arial Unicode.ttf"]
text_size = [20, 20]
text_rect = []
text_dictionary = [1, 2]
font_name = ["Arial"]
font_location = ["Fonts/Arial Unicode.ttf"]
text_X = [200, 476]
text_Y = [200, 369]
# Declaring variables - Timers
Gametick = 0
Timestart = time.time()
lineDeltimer = [None, None, None]
rectDeltimer = [None, None, None]
# Declaring variables - Events
upcomingeventtimes = []
eventfunction = []
eventfunctionargs = []
eventtitles = []
# Declaring variables - Msc
dellinelater = []
fps = 60
Clock = pygame.time.Clock()
rectangles_color = []
lines_color = []
Window_title = "Timer app"


# defining functions
def getFontViaName(Name):
    return(font_location[font_name.index(Name)])


def gettimein(wait):
    return (time.time() - Timestart) + wait


def getRectIndexViaDict(DictID):
    try:
        return rectangles_dictionary.index(DictID)
    except ValueError:
        return -1


def getLineIndexViaDict(DictID):
    try:
        return lines_dictionary.index(DictID)
    except ValueError:
        return -1


def getTextIndexViaDict(DictID):
    try:
        return text_dictionary.index(DictID)
    except ValueError:
        return -1


def delLine(DictID):
    global lineDeltimer, lines_thickness, lines_color, lines_color_red, lines_color_green, lines_color_blue, lines_start_x, lines_start_y, lines_end_x, lines_end_y
    try:
        del lineDeltimer[getLineIndexViaDict(DictID)]
        del lines_thickness[getLineIndexViaDict(DictID)]
        del lines_color[getLineIndexViaDict(DictID)]
        del lines_color_red[getLineIndexViaDict(DictID)]
        del lines_color_green[getLineIndexViaDict(DictID)]
        del lines_color_blue[getLineIndexViaDict(DictID)]
        del lines_start_x[getLineIndexViaDict(DictID)]
        del lines_start_y[getLineIndexViaDict(DictID)]
        del lines_end_x[getLineIndexViaDict(DictID)]
        del lines_end_y[getLineIndexViaDict(DictID)]
        del lines_dictionary[getLineIndexViaDict(DictID)]
    except IndexError:
        return None


def delRect(DictID):
    global rectangles_x, rectangles_y, rectangles_red, rectangles_green, rectangles_blue, rectangles_width, rectangles_height, rectangles_color, rectangles_dictionary
    try:
        del rectangles_x[getRectIndexViaDict(DictID)]
        del rectangles_y[getRectIndexViaDict(DictID)]
        del rectangles_red[getRectIndexViaDict(DictID)]
        del rectangles_green[getRectIndexViaDict(DictID)]
        del rectangles_blue[getRectIndexViaDict(DictID)]
        del rectangles_color[getRectIndexViaDict(DictID)]
        del rectangles_height[getRectIndexViaDict(DictID)]
        del rectangles_width[getRectIndexViaDict(DictID)]
        del rectangles_dictionary[getRectIndexViaDict(DictID)]
    except IndexError:
        return None


def delText(DictID):
    global text_text, text_rect, text_rendertracking, text_fonts, text_backround_red, text_backround_green, text_backround_blue, text_text_red, text_text_green, text_text_blue, text_dictionary, text_X, text_Y
    try:
        del text_rect[getTextIndexViaDict(DictID)]
        del text_text[getTextIndexViaDict(DictID)]
        del text_rendertracking[getTextIndexViaDict(DictID)]
        del text_fonts[getTextIndexViaDict(DictID)]
        del text_backround_green[getTextIndexViaDict(DictID)]
        del text_backround_red[getTextIndexViaDict(DictID)]
        del text_backround_blue[getTextIndexViaDict(DictID)]
        del text_text_color[getTextIndexViaDict(DictID)]
        del text_text_red[getTextIndexViaDict(DictID)]
        del text_text_green[getTextIndexViaDict(DictID)]
        del text_text_blue[getTextIndexViaDict(DictID)]
        del text_dictionary[getTextIndexViaDict(DictID)]
        del text_X[getTextIndexViaDict(DictID)]
        del text_Y[getTextIndexViaDict(DictID)]
    except IndexError:
        return None

def delEvent(Index):
    global eventfunction, eventfunctionargs, upcomingeventtimes, eventtitles
    del eventfunctionargs[Index]
    del eventfunction[Index]
    del upcomingeventtimes[Index]
    del eventtitles[Index]


def lineDelIn(activationpoint, DictID):
    makeevent(activationpoint, delLine, DictID, "lineDelIn function")


def rectDelin(activationpoint, DictID):
    makeevent(activationpoint, delRect, DictID, "rectDelIn function")


def runfunc(function, args):
    if type(args) == tuple or type(args) == list:
        function(*args)
    elif type(args) == str or type(args) == int:
        function(args)
    else:
        return False


def makeevent(acvtivationpoint, function, functionarguments, title):
    global eventfunction, eventfunctionargs, upcomingeventtimes
    eventfunction.append(function)
    eventfunctionargs.append(functionarguments)
    upcomingeventtimes.append(acvtivationpoint)
    eventtitles.append(title)


def drawRect(X, Y, Width, Height, Color):
    global rectangles_height, rectangles_width, rectangles_x, rectangles_y, rectangles_red, rectangles_green, rectangles_blue, rectangles_dictionary
    rectangles_width.append(Width)
    rectangles_height.append(Height)
    rectangles_x.append(X)
    rectangles_y.append(Y)
    rectangles_red.append(Color[0])
    rectangles_green.append(Color[1])
    rectangles_blue.append(Color[2])
    try:
        rectangles_dictionary.append(rectangles_dictionary[-1] + 1)
    except:
        rectangles_dictionary.append(1)
    return(rectangles_dictionary[-1])


def editRect(DictID, X = None, Y = None, Width = None, Height = None, Color = None):
    if X != None:
        global rectangles_x
        rectangles_x[getRectIndexViaDict(DictID)] = X
    if Y != None:
        global rectangles_y
        rectangles_y[getRectIndexViaDict(DictID)] = Y
    if Width != None:
        global rectangles_width
        rectangles_width[getRectIndexViaDict(DictID)] = Width
    if Height != None:
        global rectangles_height
        rectangles_height[getRectIndexViaDict(DictID)] = Height
    if Color != None:
        global rectangles_red, rectangles_green, rectangles_blue
        rectangles_red[getRectIndexViaDict(DictID)] = Color[0]
        rectangles_green[getRectIndexViaDict(DictID)] = Color[1]
        rectangles_blue[getRectIndexViaDict(DictID)] = Color[2]


def editLine(Index, start_X = None, start_Y = None, end_X = None, end_Y = None, thickness = None, color = None):
    if start_X != None:
        global lines_start_x
        lines_start_x[Index] = start_X
    if start_Y != None:
        global lines_start_y
        lines_start_y[Index] = start_Y
    if end_X != None:
        global lines_end_x
        lines_end_x[Index] = end_X
    if end_Y != None:
        global lines_end_y
        lines_end_y[Index] = end_Y
    if thickness != None:
        global lines_thickness
        lines_thickness = thickness
    if color != None:
        global lines_color_red, lines_color_green, lines_color_blue
        lines_color_red[Index] = color[0]
        lines_color_green[Index] = color[1]
        lines_color_blue[Index] = color[2]


def editText(DictID, Text = None, X = None, Y = None, Font = None, Font_Size = None, Color = None, Background_Color = None):
    try:
        if Text != None:
            global text_text
            text_text[getTextIndexViaDict(DictID)] = Text
        if X != None:
            global text_X
            text_X[getTextIndexViaDict(DictID)] = X
        if Y != None:
            global text_Y
            text_Y[getTextIndexViaDict(DictID)] = Y
        if Font != None:
            global text_font
            text_font.append(Font)
        if Font_Size != None:
            global text_size
            text_size.append(Font_Size)
        if Color != None:
            global text_text_red, text_text_green, text_text_blue
            text_text_red[getTextIndexViaDict(DictID)] = Clock[0]
            text_text_green[getTextIndexViaDict(DictID)] = Color[1]
            text_text_blue[getTextIndexViaDict(DictID)] = Color[2]
        if Background_Color != None:
            global text_backround_red, text_backround_green, text_backround_blue
            text_backround_red[getTextIndexViaDict(DictID)] = Background_Color[0]
            text_backround_green[getTextIndexViaDict(DictID)] = Background_Color[1]
            text_backround_blue[getTextIndexViaDict(DictID)] = Background_Color[2]
    except IndexError:
        print("editText error")


def timerloop(percentage, total_time, DictID, full_rect_width, title):
    title_new = str(title) + "iteration" + str(percentage)
    if percentage >= 100:
        drawText("Arial", 20, rectangles_x[getRectIndexViaDict(DictID)], rectangles_y[getRectIndexViaDict(DictID)], "Timer \"" + str(title) + "\" complete!", None, (255, 255, 255))
        delRect(DictID)
    else:
        editRect(DictID=DictID, Width=full_rect_width * (percentage / 100))
        makeevent(total_time * (percentage / 100), timerloop, (percentage + 1, total_time, DictID, full_rect_width, title), title_new)


def maketimerloop(rect_x, rect_y, starting_rect_width, full_rect_width, rect_height, rect_color, end_time, Title):
    rectdict = drawRect(rect_x, rect_y, starting_rect_width, rect_height, rect_color)
    makeevent(time.time() - Timestart, timerloop, (0, end_time - (time.time() - Timestart), rectdict, full_rect_width, Title), Title)


def drawLine(SX, SY, EX, EY, Color, Thick):
    global lines_thickness, lines_start_x, lines_start_y, lines_end_x, lines_end_y, lines_color_red, lines_color_green, lines_color_blue
    lines_thickness.append(Thick)
    lines_start_x.append(SX)
    lines_end_x.append(EX)
    lines_start_y.append(SY)
    lines_end_y.append(EY)
    lines_color_red.append(Color[0])
    lines_color_green.append(Color[1])
    lines_color_blue.append(Color[2])
    lineDeltimer.append(None)
    try:
        lines_dictionary.append(lines_dictionary[-1] + 1)
    except IndexError:
        lines_dictionary.append(1)
    return lines_dictionary[-1]


def drawText(Font, Font_Size, X, Y, Text, Backround_Color, Color):
    global text_fonts, text_text, text_dictionary, text_X, text_Y, text_backround_red, text_backround_green, text_backround_blue
    text_font.append(getFontViaName(Font))
    text_size.append(Font_Size)
    text_text.append(Text)
    try:
        text_dictionary.append(text_dictionary[-1] + 1)
    except IndexError:
        text_dictionary.append(1)
    text_X.append(X)
    text_Y.append(Y)
    if Backround_Color == None:
        text_backround_red.append(None)
        text_backround_green.append(None)
        text_backround_blue.append(None)
    else:
        text_backround_red.append(Backround_Color[0])
        text_backround_green.append(Backround_Color[1])
        text_backround_blue.append(Backround_Color[2])
    text_text_red.append(Color[0])
    text_text_green.append(Color[1])
    text_text_blue.append(Color[2])
    return(text_dictionary[-1])


def drawOutline_Line(X, Y, Width, Height, Thickness, Color):
    indexs = []
    indexs.append(drawLine(X, Y, X + Width, Y, Color, Thickness))
    indexs.append(drawLine(X, Y, X, Y + Height, Color, Thickness))
    indexs.append(drawLine(X + Width, Y + Height, X, Y + Height, Color, Thickness))
    indexs.append(drawLine(X + Width, Y + Height, X + Width, Y, Color, Thickness))
    return indexs


def random_add_line_or_rectangle(globchance):
    global rectangles_height, rectangles_width, rectangles_x, rectangles_y, rectangles_red, rectangles_green, rectangles_blue, lines_thickness, lines_color_blue, lines_color_green, lines_color_red, lines_end_x, lines_end_y, lines_start_y, lines_start_x
    lines_start_x.append(random.randint(1, screen_X))
    lines_start_y.append((random.randint(1, screen_Y)))
    lines_color_red.append(random.randint(0, 255))
    lines_color_green.append(random.randint(0, 255))
    lines_color_blue.append(random.randint(0, 255))
    lines_end_x.append(random.randint(1, screen_X))
    lines_end_y.append(random.randint(1, screen_Y))
    lines_thickness.append(random.randint(1, 15))
    lineDeltimer.append(None)


def getCollidingWithRect(Coords, DictID):
    try:
        if Coords[0] >= rectangles_x[getRectIndexViaDict(DictID)] and Coords[1] >= rectangles_y[getRectIndexViaDict(DictID)] and Coords[0] <= rectangles_x[getRectIndexViaDict(DictID)] + rectangles_width[getRectIndexViaDict(DictID)] and Coords[1] <= rectangles_y[getRectIndexViaDict(DictID)] + rectangles_height[getRectIndexViaDict(DictID)]:
            return True
        else:
            return False
    except IndexError:
        return False


def getRectLeftClicked(DictID):
    if pygame.mouse.get_pressed(num_buttons=3)[0] and getCollidingWithRect(pygame.mouse.get_pos(), DictID):
        return True
    else:
        return False



def getRectRightClicked(DictID):
    if pygame.mouse.get_pressed(num_buttons=3)[2] and getCollidingWithRect(pygame.mouse.get_pos(), DictID):
        return True
    else:
        return False


drawText("Arial", 30, 0, 0, "TEST, WORK NOW!", None, (255, 255, 255))
makeevent(gettimein(3), print, "awooga", "test")
makeevent(gettimein(10), drawRect, (400, 400, 400, 400, (255, 0, 255)), "test for draw rect w/ event")
maketimerloop(30, 30, 0, 300, 100, (0, 255, 0), gettimein(7), "Test timer")
maketimerloop(30, 30, 0, 300, 100, (0, 255, 0), gettimein(7), "Test timer")
makeevent(gettimein(2), editText, (1, "edited"), "edittesting")

# Game loop:
while (True):
    pygame.display.set_caption(Window_title)
    screen.fill(background_color)
    Clock.tick(fps)
    Gametick += 1
    rectangles_color = []
    lines_color = []
    text_text_color = []
    text_rendertracking = []
    text_backround_color = []
    text_rect = []
    text_fonts = []
    for i in range(len(rectangles_blue)):
        rectangles_color.append((rectangles_red[i], rectangles_green[i], rectangles_blue[i]))
    for i in range(len(lines_color_blue)):
        lines_color.append((lines_color_red[i], lines_color_green[i], lines_color_blue[i]))
    for i in range(len(text_text)):
        text_text_color.append((text_text_red[i], text_text_green[i], text_text_blue[i]))
    for i in range(len(text_backround_red)):
        if text_backround_red[i] == None:
            text_backround_color.append(None)
        else:
            text_backround_color.append((text_backround_red[i], text_backround_green[i], text_backround_blue[i]))
    for i in range(len(text_font)):
        text_fonts.append(pygame.font.Font(text_font[i], text_size[i]))
    for i in range(len(text_text)):
        text_rendertracking.append(text_fonts[i].render(text_text[i], True, text_text_color[i], text_backround_color[i]))
    for i in range(len(text_rendertracking)):
        text_rect.append(text_rendertracking[i].get_rect())
    for i in range(len(text_rect)):
        text_rect[i].topleft = (text_X[i], text_Y[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    for i in range(len(text_rendertracking)):
        screen.blit(text_rendertracking[i], text_rect[i])
    for i in range(len(rectangles_x)):
        pygame.draw.rect(screen, rectangles_color[i], pygame.Rect(rectangles_x[i], rectangles_y[i], rectangles_width[i], rectangles_height[i]))
    for i in range(len(lines_thickness)):
        pygame.draw.line(screen, lines_color[i], (lines_start_x[i], lines_start_y[i]), (lines_end_x[i], lines_end_y[i]),lines_thickness[i])
    for i in range(len(upcomingeventtimes) -1, -1, -1):
        if upcomingeventtimes[i] < time.time() - Timestart:
            runfunc(eventfunction[i], eventfunctionargs[i])
            delEvent(i)
    pygame.display.flip()