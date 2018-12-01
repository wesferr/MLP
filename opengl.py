import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import *

class screen(object):
    def __init__(self):
        pygame.init()
        display = (600,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -5)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def circle(self, x,y, bool, radius = 0.0625):
        if(bool):
            glBegin(GL_POLYGON)
        else:
            glBegin(GL_LINE_LOOP)
            
        DEG2RAD = 3.14159/180
        for i in range(4):
          degInRad = i*DEG2RAD*90
          glVertex2f( x+cos(degInRad)*radius , y+sin(degInRad)*radius)
        glEnd();
        
    def point(self, x, y,  cor):
      glBegin(GL_POINTS)
      glColor3f(cor[0], cor[1], cor[2])
      glVertex2f(x,y)
      glEnd()
        
    def update(self):
        pygame.display.flip()
        #pygame.time.wait(5)
        self.event()
        self.draw();
        
    def line(self, x0,y0,x1,y1):
      glBegin(GL_LINES)
      glColor3f(1,1,1)
      glVertex2f(x0,y0)
      glVertex2f(x1,y1)
      glEnd()
      
    def dreta(self, W):
      a = -W[0]/W[1]#(0 - (-W[0]/W[1]))/((-W[0]/W[2]) - 0)
      b = -W[0]/W[2]#(-W[0]/W[2])
      c = -b / a
      d = b
      self.line(-2, (-2*c) +d, 2, (2*c)+d)

    def draw(self):
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glColor3f(1,1,1)
        glPointSize(4)
        glBegin(GL_LINES)
        glVertex2f(0,-2)
        glVertex2f(0,2)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(-2,0)
        glVertex2f(2,0)
        glEnd()
