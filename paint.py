#Sartaj Sidhu Paintprogram
#theme was Fortnite ( a video game)
#features- scroll to change size, spray paint, outline what tool is being used, eyedropper, no dots in unfilled circle, breif summary of each tool
#attention to detail- everything is lined up properly and everything is the them colours (white,black,purple), big canvas
#------------------------------------------------------------------------------------
#imports
from pygame import*
from random import *
from getname import*
screen=display.set_mode((1024,768)) #display 768
display.set_caption("Fortnite Paint!")
font.init()
                               # must have this in your program for my font to work

comicFont = font.SysFont("Comic Sans MS", 20)
#------------------------------------------------------------------------------------
#loads in all the images
Cpalette        =image.load("Tools/colour.png")     #colour palette image
pencilimage     =image.load("Tools/Pencil.png")     #pencil tool image
eraserimage     =image.load("Tools/eraser.png")     #eraser tool image
spraypaintimage =image.load("Tools/Spraypaint.png") #spray paint tool image
bucketimage     =image.load("Tools/Bucket.png")     #fill tool image
circleimage     =image.load("Tools/Circle.jpg")     #filled circle image
UFcircleimage   =image.load("Tools/UFcircle.png")   #unfilled circle image
brushimage      =image.load("Tools/Brush.png")      #Paint brush image
lineimage       =image.load("Tools/Line.png")       #line image
saveimage       =image.load("Tools/save.png")
loadimage       =image.load("Tools/load.png")
dropimage       =image.load("Tools/Drop.png")
oneimage        =image.load("Tools/one.png")
twoimage        =image.load("Tools/two.png")
threeimage      =image.load("Tools/3.jpg")

penciltxt       =image.load("Txt/penciltxt.png")
brushtxt        =image.load("Txt/brushtext.png")
buckettxt       =image.load("Txt/buckettext.png")
circletxt       =image.load("Txt/circletext.png")
UFcircletxt     =image.load("Txt/UFcircletext.png")
recttxt         =image.load("Txt/recttext.png")
UFrecttxt       =image.load("Txt/UFrecttext.png")
linetxt         =image.load("Txt/linetext.png")
spraytxt        =image.load("Txt/spraytext.png")
erasertxt       =image.load("Txt/erasertext.png")
droptxt         =image.load("Txt/droptext.png")
loadtxt         =image.load("Txt/loadtext.png")
savetxt         =image.load("Txt/savetext.png")
stampstxt       =image.load("Txt/stampstext.png")

backround       =image.load("backrounds/3.jpg")
title           =image.load("backrounds/Title.png")
paint           =image.load("backrounds/Paint.png")
Icon            =image.load("backrounds/Icon.png")

Dragondisplay   =image.load("stamps/DragonDisplay.png")
dragon          =image.load("stamps/Dragon.png")
striker         =image.load("stamps/Striker.png")
strikerdisplay  =image.load("stamps/StrikerDisplay.png")
ramirez         =image.load("stamps/Ramirez.png")
ramirezdisplay  =image.load("stamps/Ramirezdisplay.png")
axe             =image.load("stamps/Future.png")
yglider         =image.load("stamps/yellowglider.png")
electric        =image.load("stamps/Electric.png")
ogglider        =image.load("stamps/Ogglider.png")
sythe           =image.load("stamps/reaper.png")
umbrella        =image.load("stamps/Umbrella.png")
#------------------------------------------------------------------------------------
#colours and screen
screen.fill(((211,211,211)))
white=(255,255,255)
black=(0,0,0)
purple=(180,10,241)
col=(0,0,0)
col2=(0,0,0)
#------------------------------------------------------------------------------------
#Important variables
Psize=2 #line size variable
Tsize=10 #circle size variable
tool="pencil" #tool variable
stamps="one" #stamps variable
stamp=""#stamp being used variable
outline="pencil"#outline variable
startx,starty=(0,0)
lastx,lasty=(0,0)
running=True

