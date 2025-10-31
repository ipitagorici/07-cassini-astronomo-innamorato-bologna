from manim import *

class Frame4(Scene):
    def construct(self):
        # COLOR LEGEND
        legenda_comet = Tex("Cometa", color=RED)\
            .to_corner(UR)
        legenda_observer = Tex("Osservatore", color=YELLOW)\
            .next_to(legenda_comet, DOWN)\
            .align_to(legenda_comet, RIGHT)
        legenda_parallax = Tex("Parallasse corretta", color=PINK)\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
            
        # MAIN STRUCTURE
        axes1 = Axes(
            (0, 5, 5), (0, 5, 5),
            5, 5,
            tips=False
        )
        bigger_arc1 = Arc(5,
                  angle=PI/2,
                  arc_center=axes1.get_origin()
        )
        smaller_arc1 = Arc(
            4.25,
            angle=PI/2,
            arc_center=axes1.get_origin()
        )
        observer_arc1 = Arc(
            1, 
            angle=PI/2,
            arc_center=axes1.get_origin()
        )

        # OBSERVER COMPONENTS
        observer_arc_label1 = Tex("Terra")\
            .next_to(observer_arc1.get_start(), DOWN)\
            .shift(LEFT*1.5)
        observer_point_label1 = Tex("Punto d'osservazione", font_size=40)\
            .next_to(observer_arc1.get_end(), LEFT)
        observer_point = Dot(observer_arc1.get_end())\
            .set_color(YELLOW)
        
        # POINTS 
        L1 = Dot([2.27, observer_arc1.get_end()[1]+0.6, 0])
        M1 = Dot(L1.get_center())\
            .shift(LEFT*0.3)\
            .shift(UP*0.7)
        comet_position1v2 = Dot([1.5, observer_arc1.get_end()[1]+0.5, 0])\
            .set_color(RED)
        
        # LABELS
        K_star1 = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc1.get_center()[0]+1.8, bigger_arc1.get_center()[1]+0.1, 0])
        K_label1 = Tex("K")\
            .next_to(K_star1, UR*0.3)
        L_label1 = Tex("L")\
            .next_to(L1, RIGHT)
        M_label1 = Tex("M")\
            .next_to(M1, RIGHT)
        G_label1 = Tex("G")\
            .next_to(comet_position1v2, DR)\
            .shift(LEFT*0.6)
    
        # DISTANCES
        BL1 = Line(observer_arc1.get_end(),
                   L1)
        ML = Line(M1.get_center(), L1,
                  stroke_width=6)\
            .set_color(PINK)

        # ARROWS
        comet_movement_arrow = CurvedArrow([-1.25, 1.6, 0], comet_position1v2.get_center(), angle=PI/4)
        star_movement_arrow = CurvedArrow([bigger_arc1.get_end()[0]+0.5, bigger_arc1.get_end()[1] - 0.03, 0], K_star1.get_center(), angle=-PI/2)



        # ANIMATIONS
        self.play(Write(legenda_comet), Write(legenda_observer), Write(legenda_parallax), run_time=0.5)

        self.play(FadeIn(axes1, observer_arc1, observer_arc_label1, observer_point_label1, observer_point, smaller_arc1, bigger_arc1))
        self.play(FadeIn(K_star1, K_label1, L1, L_label1, BL1, comet_position1v2, G_label1, ML, comet_movement_arrow, star_movement_arrow, M1, M_label1))

        self.wait(2)