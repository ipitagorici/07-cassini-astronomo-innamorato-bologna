from manim import *
from PIL import Image

class Ringraziamenti(Scene):
    def construct(self):
        self.camera.background_color = '#ffffff'
        
        ringraziamenti = Tex("Speciali ringraziamenti a:", color=BLACK).to_edge(UP)

        comitato_cassini_logo = ImageMobject("src/assets/Logo_CN.png").scale(0.2).next_to(ringraziamenti, DOWN).to_edge(LEFT).shift(DOWN)
        comitato_cassini_scritta = Tex("Comitato Nazionale Cassini\\\\400", color=BLACK).next_to(comitato_cassini_logo, RIGHT)
        comitato_cassini = Group(
            comitato_cassini_logo, comitato_cassini_scritta
        ).move_to([ORIGIN[0], comitato_cassini_logo.get_y(), 0])
        
        almamater_logo = ImageMobject("src/assets/Marchio_DIP-FISICA-E-ASTRONOMIA_DIFA_ITA.png").scale(0.25).to_edge(LEFT).shift(DOWN*2)
                
        self.play(Write(ringraziamenti))
        
        self.play(FadeIn(comitato_cassini_logo), FadeIn(comitato_cassini_scritta))
        self.play(FadeIn(almamater_logo))
