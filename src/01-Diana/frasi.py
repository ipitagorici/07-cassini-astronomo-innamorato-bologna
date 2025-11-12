from manim import *
from PIL import Image

class Beltade(Scene):
    def construct(self):
        frase = Tex("che cercavano […] il bene, la sapienza,\\\\la beltade",
                    font_size=75,
                    color=YELLOW)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
                                          
        self.play(Write(frase))
        
class Cicada(Scene):
    def construct(self):
        frase = Tex("CICADA:\\\\"+
                    "\"Onde procede, o Tansillo,\\\\"+
                    "che l'animo in tal progresso s'appaga del suo tormento?\\\\"+
                    "Onde procede quel sprone ch'il stimola sempre\\\\oltre quel che possiede?\"",
                    font_size=55,
                    color=YELLOW)   
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(frase))
