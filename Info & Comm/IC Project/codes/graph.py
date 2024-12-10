from manim import * 

def f(self, x, z):
    # Define your function f(x, z) here
    return x ** 2 + z


class TwoVariableGraph(Scene):
    def construct(self):
        x_range = (-5, 5, 0.1)
        z_values = [1, 2, 3, 4, 5]  # List of z values to vary

        axes = Axes(
            x_range=(-5, 5, 1),
            y_range=(-10, 10, 1),
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(-5, 6)},
            y_axis_config={"numbers_to_include": range(-10, 11)},
        )
        
        graphs = []
        for z in z_values:
            equation = lambda x: np.array([x, f(x, z), 0])  # Define your function f(x, z) here
            graph = ParametricFunction(equation, t_range=x_range, color=RED)
            graphs.append(graph)

        self.add(axes, *graphs)
        self.wait()

