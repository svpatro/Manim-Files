from manim import *

class LinkedList(Scene):
    def construct(self):
        title = Tex(r"Linked Lists")
        self.play(Write(title))
        self.wait(3)
