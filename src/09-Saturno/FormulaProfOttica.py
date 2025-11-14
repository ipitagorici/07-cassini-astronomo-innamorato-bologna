from manim import *
from PIL import Image

class FormulaProfOttica(Scene):
    def construct(self):
        formula = MathTex(r"\log\tfrac{F_i}{F_t}",
                          color=YELLOW,
                          font_size=200)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(formula))