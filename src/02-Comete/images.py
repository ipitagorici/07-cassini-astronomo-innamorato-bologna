from manim import *
from PIL import Image

class CostantinopoliAssediata(Scene):
    def construct(self):
        costantinopoliAssediata = ImageMobject("src/assets/costantinopoliAssediata.jpg")
        costantinopoliAssediata.move_to(ORIGIN)
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
                                          
        self.play(FadeIn(costantinopoliAssediata))
        self.wait(2)
        
class CannoneOttomano(Scene):
    def construct(self):
        cannone = ImageMobject("src/assets/cannone-ottomano.jpg")
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(cannone))
        self.wait(2)
        
class MuraCostantinopoli(Scene):
    def construct(self):
        mura = ImageMobject("src/assets/mura-costantinopoli.jpg")
        
        bg = ImageMobject("src/assets/sfondoSpazio.jpg")
        bg.set_resampling_algorithm(Image.Resampling.BICUBIC)
        bg.scale_to_fit_width(config.frame_width)
        self.add(bg)
        
        self.play(FadeIn(mura))
        self.wait(2)
        