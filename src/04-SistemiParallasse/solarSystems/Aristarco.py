from manim import *
import math # Not strictly needed here, but in case

class SolarSystemAristarco(MovingCameraScene):
    def construct(self):
        nome = Tex("Copernico").to_corner(UL)
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
            sun, mercury, venus, earth, moon, mars, jupiter, saturn
        ]
        planets_names = VGroup(
            Tex("Sole"), Tex("Mercurio"), Tex("Venere"), Tex("Terra"), Tex("Luna"), Tex("Marte"), Tex("Giove"), Tex("Saturno")
        )
        for i in range(0, len(planets)):
            if i == 0:
                planets[i].move_to((0, -4 + planets[i].radius + 0.1, 0))
                continue
            if planets[i].radius != 0.09:
                ignored_distance = planets[i].radius + planets[i-1].radius
                planets[i].move_to((0, planets[i-1].get_center()[1] + distance + ignored_distance, 0))
            else:
                ignored_distance = planets[i].radius + planets[i-1].radius
                planets[i].move_to((0, planets[i-1].get_center()[1] + distance/2 + ignored_distance, 0))
        for i in range(0, len(planets_names)):
            planets_names[i]\
                .move_to(planets[i].get_center())\
                .shift(RIGHT* planets[i].radius)\
                .shift(RIGHT* (planets_names[i].width / 2))\
                .shift(RIGHT* 0.5)
        # Add fading trails for planets (excluding sun) using TracedPath
        trails = []
        # For a trail that fades/disappears after ~1 second, use dissipating_time=1.0
        dissipating_time = 0.5
        for i in range(1, len(planets)):
            planet = planets[i]
            trail = TracedPath(
                planet.get_center,
                stroke_color=planet.color,
                stroke_width=3,
                dissipating_time=dissipating_time,
                stroke_opacity=[0, 1]
            )
            self.add(trail)
            trails.append(trail)
        self.play(Write(nome))
        for i in range(0, len(planets)):
            self.play(FadeIn(planets[i]), Write(planets_names[i]), run_time=0.5)
        moon_orbit = Circle(planets[3].get_center()[1] - planets[4].get_center()[1], color=BLACK)\
            .rotate(-90*DEGREES)\
            .add_updater(lambda x: x.move_to(planets[3].get_center()))
        self.play(FadeOut(planets_names))
        self.add(moon_orbit)
        self.play(self.camera.frame.animate.set_width(config.frame_width*2))
        self.play(self.camera.frame.animate.shift(DOWN*3))
        planets_rotating = AnimationGroup (
            Rotate(planets[1], TAU*6, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[2], TAU*5, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            AnimationGroup(
                Rotate(planets[3], TAU*4, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
                MoveAlongPath(moon, moon_orbit, rate_func=linear, run_time=5),
            ),
            Rotate(planets[5], TAU*3, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[6], TAU*2, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            Rotate(planets[7], TAU*1, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            lag_ratio=0.1
        )
        self.play(planets_rotating)
        # Optional: Remove trails after animation
        self.play(*[FadeOut(trail) for trail in trails])
        self.play(FadeOut(moon_orbit))
        self.wait(2)
        
        # Create and fade in orbits for all orbiting bodies at the end
        orbits = VGroup()
        sun_center = planets[0].get_center()
        orbiting_planets = [planets[1], planets[2], planets[3], planets[5], planets[6], planets[7]]
        for p in orbiting_planets:
            r = abs(p.get_y() - sun_center[1])
            orbit = Circle(radius=r, color=p.color, stroke_width=2)
            orbit.move_to(sun_center)
            orbits.add(orbit)
        
        # Add moon's orbit around Earth
        moon_radius = abs(planets[4].get_y() - planets[3].get_y())
        moon_final_orbit = Circle(radius=moon_radius, color=planets[4].color, stroke_width=2)
        moon_final_orbit.add_updater(lambda m: m.move_to(planets[3].get_center()))
        orbits.add(moon_final_orbit)
        
        self.play(FadeIn(orbits), run_time=2)
        self.wait(2)