#------------------------------------------------------------------------------------
#blitting backround and other important images
display.set_icon(Icon)
screen.blit(backround,(0,0))
#------------------------------------------------------------------------------------
#these are are the rectangles


canvas=Rect(10,11,799,524)              #Big ones
palette=Rect(817,535,201,228)

pencilrect  =Rect(960,185,50,50)        #First column
droprect    =Rect(960,255,50,50)
eraserrect  =Rect(960,325,50,50)
sprayrect   =Rect(960,395,50,50)
colrect     =Rect(960,465,50,50)

brushrect   =Rect(890,185,50,50)        #Second column
saverect    =Rect(890,255,50,50)
linerect    =Rect(890,325,50,50)
bucketrect  =Rect(890,395,50,50)
col2rect    =Rect(890,465,50,50)

UFcirclerect=Rect(820,185,50,50)        #Third column
loadrect    =Rect(820,255,50,50)
circlerect  =Rect(820,325,50,50)
UFrect      =Rect(820,395,50,50)
rectrect    =Rect(820,465,50,50)

dragonrect  =Rect(10,550,150,200)      #stamps
strikerrect =Rect(170,550,150,200)
ramirezrect =Rect(330,550,150,200)


textrect    =Rect(550,560,257,180)  #stamps rect
onerect     =Rect(490,550,50,50)
tworect     =Rect(490,625,50,50)
threerect   =Rect(490,700,50,50)
#------------------------------------------------------------------------------------
#drawing all the rectangles that go behind the images representing the tool

draw.rect(screen,white,canvas)      #canvas
draw.rect(screen,white,palette)     #colour palette
draw.rect(screen,white,pencilrect)  #pencil
draw.rect(screen,white,eraserrect)  #eraser
draw.rect(screen,white,sprayrect)   #spraypaint
draw.rect(screen,white,bucketrect)  #bucketrect
draw.rect(screen,white,colrect)     #colour rect
draw.rect(screen,white,col2rect)    #colour2 rect
draw.rect(screen,white,rectrect)    #Filled Rectangle rect
draw.rect(screen,white,UFrect)      #unfilled rectangle rect
draw.rect(screen,white,circlerect)  #filled circle rect
draw.rect(screen,white,UFcirclerect)#unfilled circle rect
draw.rect(screen,white,linerect)    #line rect
draw.rect(screen,white,brushrect)   #brush rect
draw.rect(screen,white,saverect)    #saverect
draw.rect(screen,white,loadrect)    #loadrect
draw.rect(screen,white,droprect)    #droprect
draw.rect(screen,white,onerect)
draw.rect(screen,white,tworect)
draw.rect(screen,white,threerect)
draw.rect(screen,white,textrect)



#------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------
#blits the images ontop of their rectangles
screen.blit(pencilimage,(960,185))      #first row
screen.blit(brushimage,(890,185))
screen.blit(UFcircleimage,(826,191))                # different than others because picture size was different according to the shape

screen.blit(loadimage,(821,255))
screen.blit(saveimage,(890,255))
screen.blit(dropimage,(960,255))

screen.blit(lineimage,(890,325))        #second row
screen.blit(eraserimage,(960,325))
screen.blit(circleimage,(820,325))

screen.blit(spraypaintimage,(960,395))  #third row
screen.blit(bucketimage,(890,395))
draw.rect(screen,black,(832,405,25,30),2)           #drawing a rectangles for the rectangle tools (kind of like the image that shows what tool it is)

draw.rect(screen,black,(832,475,25,30))             #drawing a rectangles for the rectangle tools (kind of like the image that shows what tool it is)


screen.blit(Cpalette,(817,535))

screen.blit(Dragondisplay,(10,550))     #stamps
screen.blit(ramirezdisplay,(330,550))
screen.blit(strikerdisplay,(170,550))

screen.blit(title,(820,11))
screen.blit(paint,(840,101))


