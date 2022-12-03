from manim import *

class LinkedList(Scene):
    def construct(self):
        title = Tex(r"Another Scene")
        self.play(Write(title))
        self.wait(3)
