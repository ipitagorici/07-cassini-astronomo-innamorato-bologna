from manim import *
from PIL import Image

class vehementer(Scene):
    def construct(self):
        frase = Tex("vehementer me perturbarunt",
                    color=YELLOW,
                    font_size=90)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(Write(frase))