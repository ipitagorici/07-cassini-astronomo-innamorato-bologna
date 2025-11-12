from manim import *
from PIL import Image

class Sire(Scene):
    def construct(self):
        fraseFrancese = Tex("\"Sire, ce baragouineur là ne scait se qu’il dit\"\\\\",
                    font_size=65,
                    color=YELLOW).shift(UP*1.5)
        fraseItaliano = Tex("Sire, questo fanfarone non sa quello che dice",
                    font_size=65,
                    color=YELLOW).shift(DOWN*2)

        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)

        self.play(Write(fraseFrancese), Write(fraseItaliano))