screen.blit(oneimage,(490,550))
screen.blit(twoimage,(490,625))
screen.blit(threeimage,(490,700))


while running:
    click = False
    for e in event.get():
        if e.type ==QUIT:
            running = False

        if e.type==MOUSEBUTTONDOWN:

            Scopy=screen.copy() #getting a copy of the screen so that when you use stamps or shapes the work stays on the canvas that has already been done
            screen.blit(Scopy,(0,0))
            if e.button==1 or e.button==3:
                startx,starty =e.pos

            if e.button == 4:       #if the mouse scroller is scrolled up it increases the size of a tool
                Psize+=1
                Tsize+=1

            if e.button == 5:       #if the mouse scroller is scrolled down it decreases the size of a tool
                Psize-=1
                Tsize-=1




#------------------------------------------------------------------------------------
#mouse position and button varible

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

#------------------------------------------------------------------------------------
#drawing the colour boxes
    draw.rect(screen,col,(897.7,473,36,36))
    draw.rect(screen,col2,(967.7,473,36,36))
#------------------------------------------------------------------------------------
#drawing the beggining outlines
    draw.rect(screen,black,pencilrect,3)
    draw.rect(screen,black,eraserrect,3)
    draw.rect(screen,black,palette,3)
    draw.rect(screen,black,sprayrect,3)
    draw.rect(screen,black,canvas,3)
    draw.rect(screen,black,bucketrect,3)
    draw.rect(screen,black,colrect,3)
    draw.rect(screen,black,col2rect,3)
    draw.rect(screen,black,rectrect,3)
    draw.rect(screen,black,UFrect,3)
    draw.rect(screen,black,circlerect,3)
    draw.rect(screen,black,UFcirclerect,3)
    draw.rect(screen,black,linerect,3)
    draw.rect(screen,black,brushrect,3)
    draw.rect(screen,black,saverect,3)
    draw.rect(screen,black,loadrect,3)
    draw.rect(screen,black,droprect,3)
    draw.rect(screen,black,dragonrect,3)
    draw.rect(screen,black,strikerrect,3)
    draw.rect(screen,black,ramirezrect,3)
    draw.rect(screen,black,onerect,3)
    draw.rect(screen,black,tworect,3)
    draw.rect(screen,black,threerect,3)
    draw.rect(screen,black,textrect,3)

#------------------------------------------------------------------------------------
#size restrictions

    if Psize >= 5:      #doesnt let the  Psize go over 4 so that the pencil doesnt look choppy and so that the unfilled rect/circle dont look weird
        Psize=4
    if Psize <= 0:      #doesnt let the pencil size go negative or 0
        Psize=1
    if Tsize <= 0:      #doesnt let the tool size go negative or 0
        Tsize=1

#------------------------------------------------------------------------------------
#colour pallete being used
    if mb[0]==1 and palette.collidepoint(mx,my):            #checks if mouse on colour pallete and saves that colour as col
        draw.rect(screen,purple,palette,3)
        draw.rect(screen,purple,colrect,3)
        col=screen.get_at((mx,my))


    if mb[2]==1 and palette.collidepoint(mx,my):            #checks if mouse on colour pallete and saves that colour as col
        draw.rect(screen,purple,palette,3)
        draw.rect(screen,purple,col2rect,3)
        col2=screen.get_at((mx,my))


