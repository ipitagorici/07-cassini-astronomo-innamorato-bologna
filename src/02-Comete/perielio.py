from manim import *

class Perielio(Scene):
    def construct(self):
        circle = Circle(radius=2).set_color(WHITE)\
            .shift(UP)\
            .rotate(-90*DEGREES)
        F = Dot(circle.get_center())
        
        P = Dot([F.get_x(), F.get_y()+circle.radius+0.1, 0])
        C = Dot([F.get_x(), F.get_y()-circle.radius-0.1, 0])
        
        B = always_redraw(lambda: Dot(radius=0.1)\
            .move_to([C.get_x()-1.55, C.get_y()+0.7, 0]))
        G = always_redraw(lambda: Dot(radius=0.1)\
            .move_to([C.get_x()-0.8, C.get_y()+0.35, 0]))
        H = always_redraw(lambda: Dot(radius=0.1)\
            .move_to([C.get_x()+0.8, C.get_y()+0.35, 0]))
        E = always_redraw(lambda: Dot(radius=0.1)\
            .move_to([C.get_x()+1.55, C.get_y()+0.7, 0]))
        
        
        FP = always_redraw(lambda: Line(F, P))
        FC = always_redraw(lambda: Line(F, C))
        FB = always_redraw(lambda: Line(F, B))
        FG = always_redraw(lambda: Line(F, G))
        FH = always_redraw(lambda: Line(F, H))
        FE = always_redraw(lambda: Line(F, E))
        
        BC = Line(FB.get_end(), FC.get_end())
        EC = Line(FE.get_end(), FC.get_end())
        
        M = Dot([FC.get_end()[0], FC.get_end()[1]-1.25, 0])
        CM = Line(M.get_center(), FC.get_end())
        BM = Line(M.get_center(), FB.get_end())
        EM = Line(M.get_center(), FE.get_end())
        
        IK = Line([FC.get_end()[0]-circle.radius, FC.get_end()[1], 0],
            [FC.get_end()[0]+circle.radius, FC.get_end()[1], 0])
        CI = Line(FC.get_end(),
            [IK.get_start()[0], IK.get_start()[1]-circle.radius/2, 0])
        CK = Line(FC.get_end(),
            [IK.get_end()[0], IK.get_end()[1]-circle.radius/2, 0])
        
        MD = Line(M.get_center(),
            [FC.get_end()[0]-0.45, FC.get_end()[1]-0.2, 0])
        MA = Line(M.get_center(),
            [FC.get_end()[0]+0.45, FC.get_end()[1]-0.2, 0])
        
        self.play(FadeIn(circle), FadeIn(F),
                 FadeIn(FP), FadeIn(FC), FadeIn(FB), FadeIn(FG), FadeIn(FH), FadeIn(FE),
                 FadeIn(BC), FadeIn(EC),
                 FadeIn(M), FadeIn(CM), FadeIn(BM), FadeIn(EM),
                 FadeIn(IK), FadeIn(CI), FadeIn(CK),
                 FadeIn(MD), FadeIn(MA))
                
        
        self.wait(2)