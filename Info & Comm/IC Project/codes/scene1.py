from manim import *

# Parameters
N = 3  # Number of databases
K = 5  # Number of messages

class PIRScene(Scene):
    def construct(self):
        # Set up the scene
        databases = VGroup(*[
            ImageMobject("database.png").scale(0.8).shift(2 * i * UP)
            for i in range(1, N+1)
        ])
        messages = VGroup(*[
            Tex(r"W_{i}").next_to(databases, LEFT, buff=1)
            for i, databases in enumerate(databases, start=1)
        ])
        user = ImageMobject("user.png").scale(0.8).to_edge(LEFT)

        # Fade in databases and messages
        self.play(FadeIn(databases))
        self.play(FadeIn(messages))

        # Fade in user and desired message
        desired_message = MathTex("W_{\\theta}").next_to(user, RIGHT, buff=1)
        self.play(FadeIn(user), FadeIn(desired_message))

        # Clear the left side
        self.wait(1)
        self.play(FadeOut(user), FadeOut(desired_message), FadeOut(databases), FadeOut(messages))

        # Generate and send queries
        queries = VGroup(*[
            Tex(r"Q_{i}").to_edge(LEFT, buff=1)
            for i in range(1, N+1)
        ])
        self.play(FadeIn(queries))

        # Move queries to databases
        for i, query in enumerate(queries):
            query.generate_target()
            query.target.next_to(databases[i], LEFT, buff=0.5)
            self.play(MoveToTarget(query))

        # Remove queries
        self.wait(1)
        self.play(FadeOut(queries))

        # Generate and move answers
        answers = VGroup(*[
            MathTex(f"A_{i}").next_to(query, LEFT, buff=0.5)
            for i, query in enumerate(queries)
        ])
        self.play(FadeIn(answers))

        # Move answers back to original positions
        for i, answer in enumerate(answers):
            answer.generate_target()
            answer.target.next_to(databases[i], LEFT, buff=0.5)
            self.play(MoveToTarget(answer))

        # Fade out answers
        self.wait(1)
        self.play(FadeOut(answers))

        self.wait(2)

# Parameters
N = 3  # Number of databases
K = 5  # Number of messages
