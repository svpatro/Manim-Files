from manim import *

class OpeningText(Scene):
    def construct(self):
        title = Tex(r"Linked Lists")
        self.play(Write(title))
        self.wait(3)

class LinkedList(Scene):
    def construct(self):
        title = Tex(r"Another Scene")
        self.play(Write(title))
        self.wait(3)
