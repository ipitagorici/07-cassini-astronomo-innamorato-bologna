from manim import *

class Pitagorici(Scene):
    def construct(self):
        pythagoras = ImageMobject("src/assets/pythagoras_nobg.png")
        pitagorici = ImageMobject("src/assets/PITAGORICI (29.7 x 21 cm).png")
        
        pitagorici.scale(0.5).to_edge(UP)
        pythagoras.scale(0.8).to_edge(DOWN)
        
        self.play(FadeIn(pitagorici), FadeIn(pythagoras))