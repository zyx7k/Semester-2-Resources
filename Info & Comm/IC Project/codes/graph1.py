from manim import *
import numpy as np

class GraphPlot(Scene):
    def construct(self):
        K = 5  # Set the value of K here

        # Create the axes
        axes = Axes(
            x_range=[-15, 15, 5],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False}
        )
        axes_labels = axes.get_axis_labels(x_label="X", y_label="Y")
        self.play(Create(axes), Create(axes_labels))

        # Set the x-axis range
        x_min = 1
        x_max = 10
        x_range = ValueTracker(x_min)
        x_axis = axes.get_x_axis()
        x_axis.add_updater(lambda axis: axis.set_range(x_range.get_value(), x_max))

        # Create the graph plot
        graph = axes.get_graph(
            lambda x: (1 + sum([1 / (x ** i) for i in range(K)])) ** -1,
        )
        self.add(x_axis, graph)
        self.play(x_range.animate.set_value(x_max), run_time=2)

        self.wait()
