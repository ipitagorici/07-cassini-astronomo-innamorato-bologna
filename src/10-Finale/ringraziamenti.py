from manim import *

class Ringraziamenti(Scene):
    def construct(self):
        comitato_cassini_logo = ImageMobject("src/assets/Logo_CN.png").scale(0.3).next_to(ringraziamenti, DOWN).to_edge(LEFT)
        comitato_cassini = Tex("Comitato Nazionale Cassini 400").next_to(comitato_cassini_logo, DOWN).to_edge(LEFT)
        
        almamater_logo = ImageMobject("src/assets/Marchio_DIP-FISICA-E-ASTRONOMIA_DIFA_ITA.png").scale(0.5).to_edge(RIGHT)
        
        ringraziamenti = Tex("Speciali ringraziamenti a:").to_edge(UP)
        
        self.play(Write(ringraziamenti))
        
        self.play(FadeIn(comitato_cassini_logo), DrawBorderThenFill(comitato_cassini))
        self.play(FadeIn(almamater_logo))
