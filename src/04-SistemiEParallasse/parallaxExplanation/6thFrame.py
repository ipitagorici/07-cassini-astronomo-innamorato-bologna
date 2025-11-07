from manim import *

class Frame6(Scene):
    def color_switcher_G(color_value):
        return GREEN if color_value==0 else PINK
    def color_switcher_K(color_value):
        return BLUE if color_value==0 else PINK
    
    def construct(self):
        # COLOR LEGEND
        legenda_comet = Tex("Cometa", color=RED)\
            .to_corner(UR)
        legenda_observer = Tex("Osservatori", color=YELLOW)\
            .next_to(legenda_comet, DOWN)\
            .align_to(legenda_comet, RIGHT)
        legenda_distance_EG = Tex("Distanza EG", color=GREEN)\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
        legenda_distance_EK = Tex("Distanza EK", color=BLUE)\
            .next_to(legenda_distance_EG, DOWN)\
            .align_to(legenda_observer, RIGHT)
        legenda_parallasse_corretta = Tex("Parallasse corretta", color=PINK)\
            .next_to(legenda_distance_EK, DOWN)\
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
            .move_to([bigger_arc.get_end()[0]+0.5, bigger_arc.get_end()[1]-0.05, 0])
        # G: State tracker for color switch (0=green, 1=pink)
        G_color_state = ValueTracker(0)  # Float: Safe scalar
        G_radius = ValueTracker(0)
        def get_G_color():
            return GREEN if G_color_state.get_value() < 0.5 else PINK
        G = always_redraw(lambda: Dot(
            radius=G_radius.get_value(),
            color=get_G_color()  # Dynamic: Pulls from state
        ).move_to([comet.get_center()[0]+0.25, comet.get_center()[1]+0.65, 0]))

        # K: Same pattern (0=blue, 1=pink)
        K_color_state = ValueTracker(0)
        K_radius = ValueTracker(0)
        def get_K_color():
            return BLUE if K_color_state.get_value() < 0.5 else PINK
        K = always_redraw(lambda: Dot(
            radius=K_radius.get_value(),
            color=get_K_color()  # Dynamic
        ).move_to([comet.get_center()[0]+0.53, comet.get_center()[1]+0.53, 0]))
            
        # LINES
        EG = Line(E, G,
            stroke_width=5,
            color=GREEN)
        EK = Line(E, K,
            stroke_width=5,
            color=BLUE)
        GK = Line(G, K,
            color=PINK)
        
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
        self.play(Write(legenda_comet, run_time=0.5),
                Write(legenda_observer, run_time=0.5),
                Write(legenda_distance_EG),
                Write(legenda_distance_EK),
                Write(legenda_parallasse_corretta)  
        )
        
        self.play(FadeIn(axes, bigger_arc, smaller_arc, observer_arc, BG, E, G, K, CG, BK, comet, A_label, B_label, C_label, D_label, E_label, H_label, K_label, G_label, observer_point_B, observer_point_C))
        
        EG_appearance = AnimationGroup(AnimationGroup(FadeIn(EG), G_radius.animate.set_value(0.15)))
        EG_disappearance = AnimationGroup(FadeOut(EG, run_time=2), G_radius.animate.set_value(0))
        EK_appearance = AnimationGroup(AnimationGroup(FadeIn(EK), K_radius.animate.set_value(0.15)))
        EK_disappearance = AnimationGroup(FadeOut(EK, run_time=2), K_radius.animate.set_value(0))
        
        G_color_switch = G_color_state.animate.set_value(1).set_run_time(1)
        K_color_switch = K_color_state.animate.set_value(1).set_run_time(1)
        GK_appearance = AnimationGroup(G_color_switch,
                                       K_color_switch,
                                       G_radius.animate.set_value(0.1),
                                       K_radius.animate.set_value(0.1),
                                       FadeIn(GK))
        
        self.play(EG_appearance)
        self.play(EK_appearance)
        self.wait()
        self.play(EG_disappearance, EK_disappearance, GK_appearance)
        
        self.wait(2)        