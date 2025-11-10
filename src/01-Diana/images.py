from manim import *
from PIL import Image

class DianaGuercino(Scene):
    def construct(self):
        diana_guercino = ImageMobject("src/assets/Diana-Cacciatrice-del-Guercino-1658.jpg")
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(diana_guercino))
        self.wait(2)

class DianaCaserta(Scene):
    def construct(self):
        diana_caserta = ImageMobject("src/assets/Reggia-di-Caserta-Diana.jpg")
        diana_caserta.scale(0.65)
                    
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
                                          
        self.play(FadeIn(diana_caserta))
        self.wait(2)

class AtteoneCani(Scene):
    def construct(self):
        atteone_cani = ImageMobject("src/assets/Atteone-Cani.jpg")                          
        atteone_cani.scale(0.45)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(atteone_cani))
        self.wait(2)