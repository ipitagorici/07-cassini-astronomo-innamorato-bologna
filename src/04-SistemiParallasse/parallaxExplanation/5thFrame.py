from manim import *

class Frame5(Scene):
    def construct(self):
        # COLOR LEGEND
        legenda_comet = Tex("Cometa", color=RED)\
            .to_corner(UR)
        legenda_observer = Tex("Osservatori", color=YELLOW)\
            .next_to(legenda_comet, DOWN)\
            .align_to(legenda_comet, RIGHT)
        
        # MAIN STRUCTURE
        axes = Axes(
            (0, 5, 5), (0, 5, 5),
            5, 5,
            tips=False
        )
        bigger_arc = Arc(5,
                  angle=PI/2,
                  arc_center=axes.get_origin()
        )
        smaller_arc = Arc(
            4.25,
            angle=PI/2,
            arc_center=axes.get_origin()
        )
        observer_arc = Arc(
            1, 
            angle=PI/2,
            arc_center=axes.get_origin()
        )       
        
        # OBSERVER COMPONENTS
        observer_point_B = Dot(observer_arc.get_end())\
            .set_color(YELLOW)
        observer_point_C = Dot(observer_arc.get_start())\
            .shift(UP*0.5)\
            .shift(LEFT*0.15)\
            .set_color(YELLOW)
        
        # POINTS
        comet = Dot(color = RED)\
            .move_to([bigger_arc.get_center()[0]-0.35, bigger_arc.get_center()[1]+1.2, 0])
        E = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc.get_end()[0]+0.5, bigger_arc.get_end()[1], 0])
        G = Dot(radius=0)\
            .move_to([comet.get_center()[0]+0.25, comet.get_center()[1]+0.65, 0])
        K = Dot(radius=0)\
            .move_to([comet.get_center()[0]+0.53, comet.get_center()[1]+0.56, 0])
        
        # DISTANCES
        BK = Line(observer_arc.get_end(),
            K.get_center())
        BG = Line(observer_point_B,
            G.get_center()) 
        CG = Line(observer_point_C,
            G.get_center())
        
        # LABEL
        A_label = Tex("A")\
            .next_to(axes.get_origin(), DOWN)\
            .shift(LEFT*0.3)
        B_label = Tex("B")\
            .next_to(observer_arc.get_end(), LEFT)
        C_label = Tex("C")\
            .next_to(CG.get_start(), RIGHT)
        D_label = Tex("D")\
            .next_to(bigger_arc.get_end(), LEFT)
        E_label = Tex("E")\
            .next_to(E, UP)
        H_label = Tex("H")\
            .next_to(comet, DOWN)
        K_label = Tex("K")\
            .next_to(K, UR*0.4)
        G_label = Tex("G")\
            .next_to(G, UP*0.9)\
            .shift(RIGHT*0.1)

        # ANIMATIONS
        self.play(Write(legenda_comet), Write(legenda_observer))
        
        self.play(FadeIn(axes, bigger_arc, smaller_arc, observer_arc, BG, E, K, CG, BK, comet, A_label, B_label, C_label, D_label, E_label, H_label, K_label, G_label, observer_point_B, observer_point_C))
        
        self.wait(2)