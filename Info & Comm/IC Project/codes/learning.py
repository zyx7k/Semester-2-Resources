from manim import *


class trial(Scene):
    def construct(self):
        name = Tex(
            r"$C_{0}=C_{\epsilon}=\left(1+\frac{1}{N}+\frac{1}{N^{2}}+....\ +\ \frac{1}{N^{K-1}}\right)^{-1}$")

        self.play(Write(name))
        self.wait(1.5)


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
        target_position2 = np.array([-5, 1, 0])
        target_position3 = np.array([-3, -2, 0])
        target_position4 = np.array([3, -2, 0])
        target_position5 = np.array([5, 1, 0])
        image1.move_to(target_position1)
        image2.move_to(target_position2)
        image3.move_to(target_position3)
        image4.move_to(target_position4)
        image5.move_to(target_position5)

        self.play(FadeIn(image1, image2, image3, image4, image5))

        arrow = DoubleArrow(start=UP, end=DOWN, color=WHITE, buff=0)
        # Create the cross
        cross_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross = VGroup(cross_h1, cross_h2)
        # Create the arrow with cross
        arrow_with_cross1 = VGroup(arrow, cross)
        arrow_with_cross2 = VGroup(arrow, cross)
        # Add the arrow with cross to the scene
        self.add(arrow_with_cross1)
        self.add(arrow_with_cross2)

        arrow_with_cross1.next_to(image1, DOWN)
        arrow_with_cross2.next_to(image1, UP) 
        # Animate the fade in and fade out
        self.play(FadeIn(arrow_with_cross1, arrow_with_cross2), run_time=2)
        self.wait(1)
        self.play(FadeOut(arrow_with_cross1, arrow_with_cross2, image1, image2, image3), run_time=2)
        self.wait()

class ArrowCross(Scene):
    def construct(self):
        # Create the arrow
        arrow = DoubleArrow(start=UP, end=DOWN, color=WHITE, buff=0)

        # Create the cross
        cross_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross = VGroup(cross_h1, cross_h2)

        # Create the arrow with cross
        arrow_with_cross = Group(arrow, cross)

        # Add the arrow with cross to the scene
        self.add(arrow_with_cross)

        # Animate the fade in and fade out
        self.play(FadeIn(arrow_with_cross), run_time=1)
        self.wait(4)
        self.play(FadeOut(arrow_with_cross), run_time=1)
        self.wait(1)

class TextExample(Scene):
    def construct(self):
        #Normal Text
        normal_text=Text("lorum ipsum").move_to(UP)
        #Tex Text
        tex_text=Tex("lorum ipsum")
        #Latex
        latex=Tex(r"$e=m\cdot c^{2}$").move_to(DOWN)

        self.write(FadeIn(normal_text, tex_text, latex), run_time=2)
        self.wait(2)
        self.write(FadeOut(normal_text, tex_text, latex), run_time=2)
        self.wait(1)

        #Some animations
        #Normal Text
        normal_text1=AddTextLetterByLetter("lorum ipsum").move_to(UP)
        #Tex Text
        tex_text1=AddTextWordByWord("Hello How Are You?")
        #Latex
        latex1=RemoveTextLetterByLetter(r"$e=m\cdot c^{2}$").move_to(DOWN)