#------------------------------------------------------------------------------------
#choose tools and outlines
    if mb[0]==1 and eraserrect.collidepoint(mx,my):
        tool="eraser"
        outline="eraser"
    if mb[0]==1 and pencilrect.collidepoint(mx,my):
        tool="pencil"
        outline="pencil"
    if mb[0]==1 and sprayrect.collidepoint(mx,my):
        tool="spray"
        outline="spray"
    if mb[0]==1 and bucketrect.collidepoint(mx,my):
        tool="bucket"
        outline="bucket"
    if mb[0]==1 and rectrect.collidepoint(mx,my):
        tool="rect"
        outline="rect"
    if mb[0]==1 and UFrect.collidepoint(mx,my):
        tool="UFrect"
        outline="UFrect"
    if mb[0]==1 and UFcirclerect.collidepoint(mx,my):
        tool="UFcircle"
        outline="UFcircle"
    if mb[0]==1 and circlerect.collidepoint(mx,my):
        tool="circle"
        outline="circle"
    if mb[0]==1 and linerect.collidepoint(mx,my):
        tool="line"
        outline="line"
    if mb[0]==1 and brushrect.collidepoint(mx,my):
        tool="brush"
        outline="brush"
    if mb[0]==1 and saverect.collidepoint(mx,my):
        tool="save"
        outline="save"
    if mb[0]==1 and loadrect.collidepoint(mx,my):
        tool="load"
        outline="load"
    if mb[0]==1 and droprect.collidepoint(mx,my):
        tool="drop"
        outline="drop"
    if mb[0]==1 and dragonrect.collidepoint(mx,my) and stamps=="one":
        tool="ninja"
        stamp=""
        outline="ninja"
    if mb[0]==1 and strikerrect.collidepoint(mx,my)and stamps=="one":
        tool="striker"

        outline="striker"
    if mb[0]==1 and ramirezrect.collidepoint(mx,my)and stamps=="one":
        tool="ramirez"

        outline="ramirez"
    if mb[0]==1 and dragonrect.collidepoint(mx,my)and stamps=="two":
        tool="electric"

        outline="ninja"
    if mb[0]==1 and strikerrect.collidepoint(mx,my)and stamps=="two":
        tool="sythe"

        outline="ramirez"
    if mb[0]==1 and ramirezrect.collidepoint(mx,my)and stamps=="two":
        tool="axe"

        outline="striker"
    if mb[0]==1 and dragonrect.collidepoint(mx,my)and stamps=="three":
        tool="yglider"

        outline="ninja"
    if mb[0]==1 and strikerrect.collidepoint(mx,my)and stamps=="three":
        tool="umbrella"

        outline="ramirez"
    if mb[0]==1 and ramirezrect.collidepoint(mx,my)and stamps=="three":
        tool="ogglider"

        outline="striker"
    if mb[0]==1 and onerect.collidepoint(mx,my):
        stamps="one"
    if mb[0]==1 and tworect.collidepoint(mx,my):
        stamps="two"
    if mb[0]==1 and threerect.collidepoint(mx,my):
        stamps="three"
#------------------------------------------------------------------------------------
#blitting the text for describing the tool
    if tool=="pencil":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(penciltxt,(555,570))
    if tool=="eraser":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(erasertxt,(555,570))
    if tool=="bucket":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(buckettxt,(555,570))
    if tool=="line":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(linetxt,(555,570))
    if tool=="circle":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(circletxt,(555,570))
    if tool=="rect":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(recttxt,(555,570))
    if tool=="spray":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(spraytxt,(555,570))
    if tool=="drop":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(droptxt,(555,570))
    if tool=="UFrect":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(UFrecttxt,(555,570))
    if tool=="UFcircle":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(UFcircletxt,(555,570))
    if tool=="save":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(savetxt,(555,570))
    if tool=="load":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(loadtxt,(555,570))
    if tool=="ogglider" or tool=="yglider" or tool=="umbrella" or tool=="axe" or tool=="electric" or tool=="sythe" or tool=="ninja"or tool=="ramirez" or  tool=="striker":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(stampstxt,(555,570))
    if tool=="brush":
        draw.rect(screen,white,textrect)
        draw.rect(screen,black,textrect,3)
        screen.blit(brushtxt,(555,570))
#------------------------------------------------------------------------------------
#drawing the outlines on the stamp buttons
    if stamps=="one":
      draw.rect(screen,purple,onerect,3)
    if stamps=="two":
      draw.rect(screen,purple,tworect,3)
    if stamps=="three":
      draw.rect(screen,purple,threerect,3)




