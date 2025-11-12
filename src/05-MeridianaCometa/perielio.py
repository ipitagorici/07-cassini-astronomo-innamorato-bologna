from manim import *
class Perielio(Scene):
    def construct(self):
        ##############
        ### CIRCLE ###
        ##############
        circle = Circle(radius=2).set_color(WHITE)\
            .shift(UP)\
            .rotate(-90*DEGREES)
        ############
        ### DOTS ###
        ############
        F = Dot(circle.get_center())
        P = Dot([F.get_x(), F.get_y()+circle.radius, 0])
        C = Dot([F.get_x(), F.get_y()-circle.radius, 0])\
            .set_color(PURPLE)\
            .set_z_index(9999)
        B = Dot(radius=0.1)\
            .move_to([C.get_x()-1.6, C.get_y()+0.7, 0])
        G = Dot(radius=0.1)\
            .move_to([C.get_x()-0.8, C.get_y()+0.3, 0])
        H = Dot(radius=0.1)\
            .move_to([C.get_x()+0.8, C.get_y()+0.3, 0])
        E = Dot(radius=0.1)\
            .move_to([C.get_x()+1.6, C.get_y()+0.7, 0])
        D = Dot([C.get_x()-0.45, C.get_y()-0.2, 0])
        A = Dot([C.get_x()+0.45, C.get_y()-0.2, 0])
        ##############
        ### LABELS ###
        ##############
        F_label = Tex("F",
            font_size=30)\
            .next_to(F, UR*0.2)
        P_label = Tex("P",
            font_size=30)\
            .next_to(P, UP)
        C_label = Tex("C",
            font_size=30)\
            .next_to(C, DOWN*0.2).shift(RIGHT*0.165)
        B_label = Tex("B",
            font_size=30)\
            .next_to(B, DOWN*0.25)
        G_label = Tex("G",
            font_size=30)\
            .next_to(G, UP*0.2).shift(RIGHT*0.4)
        H_label = Tex("H",
            font_size=30)\
            .next_to(H, UP*0.2).shift(LEFT*0.4)
        E_label = Tex("E",
            font_size=30)\
            .next_to(E, DOWN*0.2)
        D_label = Tex("D",
            font_size=20)\
            .move_to(D.get_center())\
            .shift(LEFT*0.2).shift(UP*0.09)
        A_label = Tex("A",
            font_size=20)\
            .move_to(A.get_center())\
            .shift(RIGHT*0.2).shift(UP*0.09)
        ############
        ### ARCS ###
        ############
        vec_E = E.get_center() - F.get_center()
        start_angle_E = np.arctan2(vec_E[1], vec_E[0])
        vec_B = B.get_center() - F.get_center()
        start_angle_B = np.arctan2(vec_B[1], vec_B[0])
        vec_C = C.get_center() - F.get_center()
        end_angle_C = np.arctan2(vec_C[1], vec_C[0])
        angle_span_EC = end_angle_C - start_angle_E
        EC_arc = Arc(radius=circle.radius, start_angle=start_angle_E, angle=angle_span_EC, stroke_width=8)\
            .set_color(RED)\
            .move_to(H.get_center())\
            .shift(UP*0.1)
        angle_span_BC = end_angle_C - start_angle_B
        BC_arc = Arc(radius=circle.radius, start_angle=start_angle_B, angle=angle_span_BC, stroke_width=8)\
            .set_color(BLUE)\
            .move_to(G.get_center())\
            .shift(UP*0.1)
        BE_angle_span = start_angle_E - start_angle_B
        BE_arc = Arc(arc_center=F.get_center(), radius=circle.radius, start_angle=start_angle_B, angle=BE_angle_span, stroke_width=8)
        BE_angle_span_reverse = start_angle_B - start_angle_E
        BE_arc_reverse = Arc(arc_center=F.get_center(), radius=circle.radius, start_angle=start_angle_E, angle=BE_angle_span_reverse, stroke_width=8)
        #############
        ### LINES ###
        #############
        FP = Line(F, P)
        FC = Line(F, C)
        FB = Line(F, B)
        FG = Line(F, G)
        FH = Line(F, H)
        FE = Line(F, E)
        M = Dot([FC.get_end()[0], FC.get_end()[1]-1.25, 0])
        BC = Line(FB.get_end(), C.get_center())
        EC = Line(FE.get_end(), C.get_center())
        CM = Line(M.get_center(), FC.get_end())
        BM = Line(M.get_center(), FB.get_end())
        EM = Line(M.get_center(), FE.get_end())
        IK = Line([C.get_x()-circle.radius, C.get_y(), 0],
            [C.get_x()+circle.radius, C.get_y(), 0])
        CI = Line(FC.get_end(),
            [IK.get_start()[0], IK.get_start()[1]-circle.radius/2, 0])
        CK = Line(FC.get_end(),
            [IK.get_end()[0], IK.get_end()[1]-circle.radius/2, 0])
        MD = Line(M.get_center(),
            D.get_center())
        MA = Line(M.get_center(),
            A.get_center())
        ##################
        ### ANIMATIONS ###
        ##################
        self.play(FadeIn(circle),
            FadeIn(F), FadeIn(P), FadeIn(C), #FadeIn(B), FadeIn(G), FadeIn(H), FadeIn(E),
            FadeIn(F_label), FadeIn(P_label), FadeIn(C_label), FadeIn(B_label), FadeIn(G_label), FadeIn(H_label), FadeIn(E_label), FadeIn(D_label), FadeIn(A_label),
            FadeIn(FP), FadeIn(FC), FadeIn(FB), FadeIn(FG), FadeIn(FH), FadeIn(FE),
            FadeIn(BC), FadeIn(EC),
            FadeIn(M), FadeIn(CM), FadeIn(BM), FadeIn(EM),
            FadeIn(IK), FadeIn(CI), FadeIn(CK),
            FadeIn(MD), FadeIn(MA),
            run_time=1.5)
        self.play(C.animate.move_to(E.get_center()+[-0.1, 0.05, 0]), run_time=0.8)
        self.play(MoveAlongPath(C, EC_arc, run_time=0.5), Create(EC_arc, run_time=2))
        self.play(C.animate.move_to(B.get_center()+[0.1, 0.05, 0]), run_time=0.8)
        self.play(MoveAlongPath(C, BC_arc, run_time=0.5), Create(BC_arc, run_time=2))
       
        self.play(C.animate.move_to(B.get_center()))
       
        self.play(MoveAlongPath(C, BE_arc))
        self.play(MoveAlongPath(C, BE_arc_reverse))
        self.play(MoveAlongPath(C, BE_arc))
        self.play(MoveAlongPath(C, BE_arc_reverse))
        self.play(MoveAlongPath(C, BE_arc))
        self.play(MoveAlongPath(C, BE_arc_reverse))
        
        self.play(C.animate.move_to([F.get_x(),F.get_y()-circle.radius, 0]))
        
        
        self.wait(2)