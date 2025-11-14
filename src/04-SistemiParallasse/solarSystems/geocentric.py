from manim import *

class SolarSystemGeocentric(MovingCameraScene):
    def construct(self):
        nome = Tex("Tolomeo").to_corner(UL)
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
        
        # Compute orbit radii for planets orbiting Earth (excluding Earth itself)
        orbit_radii = [abs(p.get_y() - planets[0].get_y()) for p in planets[1:]]
        
        for i in range(0, len(planets_names)):
            planets_names[i]\
                .move_to(planets[i].get_center())\
                .shift(RIGHT* planets[i].radius)\
                .shift(RIGHT* (planets_names[i].length_over_dim(0)/2))\
                .shift(RIGHT* 0.5)
        self.play(FadeIn(nome))
        for i in range(0, len(planets)):
            self.play(FadeIn(planets[i]), Write(planets_names[i]), run_time=0.5)
        self.play(FadeOut(planets_names))
        
        # Add TracedPaths for all planets
        traces = VGroup()
        for planet in planets:
            trace = TracedPath(lambda p=planet: p.get_center(), stroke_color=planet.color, stroke_width=2, dissipating_time=0.5)
            traces.add(trace)
        self.add(traces)
        self.play(self.camera.frame.animate.set_width(config.frame_width*2))
        self.play(self.camera.frame.animate.shift(DOWN*3))
        planets_rotating = AnimationGroup(
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
        self.play(FadeOut(traces), run_time=0.5)
        self.wait(2)
        
        # Create and fade in orbits for all orbiting bodies at the end
        orbits = VGroup()
        earth_center = planets[0].get_center()
        for i, r in enumerate(orbit_radii):
            orbit = Circle(radius=r, color=planets[i+1].color, stroke_width=2)
            orbit.move_to(earth_center)
            orbits.add(orbit)
        self.play(FadeIn(orbits), run_time=2)
        self.wait(2)