#------------------------------------------------------------------------------------
#checks whats the outline and draws it
    if outline=="pencil":
        draw.rect(screen,purple,pencilrect,3)
    if outline=="eraser":
        draw.rect(screen,purple,eraserrect,3)
    if outline=="spray":
        draw.rect(screen,purple,sprayrect,3)
    if outline=="eyedrop":
        draw.rect(screen,purple,eyedroprect,3)
    if outline=="bucket":
        draw.rect(screen,purple,bucketrect,3)
    if outline=="rect":
        draw.rect(screen,purple,rectrect,3)
    if outline=="UFrect":
        draw.rect(screen,purple,UFrect,3)
    if outline=="circle":
        draw.rect(screen,purple,circlerect,3)
    if outline=="UFcircle":
        draw.rect(screen,purple,UFcirclerect,3)
    if outline=="line":
        draw.rect(screen,purple,linerect,3)
    if outline=="brush":
        draw.rect(screen,purple,brushrect,3)
    if outline=="drop":
        draw.rect(screen,purple,droprect,3)
    if outline=="save":
        draw.rect(screen,purple,saverect,3)
    if outline=="load":
        draw.rect(screen,purple,loadrect,3)
    if outline=="ramirez":
        draw.rect(screen,purple,ramirezrect,3)
    if outline=="striker":
        draw.rect(screen,purple,strikerrect,3)
    if outline=="ninja":
        draw.rect(screen,purple,dragonrect,3)
    if canvas.collidepoint(mx,my):
        draw.rect(screen,purple,canvas,3)


#------------------------------------------------------------------------------------
#blitting them
    if stamps=="one":
        draw.rect(screen,white,dragonrect)
        draw.rect(screen,white,ramirezrect)
        draw.rect(screen,white,strikerrect)
        screen.blit(Dragondisplay,(10,550))     #stamps
        screen.blit(ramirezdisplay,(330,550))
        screen.blit(strikerdisplay,(170,550))
    if stamps=="two":
        draw.rect(screen,white,dragonrect)
        draw.rect(screen,white,ramirezrect)
        draw.rect(screen,white,strikerrect)
        screen.blit(electric,(10,550))     #stamps
        screen.blit(axe,(330,550))
        screen.blit(sythe,(170,550))

    if stamps=="three":
        draw.rect(screen,white,dragonrect)
        draw.rect(screen,white,ramirezrect)
        draw.rect(screen,white,strikerrect)
        screen.blit(yglider,(10,550))     #stamps
        screen.blit(ogglider,(330,550))
        screen.blit(umbrella,(170,550))



#------------------------------------------------------------------------------------
#checks if mouse is pressed on canvas and clips the canvas
    if  mb[0]==1 and canvas.collidepoint(mx,my):

        screen.set_clip(canvas)

