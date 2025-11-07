from manim import *

class DianaGuercino(Scene):
    def construct(self):
        diana_guercino = ImageMobject("src/assets/Diana-Cacciatrice-del-Guercino-1658.jpg")
        
        self.play(FadeIn(diana_guercino))
        self.wait(2)

class DianaCaserta(Scene):
    def construct(self):
        diana_caserta = ImageMobject("src/assets/Reggia-di-Caserta-Diana.jpg")
        diana_caserta.scale(0.65)
                                          
        self.play(FadeIn(diana_caserta))
        self.wait(2)

class AtteoneCani(Scene):
    def construct(self):
        atteone_cani = ImageMobject("src/assets/Atteone-Cani.jpg")                          
        atteone_cani.scale(0.45)
        
        self.play(FadeIn(atteone_cani))
        self.wait(2)