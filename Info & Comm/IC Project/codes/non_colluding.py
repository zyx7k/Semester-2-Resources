from manim import *

class MyScene(Scene):
    def construct(self):

        #Images
        image1 = ImageMobject("database.png")
        image2 = ImageMobject("database.png")
        image3 = ImageMobject("database.png")
        image4 = ImageMobject("database.png")
        image5 = ImageMobject("database.png")
        image1.scale(0.15)
        image2.scale(0.15)
        image3.scale(0.15)
        image4.scale(0.15)
        image5.scale(0.15)
        target_position1 = np.array([0, 3.2, 0])
        target_position2 = np.array([-3.7, 1, 0])
        target_position3 = np.array([-2.3, -2.7, 0])
        target_position4 = np.array([2.3, -2.7, 0])
        target_position5 = np.array([3.7, 1, 0])
        image1.move_to(target_position1)
        image2.move_to(target_position2)
        image3.move_to(target_position3)
        image4.move_to(target_position4)
        image5.move_to(target_position5)

        self.play(FadeIn(image1, image2, image3, image4, image5), run_time=1.5)
        self.wait(1)

        arrow1 = DoubleArrow(start=UP, end=DOWN, color=WHITE, buff=0)
        cross1_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross1_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross1 = VGroup(cross1_h1, cross1_h2)
        arrow_with_cross1 = VGroup(arrow1, cross1)
        arrow_with_cross1.next_to(image1, RIGHT)
        arrow_with_cross1.rotate(PI/3)
        arrow_with_cross1.shift(RIGHT + DOWN*0.8)

        arrow2 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross2_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross2_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross2 = VGroup(cross2_h1, cross2_h2)
        arrow_with_cross2 = VGroup(arrow2, cross2)
        arrow_with_cross2.next_to(image2, UP) 
        arrow_with_cross2.rotate(PI/6)
        arrow_with_cross2.shift(RIGHT*1.6 + UP*0.35)

        arrow3 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross3_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross3_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross3 = VGroup(cross3_h1, cross3_h2)
        arrow_with_cross3 = VGroup(arrow3, cross3)
        target_position6 = np.array([0, -2.7, 0])
        arrow_with_cross3.move_to(target_position6)

        arrow4 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross4_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross4_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross4 = VGroup(cross4_h1, cross4_h2)
        arrow_with_cross4 = VGroup(arrow4, cross4)
        target_position7 = np.array([-3, -0.78, 0])
        arrow_with_cross4.rotate(-PI/(2.8))
        arrow_with_cross4.move_to(target_position7)


        arrow5 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross5_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross5_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross5 = VGroup(cross5_h1, cross5_h2)
        arrow_with_cross5 = VGroup(arrow5, cross5)
        target_position8 = np.array([3, -0.78, 0])
        arrow_with_cross5.rotate(PI/(2.8))
        arrow_with_cross5.move_to(target_position8)

        center_text1=Text("Non-Colluding")
        center_text1.shift(UP*0.4)
        center_text2=Text("Servers")
        center_text2.next_to(center_text1, DOWN*0.5)
        self.add(arrow_with_cross1, arrow_with_cross2, arrow_with_cross3, arrow_with_cross4, arrow_with_cross5)
        # Animate the fade in and fade out
        self.play(FadeIn(arrow_with_cross2, arrow_with_cross3, arrow_with_cross1, arrow_with_cross4, arrow_with_cross5, center_text1,center_text2), run_time=1.75)
        self.wait(4)
        self.play(FadeOut(arrow_with_cross1, arrow_with_cross2, arrow_with_cross3, arrow_with_cross5, arrow_with_cross4, image1, image2, image3, image4, image5, center_text1, center_text2), run_time=1.75)