#------------------------------------------------------------------------------------
#checks the tools and uses them
        if tool=="pencil":

            draw.line(screen,col,(omx,omy),(mx,my),Psize)



        if tool=="eraser":
            draw.circle(screen,white,(mx,my),Tsize)
            draw.line(screen,white,(omx,omy),(mx,my),Tsize+15)



        if tool=="spray":
           radius =Tsize // 2                           #radius = diameter//2  (i use double backslash because i dont want decimals)
           for i in range(10):                          #the speed of how fast points are generated
                sx = randint(-radius, radius)           #choose a random point within the radius
                sy = int((radius ** 2 - sx ** 2)**0.5)  #use the equation of a circle to find sy using the square root of radius squared minus sx squared
                sy = randint(-sy, sy)                   #choose a random point within sy
                screen.set_at((mx+sx,my+sy),col)        #change the colour of a singe point inside the circle
        if tool=="bucket":
            screen.fill(col)

        if tool=="rect":
            screen.blit(Scopy,(0,0))
            draw.rect(screen,col,(startx,starty,mx-startx,my-starty))  #the starting point is x,y and the distance for x is the ending point subtracting the starting and the same for the y distance

        if tool=="UFrect":
            screen.blit(Scopy,(0,0))
            draw.rect(screen,col,(startx,starty,mx-startx,my-starty),Psize) #the same as the rect tool but has a size so that it is unfilled


        circle=Rect(startx,starty,mx-startx,my-starty)
        circle.normalize()

        if tool=="circle":
            screen.blit(Scopy,(0,0))
            draw.ellipse(screen,col,circle)
            #if   mx-startx >0 and my-starty>0 :
                #draw.ellipse(screen,col,(startx,starty,mx-startx,my-starty))#down and right
            #elif mx-startx <0 and my-starty<0:
                #draw.ellipse(screen,col,(mx,my,startx-mx,starty-my))#up and left
            #if mx-startx >0 and my-starty<0:
                #draw.ellipse(screen,col,(startx,my,mx-startx,starty-my))#up and right
            #elif mx-startx <0 and my-starty>0:
                #draw.ellipse(screen,col,(mx,starty,startx-mx,my-starty))# down and left


        if tool=="UFcircle":
            screen.blit(Scopy,(0,0))
            if circle.width > Tsize*2 and circle.height >Tsize*2:
                draw.ellipse(screen,col,circle,Tsize)
                draw.ellipse(screen,col,(circle.x+1,circle.y,circle.width,circle.height),Tsize) #draws circles atn different postitions to not make it look weird
                draw.ellipse(screen,col,(circle.x-1,circle.y,circle.width,circle.height),Tsize)
                draw.ellipse(screen,col,(circle.x,circle.y+1,circle.width,circle.height),Tsize)
                draw.ellipse(screen,col,(circle.x,circle.y-1,circle.width,circle.height),Tsize)
            else:
                draw.ellipse(screen,col,circle)


        if tool=="line":
            screen.blit(Scopy,(0,0))
            draw.line(screen, (col),(startx,starty),(mx,my),Tsize)

        if tool=='brush':
            draw.circle(screen,col,(mx,my),Tsize)
            draw.line(screen,col,(omx,omy),(mx,my),Tsize+15)

        if tool=="drop":
            col=screen.get_at((mx,my))


        if tool=="save":
            txt = getName(screen,False)                     # this is how you would call my getName function
            image.save(screen.subsurface(canvas),txt)                                # your main loop will stop looping until user hits enter
            #txtPic = comicFont.render(txt, True, (255,0,0))
            #screen.blit(txtPic,(100,100))
        if tool=="load":
            txt = getName(screen,False)
            load=image.load(txt)
            screen.blit(load,(10,11))


        if tool=="ninja":
            screen.blit(Scopy,(0,0))
            screen.blit(dragon,(mx-dragon.get_width()//2,my-dragon.get_width()//2))
        if tool=="ramirez":
            screen.blit(Scopy,(0,0))
            screen.blit(ramirez,(mx-ramirez.get_width()//2,my-ramirez.get_width()//2))
        if tool=="striker":
            screen.blit(Scopy,(0,0))
            screen.blit(striker,(mx-striker.get_width()//2,my-striker.get_width()//2))
        if tool=="axe":
            screen.blit(Scopy,(0,0))
            screen.blit(axe,(mx-axe.get_width()//2,my-axe.get_width()//2))
        if tool=="sythe":
            screen.blit(Scopy,(0,0))
            screen.blit(sythe,(mx-sythe.get_width()//2,my-sythe.get_width()//2))
        if tool=="electric":
            screen.blit(Scopy,(0,0))
            screen.blit(electric,(mx-electric.get_width()//2,my-electric.get_width()//2))
        if tool=="yglider":
            screen.blit(Scopy,(0,0))
            screen.blit(yglider,(mx-yglider.get_width()//2,yglider.get_width()//2))
        if tool=="ogglider":
            screen.blit(Scopy,(0,0))
            screen.blit(ogglider,(mx-ogglider.get_width()//2,my-ogglider.get_width()//2))
        if tool=="umbrella":
            screen.blit(Scopy,(0,0))
            screen.blit(umbrella,(mx-umbrella.get_width()//2,my-umbrella.get_width()//2))


    screen.set_clip(None) #unclips the canvas after done drawing



#------------------------------------------------------------------------------------
#checks if mouse is pressed on canvas and clips the canvas
    if mb[2]==1 and canvas.collidepoint(mx,my):
        screen.set_clip(canvas)

#------------------------------------------------------------------------------------
#checks the tools and uses them #with the second colour
        if tool=="pencil":

            draw.line(screen,col2,(omx,omy),(mx,my),Psize)



        if tool=="spray":
           radius =Tsize // 2                           #radius = diameter//2  (i use double backslash because i dont want decimals)
           for i in range(10):                          #the speed of how fast points are generated
                sx = randint(-radius, radius)           #choose a random point within the radius
                sy = int((radius ** 2 - sx ** 2)**0.5)  #use the equation of a circle to find sy using the square root of radius squared minus sx squared
                sy = randint(-sy, sy)                   #choose a random point within sy
                screen.set_at((mx+sx,my+sy),col2)        #change the colour of a singe point inside the circle
        if tool=="bucket":
            screen.fill(col2)

        if tool=="rect":
            screen.blit(Scopy,(0,0))
            draw.rect(screen,col2,(startx,starty,mx-startx,my-starty))  #the starting point is x,y and the distance for x is the ending point subtracting the starting and the same for the y distance

        if tool=="UFrect":
            screen.blit(Scopy,(0,0))
            draw.rect(screen,col2,(startx,starty,mx-startx,my-starty),Psize) #the same as the rect tool but has a size so that it is unfilled


        circle=Rect(startx,starty,mx-startx,my-starty)
        circle.normalize()

        if tool=="circle":
            screen.blit(Scopy,(0,0))
            draw.ellipse(screen,col2,circle)
            #if   mx-startx >0 and my-starty>0 :
                #draw.ellipse(screen,col,(startx,starty,mx-startx,my-starty))#down and right
            #elif mx-startx <0 and my-starty<0:
                #draw.ellipse(screen,col,(mx,my,startx-mx,starty-my))#up and left
            #if mx-startx >0 and my-starty<0:
                #draw.ellipse(screen,col,(startx,my,mx-startx,starty-my))#up and right
            #elif mx-startx <0 and my-starty>0:
                #draw.ellipse(screen,col,(mx,starty,startx-mx,my-starty))# down and left


        if tool=="UFcircle":
            screen.blit(Scopy,(0,0))
            if circle.width > Tsize*2 and circle.height >Tsize*2:
                draw.ellipse(screen,col2,circle,Tsize)
                draw.ellipse(screen,col2,(circle.x+1,circle.y,circle.width,circle.height),Tsize) #draws circles atn different postitions to not make it look weird
                draw.ellipse(screen,col2,(circle.x-1,circle.y,circle.width,circle.height),Tsize)
                draw.ellipse(screen,col2,(circle.x,circle.y+1,circle.width,circle.height),Tsize)
                draw.ellipse(screen,col2,(circle.x,circle.y-1,circle.width,circle.height),Tsize)
            else:
                draw.ellipse(screen,col2,circle)


        if tool=="line":
            screen.blit(Scopy,(0,0))
            draw.line(screen, (col2),(startx,starty),(mx,my),Tsize)

        if tool=='brush':
            draw.circle(screen,col2,(mx,my),Tsize)
            draw.line(screen,col2,(omx,omy),(mx,my),Tsize+15)

        if tool=="drop":
            col2=screen.get_at((mx,my))







    screen.set_clip(None) #unclips the canvas after done drawing

    print(mx,my)
    omx,omy=mx,my
    display.flip()
quit()
