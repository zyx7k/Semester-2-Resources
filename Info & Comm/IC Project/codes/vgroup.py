from manim import *

class VGroupExample(Scene):
    def construct(self):
      p1= [2,-2,1]
      p2= [-2,-2,0]
      p3= [2, 0, 1]
      p4= [-2,2,0]
      p5= [2,2,1]
      bec = Line3D(p1,p2).append_points(Line3D(p2,p3).points).append_points(Line3D(p3,p4).points).append_points(Line3D(p4,p5).points).append_points(Line3D(p5, p1).points)
      self.play(Create(bec))
