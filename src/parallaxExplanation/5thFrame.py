from manim import *

class Frame5(Scene):
    def construct(self):
        # COLOR LEGEND
        legenda_comet = Tex("Cometa", color=RED)\
            .to_corner(UR)
        legenda_observer = Tex("Osservatori", color=YELLOW)\
            .next_to(legenda_comet, DOWN)\
            .align_to(legenda_comet, RIGHT)
        legenda_distance = Tex("Parallasse corretta", color=PINK)\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
        
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
        observer_point_1 = Dot(observer_arc.get_end())\
            .set_color(YELLOW)
        observer_point_2 = Dot(observer_arc.get_start())\
            .shift(UP*0.5)\
            .shift(LEFT*0.15)\
            .set_color(YELLOW)
        
        # POINTS
        E = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc.get_end()[0]+0.5, bigger_arc.get_end()[1], 0])
        K = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc.get_center()[0]+0.7, bigger_arc.get_center()[1]+1.25, 0])
        comet = Dot(color = RED)\
            .next_to(K, DL)\
            .shift(LEFT*0.2)
        
        # DISTANCES
        BK = Line(observer_arc.get_end(),
            K.get_center())
        CG = Line([observer_arc.get_start()[0]-0.15, observer_arc.get_start()[1]+0.5, 0],
            [BK.get_end()[0]-0.1, BK.get_end()[1]+0.1, 0])
        BG = Line(observer_arc.get_end(),
            CG.get_end())
        
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
            .next_to(E, UR)
        H_label = Tex("H")\
            .next_to(comet, DOWN)
        K_label = Tex("K")\
            .next_to(K, UR*0.3)
        G_label = Tex("G")\
            .next_to(BG.get_end(), UR*0.5)



        # ANIMATIONS
        self.play(Write(legenda_comet), Write(legenda_observer), Write(legenda_distance))
        
        self.play(FadeIn(axes, bigger_arc, smaller_arc, observer_arc, BG, E, K, CG, BK, comet, A_label, B_label, C_label, D_label, E_label, H_label, K_label, G_label, observer_point_1, observer_point_2))
        
        self.wait(2)