from manim import *
import math # Not strictly needed here, but in case
import numpy as np

class SolarSystemEraclide(MovingCameraScene):
    def construct(self):
        nome = Tex("Eraclide").to_corner(UL)
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
            earth, moon, venus, mercury, sun, mars, jupiter, saturn
        ]
        planets_names = VGroup(
            Tex("Terra"), Tex("Luna"), Tex("Venere"), Tex("Mercurio"), Tex("Sole"), Tex("Marte"), Tex("Giove"), Tex("Saturno")
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
        self.play(FadeIn(nome))
        for i in range(0, len(planets)):
            self.play(FadeIn(planets[i]), Write(planets_names[i]), run_time=0.5)
        
        # Animate shift of inner system down to prevent orbit overlap
        delta = 1.0
        inner_planets = planets[:5]
        inner_names = planets_names[:5]
        self.play(
            *[p.animate.shift(DOWN * delta) for p in inner_planets],
            *[n.animate.shift(DOWN * delta) for n in inner_names],
            run_time=2
        )
        
        # Updaters for Venus and Mercury
        rel_pos_venus = planets[2].get_center() - planets[4].get_center()
        radius_venus = np.linalg.norm(rel_pos_venus)
        initial_angle_venus = np.arctan2(rel_pos_venus[1], rel_pos_venus[0])
        venus_angle = ValueTracker(initial_angle_venus)
        planets[2].add_updater(
            lambda m: m.move_to(
                planets[4].get_center() +
                radius_venus * np.array([
                    np.cos(venus_angle.get_value()),
                    np.sin(venus_angle.get_value()),
                    0
                ])
            )
        )
        rel_pos_mercury = planets[3].get_center() - planets[4].get_center()
        radius_mercury = np.linalg.norm(rel_pos_mercury)
        initial_angle_mercury = np.arctan2(rel_pos_mercury[1], rel_pos_mercury[0])
        mercury_angle = ValueTracker(initial_angle_mercury)
        planets[3].add_updater(
            lambda m: m.move_to(
                planets[4].get_center() +
                radius_mercury * np.array([
                    np.cos(mercury_angle.get_value()),
                    np.sin(mercury_angle.get_value()),
                    0
                ])
            )
        )
        moon_radius = abs(planets[1].get_center()[1] - planets[0].get_center()[1])
        moon_orbit = Circle(moon_radius, color=BLACK)\
            .move_to(planets[0].get_center())\
            .rotate(-90*DEGREES)
        self.play(FadeOut(planets_names))
        self.add(moon_orbit)
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
        mercury_anim = mercury_angle.animate.set_value(initial_angle_mercury + TAU).set_run_time(5).set_rate_func(linear)
        venus_anim = venus_angle.animate.set_value(initial_angle_venus + TAU).set_run_time(5).set_rate_func(linear)
        self.play(self.camera.frame.animate.set_width(config.frame_width*2))
        self.play(self.camera.frame.animate.shift(DOWN*3))
        planets_rotating = AnimationGroup(
            Rotate(planets[1], TAU*5, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
            mercury_anim,
            venus_anim,
            Rotate(planets[4], TAU*4, about_point=planets[0].get_center(), rate_func=linear, run_time=5),
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
        earth_center = planets[0].get_center()
        # Moon orbit around Earth
        moon_r = np.linalg.norm(planets[1].get_center() - earth_center)
        moon_final_orbit = Circle(radius=moon_r, color=planets[1].color, stroke_width=2)
        moon_final_orbit.move_to(earth_center)
        orbits.add(moon_final_orbit)
        # Sun orbit around Earth
        sun_r = np.linalg.norm(planets[4].get_center() - earth_center)
        sun_orbit = Circle(radius=sun_r, color=planets[4].color, stroke_width=2)
        sun_orbit.move_to(earth_center)
        orbits.add(sun_orbit)
        # Mars orbit around Earth
        mars_r = np.linalg.norm(planets[5].get_center() - earth_center)
        mars_orbit = Circle(radius=mars_r, color=planets[5].color, stroke_width=2)
        mars_orbit.move_to(earth_center)
        orbits.add(mars_orbit)
        # Jupiter orbit around Earth
        jup_r = np.linalg.norm(planets[6].get_center() - earth_center)
        jup_orbit = Circle(radius=jup_r, color=planets[6].color, stroke_width=2)
        jup_orbit.move_to(earth_center)
        orbits.add(jup_orbit)
        # Saturn orbit around Earth
        sat_r = np.linalg.norm(planets[7].get_center() - earth_center)
        sat_orbit = Circle(radius=sat_r, color=planets[7].color, stroke_width=2)
        sat_orbit.move_to(earth_center)
        orbits.add(sat_orbit)
        # Venus orbit around Sun
        venus_orbit = Circle(radius=radius_venus, color=planets[2].color, stroke_width=2)
        venus_orbit.add_updater(lambda v: v.move_to(planets[4].get_center()))
        orbits.add(venus_orbit)
        # Mercury orbit around Sun
        mercury_orbit = Circle(radius=radius_mercury, color=planets[3].color, stroke_width=2)
        mercury_orbit.add_updater(lambda m: m.move_to(planets[4].get_center()))
        orbits.add(mercury_orbit)
        self.play(FadeIn(orbits), run_time=2)
        self.wait(2)