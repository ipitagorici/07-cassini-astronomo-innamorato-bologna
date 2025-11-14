from manim import *

class FirstMethod(Scene):
    def construct(self):
        
        ##############
        ### LEGEND ###
        ##############
        
        legenda_comet = Tex("Cometa", color=RED)\
            .to_corner(UR)
        legenda_observer = Tex("Osservatore", color=YELLOW)\
            .next_to(legenda_comet, DOWN)\
            .align_to(legenda_comet, RIGHT)
        legenda_distance = Tex("Distanza da stella", color=GREEN)\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
        legenda_parallax_1 = Tex("Possibile\\\\parallasse corretta", color=GREEN,
                               tex_environment="flushright")\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
        legenda_parallax_2 = Tex("Possibile\\\\parallasse corretta", color=PINK,
                               tex_environment="flushright")\
            .next_to(legenda_observer, DOWN)\
            .align_to(legenda_observer, RIGHT)
            
        parallax_original = ImageMobject("src/assets/parallasse_metodo_1.jpg")\
            .scale(0.7)\

            
            
        #####################
        ### SCENE OBJECTS ###
        #####################
        
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

        observer_arc_label = Tex("Terra")\
            .next_to(observer_arc.get_start(), DOWN)\
            .shift(LEFT*1.5)
        observer_point_label = Tex("Punto d'osservazione", font_size=40)\
            .next_to(observer_arc.get_end(), LEFT)

        observer_point = Dot(observer_arc.get_end())\
            .set_color(YELLOW)
            
            
            
        # SECOND FRAME OBJECTS
        
        # POINTS
        H = Dot([-1, 2.3, 0])
        comet_position_1 = Dot([-1.25, 1.6, 0])\
            .set_color(RED)


        # POINTS LABELS
        E_star = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc.get_end()[0]+0.5, bigger_arc.get_end()[1] - 0.05, 0])
        E_label = Tex("E")\
            .next_to(E_star, UP)
        F_label = Tex("F")\
            .next_to(comet_position_1, DR)\
            .shift(LEFT*0.3)
        H_label = Tex("H")\
            .next_to(H, UP)


        # DISTANCES
        BH = Line(observer_arc.get_end(),
                  H)
        EH = Line(E_star, H,
                  stroke_width=6)\
            .set_color(GREEN)
            
            
            
        # THIRD FRAME OBJECTS
        L = Dot([2.3, observer_arc.get_end()[1]+0.55, 0])
        comet_position_2 = Dot([1.5, observer_arc.get_end()[1]+0.5, 0])\
            .set_color(RED)

        # POINTS LABELS
        K_star = Star(outer_radius=0.1).set_color(WHITE)\
            .move_to([bigger_arc.get_center()[0]+1.8, bigger_arc.get_center()[1]+0.1, 0])
        K_label = Tex("K")\
            .next_to(K_star, UR*0.3)
        L_label = Tex("L")\
            .next_to(L, RIGHT)
        G_label = Tex("G")\
            .next_to(comet_position_2, DR)\
            .shift(LEFT*0.6)

        # DISTANCES
        BL = Line(observer_arc.get_end(),
                   L)
        KL = Line(K_star, L,
                  stroke_width=6)\
            .set_color(GREEN)

        # ARROWS
        comet_movement_arrow = CurvedArrow([-1.25, 1.6, 0], comet_position_2.get_center(), angle=PI/4)
        star_movement_arrow = CurvedArrow([bigger_arc.get_end()[0]+0.5, bigger_arc.get_end()[1] - 0.03, 0], K_star.get_center(), angle=-PI/2)
        
            
            
        # FOURTH FRAME OBJECTS
        M = Dot(L.get_center())\
            .shift(LEFT*0.345)\
            .shift(UP*0.7)
        M_label = Tex("M")\
            .next_to(M, RIGHT)
        ML = Line(M.get_center(), L,
            stroke_width=6)\
            .set_color(PINK)
            
        ##################
        ### ANIMATIONS ###
        ##################
        
        # PARALLAX IMAGE APPEARANCE
        self.play(FadeIn(parallax_original))
        self.wait()
        
        self.play(parallax_original.animate.scale(0.4))
        self.play(parallax_original.animate\
            .next_to(legenda_parallax_2, DOWN))
        self.play(parallax_original.animate.shift(RIGHT*0.5))
        
        
        # FIRST FRAME
        self.play(Write(legenda_observer))
        
        self.play(FadeIn(axes, observer_arc, observer_arc_label, observer_point_label, observer_point, smaller_arc, bigger_arc))
        
        self.wait(2)
        
        # CLEANING
        self.play(FadeOut(observer_arc_label, observer_point_label), run_time=1)
        
        
        # SECOND FRAME
        self.play(Write(legenda_distance), Write(legenda_comet))
        
        self.play(FadeIn(E_star, E_label, H, H_label, BH, comet_position_1, F_label, EH))
        
        self.wait(2)        

        
        # THIRD FRAME
        second_frame_exclusive_objects = VGroup(
            E_star, E_label, H, H_label, BH, comet_position_1, F_label, EH
        )
        third_frame_exclusive_objects = VGroup(
            K_star, K_label, L, L_label, BL, comet_position_2, G_label, KL, comet_movement_arrow, star_movement_arrow
        )
        
        self.play(Transform(second_frame_exclusive_objects, third_frame_exclusive_objects, replace_mobject_with_target_in_scene=True),
                  Transform(legenda_distance, legenda_parallax_1, replace_mobject_with_target_in_scene=True))
        
        self.wait(2) 
        
        
        # COPYING
        third_frame_copy = VGroup(
            third_frame_exclusive_objects.copy(),
            axes.copy(),
            observer_arc.copy(),
            smaller_arc.copy(),
            bigger_arc.copy(),
            observer_point.copy()
        )
        third_frame_copy.scale(0.6).to_edge(LEFT)
        
        self.play(Transform(third_frame_exclusive_objects.copy(), third_frame_copy))
        
        
        # FOURTH FRAME
        self.play(Uncreate(legenda_parallax_1), run_time=0.5)
        self.play(FadeIn(M, M_label), Transform(KL, ML, replace_mobject_with_target_in_scene=True),
                  Write(legenda_parallax_2), run_time=0.5)
        
        
        self.wait(2)    