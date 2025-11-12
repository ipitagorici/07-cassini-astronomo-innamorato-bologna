from manim import *
import numpy as np

class Cassiniana(MovingCameraScene):
    def construct(self):
        
        ###########
        ### TEX ###
        ###########
        
        title = Tex("Cassiniana\\\\(Ovale di Cassini)").to_edge(UP)
        lemniscate = Tex("Lemniscata\\\\di Bernoulli")



        ##############
        ### VALUES ###
        ##############
        
        a = 1.5
        b_values = [1.1, 1.5, 1.9, a**2, 1.3*(a**2), 1.7*(a**2), 4.4, 5, 5.6] 
        colors = [RED, ORANGE, YELLOW, PURPLE, GREEN, BLUE, TEAL, PINK, MAROON, GRAY]


        
        ############
        ### FOCI ###
        ############
        
        focus1 = Dot([-a, 0, 0], color=RED, radius=0.08)
        focus2 = Dot([a, 0, 0], color=RED, radius=0.08)
        foci = VGroup(focus1, focus2)
        
        
        
        ##################
        ### ANIMATIONS ###
        ##################
        
        self.play(Write(title, run_time=0.75))
        
        self.play(FadeIn(foci), run_time=1)
        self.wait(1)
        
        
        # CREATION OF CASSINI OVAL
        
        cassiniana = VGroup()
        for b, color in zip(b_values, colors):
            # Equation with fixed a, varying b—builds the nested family
            cassiniana_equation = lambda x, y: ((x + a)**2 + y**2) * ((x - a)**2 + y**2) - b**2
            curve = ImplicitFunction(
                cassiniana_equation,
                color=color,
                stroke_width=2
            )
            cassiniana.add(curve)
            
            self.play(Create(curve), run_time=1)
            
            if b == a**2:
                lemniscate.next_to(curve, RIGHT)
                
                self.play(curve.animate.set_stroke(width=8), Flash(curve, flash_radius=2.4, num_lines=30), TransformFromCopy(curve, lemniscate))
                self.wait(2)
                self.play(curve.animate.set_stroke(width=2), FadeOut(lemniscate))
        
        
        # ZOOMING CAMERA   
        
        self.play(self.camera.frame.animate.set(width = cassiniana.width*1.5))
        
        
        # COOL STUFF
        
        self.play(FadeOut(cassiniana), FadeOut(foci), run_time=0.25)
        self.play(ShowPassingFlash(cassiniana), ShowPassingFlash(foci), run_time=0.5)
        self.play(FadeIn(cassiniana), FadeIn(foci), run_time=2)
        
            
        self.wait(2)
