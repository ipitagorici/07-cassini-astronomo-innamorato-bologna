from manim import *
class SolarSystemGeocentric(Scene):
    def construct(self):
        distance = 0.45
        
        earth = Dot(
            (0, -3.5, 0),
            0.2,
            color=GREEN
        )
        moon = Dot(
            (0, 0, 0),
            0.09,
            color=GREY
        ) 
        mercury = Dot(
            (0, 0, 0),
            0.1,
            color=YELLOW
        )
        venus = Dot(
            (0, 0, 0),
            0.2,
            color=ORANGE
        )
        sun = Dot(
            (0, 0, 0),
            0.9,
            color=YELLOW
        )
        mars = Dot(
            (0, 0, 0),
            0.1,
            color=RED
        )
        jupiter = Dot(
            (0, 0, 0),
            0.4,
            color=DARK_BROWN
        )
        saturn = Dot(
            (0, 0, 0),
            0.4,
            color=YELLOW_E
        )
        
        planets = [
            earth, moon, mercury, venus, sun, mars, jupiter, saturn
        ]
        planets_names = VGroup(
            Tex("Terra"), Tex("Luna"), Tex("Mercurio"), Tex("Venere"), Tex("Sole"), Tex("Marte"), Tex("Giove"), Tex("Saturno") 
        )

        for i in range(0, len(planets)):
            if i == 0:
                planets[i].move_to((0, -4 + planets[i].radius + 0.1, 0))
                continue
            if planets[i].radius == 0.09:
                ignored_distance = planets[i].radius + planets[i-1].radius
                planets[i].move_to((0, planets[i-1].get_center()[1] + distance/2 + ignored_distance, 0))
            else:
                ignored_distance = planets[i].radius + planets[i-1].radius
                planets[i].move_to((0, planets[i-1].get_center()[1] + distance + ignored_distance, 0))

        for i in range(0, len(planets_names)):
            planets_names[i]\
                .move_to(planets[i].get_center())\
                .shift(RIGHT* planets[i].radius)\
                .shift(RIGHT* (planets_names[i].length_over_dim(0)/2))\
                .shift(RIGHT* 0.5)
                
        for i in range(0, len(planets)):
            self.play(FadeIn(planets[i]), Write(planets_names[i]), run_time=0.5)
    
        mercury_orbit = Circle(planets[4].get_center()[1] - planets[2].get_center()[1], color=BLACK)\
            .rotate(-90*DEGREES)\
            .add_updater(lambda x: x.move_to(planets[4].get_center()))\
            .move_to(planets[4].get_center())
        venus_orbit = Circle(planets[4].get_center()[1] - planets[3].get_center()[1], color=BLACK)\
            .rotate(-90*DEGREES)\
            .add_updater(lambda x: x.move_to(planets[4].get_center()))\
            .move_to(planets[4].get_center())
        
        self.play(FadeOut(planets_names))
        
        self.add(mercury_orbit, venus_orbit) 
    
        planets_rotating = AnimationGroup (
            Rotate(planets[1], TAU*7, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[2], TAU*6, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[3], TAU*5, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[4], TAU*4, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[5], TAU*3, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[6], TAU*2, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[7], TAU*1, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            lag_ratio=0.1
        )
        
        self.play(planets_rotating)
        
        self.wait(2)