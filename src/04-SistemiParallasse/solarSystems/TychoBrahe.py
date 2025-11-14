from manim import *
from manim.utils.space_ops import rotate_vector
import numpy as np
from math import floor, pi

class SolarSystemTychoBrahe(MovingCameraScene):
    def construct(self):
        nome = Tex("Tycho Brahe").to_corner(UL)
        distance = 0.45
        T = 5 # base rotation duration in seconds
        speed_factor = 3.0 # Set to three as requested
        # === Celestial bodies ===
        earth = Dot((0, -3.5, 0), radius=0.2, color=GREEN)
        moon = Dot((0, 0, 0), radius=0.09, color=GREY)
        sun = Dot((0, 0, 0), radius=0.9, color=YELLOW)
        mercury = Dot((0, 0, 0), radius=0.1, color=YELLOW_E)
        venus = Dot((0, 0, 0), radius=0.15, color=ORANGE)
        mars = Dot((0, 0, 0), radius=0.1, color=RED)
        jupiter = Dot((0, 0, 0), radius=0.35, color=DARK_BROWN)
        saturn = Dot((0, 0, 0), radius=0.4, color=YELLOW_E)
        planets = [earth, moon, sun, mercury, venus, mars, jupiter, saturn]
        planet_names = VGroup(
            Tex("Terra"), Tex("Luna"), Tex("Sole"),
            Tex("Mercurio"), Tex("Venere"), Tex("Marte"), Tex("Giove"), Tex("Saturno")
        )
        # === Position planets vertically ===
        for i, planet in enumerate(planets):
            if i == 0:
                planet.move_to((0, -4 + planet.radius + 0.1, 0))
            else:
                prev = planets[i - 1]
                offset = distance / 2 if planet.radius == 0.09 else distance
                planet.move_to(
                    (0, prev.get_center()[1] + offset + planet.radius + prev.radius, 0)
                )
        # === Position labels ===
        for i, name in enumerate(planet_names):
            name.next_to(planets[i], RIGHT)
        self.play(FadeIn(nome))
        # === Show planets and labels ===
        for i in range(len(planets)):
            self.play(FadeIn(planets[i]), Write(planet_names[i]), run_time=0.4)
        self.play(FadeOut(planet_names))
        # === References ===
        earth_center = earth
        sun_center = sun
        # === Orbit structure ===
        earth_orbiting_bodies = [moon, sun] # orbit Earth
        sun_orbiting_bodies = [mercury, venus, mars, jupiter, saturn] # orbit Sun
        # === Initial offsets ===
        offsets_earth = {p: p.get_center() - earth_center.get_center() for p in earth_orbiting_bodies}
        offsets_sun = {p: p.get_center() - sun_center.get_center() for p in sun_orbiting_bodies}
        # === Compute distances ===
        dist_earth = {p: np.linalg.norm(offset) for p, offset in offsets_earth.items()}
        dist_sun = {p: np.linalg.norm(offset) for p, offset in offsets_sun.items()}
        # === Correct Keplerian angular speeds ===
        # Earth system
        a_inner_earth = dist_earth[moon]
        omega_base_earth = speed_factor * TAU / (T / 2)
        # Sun system
        a_inner_sun = dist_sun[mercury]
        omega_base_sun = speed_factor * TAU / (T / 3)
        # === Speeds ===
        speeds = {}
        for planet in earth_orbiting_bodies:
            a = dist_earth[planet]
            speeds[planet] = omega_base_earth * (a_inner_earth / a) ** 1.5
        for planet in sun_orbiting_bodies:
            a = dist_sun[planet]
            speeds[planet] = omega_base_sun * (a_inner_sun / a) ** 1.5
        # === Staggered start times ===
        order = [moon, sun, mercury, venus, mars, jupiter, saturn]
        start_times = {}
        st = 0.0
        for p in order:
            start_times[p] = st
            st += 0.5
        # Override: sun-orbiting bodies start at the same time as sun
        sun_start = start_times[sun]
        for p in sun_orbiting_bodies:
            start_times[p] = sun_start
        # === Compute align times with staggered starts ===
        align_t = {}
        TAU_EPS = 1e-8
        # For moon: check after 5 seconds from global start
        check_time_moon = 5.0
        effective_dt_moon = check_time_moon - start_times[moon]
        orbits_moon = speeds[moon] * effective_dt_moon / TAU
        num_moon = floor(orbits_moon + TAU_EPS)
        next_o_moon = num_moon + 1
        align_effective_dt_moon = next_o_moon * TAU / speeds[moon]
        align_t[moon] = start_times[moon] + align_effective_dt_moon
        # For sun: after moon stops
        speed_sun_obj = speeds[sun]
        effective_dt_at_moon_stop_for_sun = align_t[moon] - start_times[sun]
        orbits_sun = speed_sun_obj * effective_dt_at_moon_stop_for_sun / TAU
        num_sun = floor(orbits_sun + TAU_EPS)
        next_o_sun = num_sun + 1
        align_effective_dt_sun = next_o_sun * TAU / speed_sun_obj
        align_t[sun] = start_times[sun] + align_effective_dt_sun
        # For sun-orbiting bodies: after sun stops
        for p in sun_orbiting_bodies:
            speed = speeds[p]
            effective_dt_at_sun_stop = align_t[sun] - start_times[p]
            orbits = speed * effective_dt_at_sun_stop / TAU
            num = floor(orbits + TAU_EPS)
            next_o = num + 1
            align_effective_dt = next_o * TAU / speed
            align_t[p] = start_times[p] + align_effective_dt
        max_align_t = max(align_t.values())
        # === Time tracker ===
        t = ValueTracker(0)
        # === Updaters with staggered starts, alignment stops, and snap ===
        def add_orbital_updater(planet, center, offset, speed, start_t, align_effective_dt):
            def updater(m):
                dt = t.get_value()
                effective_dt = max(0, dt - start_t)
                if effective_dt >= align_effective_dt:
                    m.move_to(center.get_center() + offset)
                    m.clear_updaters()
                    return
                total_angle = speed * effective_dt
                angle = total_angle % TAU
                m.move_to(center.get_center() + rotate_vector(offset, angle))
            planet.add_updater(updater)
        for planet in earth_orbiting_bodies:
            offset = offsets_earth[planet]
            speed = speeds[planet]
            start_t = start_times[planet]
            align_effective_dt = align_t[planet] - start_t
            add_orbital_updater(planet, earth_center, offset, speed, start_t, align_effective_dt)
        for planet in sun_orbiting_bodies:
            offset = offsets_sun[planet]
            speed = speeds[planet]
            start_t = start_times[planet]
            align_effective_dt = align_t[planet] - start_t
            add_orbital_updater(planet, sun_center, offset, speed, start_t, align_effective_dt)
        # === Trails ===
        trails = []
        orbiting_bodies = earth_orbiting_bodies + sun_orbiting_bodies
        for planet in orbiting_bodies:
            trail = TracedPath(planet.get_center, stroke_color=planet.color, stroke_width=3, dissipating_time=0.5)
            trails.append(trail)
            self.add(trail)
        self.play(self.camera.frame.animate.set_width(config.frame_width*2))
        self.play(self.camera.frame.animate.shift(DOWN*3))
        # === Animation ===
        self.play(t.animate.set_value(max_align_t), run_time=max_align_t, rate_func=linear)
        self.wait(2)

        # === Final diagram setup ===
        # Fade out trails
        self.play(FadeOut(VGroup(*trails)), run_time=1)

        # Define desired angles for final positions (adjusted to spread out like a typical diagram)
        earth_orbit_angles = {
            moon: 4 * pi / 5,  # ~144 degrees, upper left
            sun: pi / 5,       # ~36 degrees, upper right
        }
        sun_orbit_angles = {
            mercury: 0,        # 0 degrees, right
            venus: 2 * pi / 5, # ~72 degrees, upper right
            mars: 4 * pi / 5,  # ~144 degrees, upper left
            jupiter: 6 * pi / 5, # ~216 degrees, lower left
            saturn: 8 * pi / 5,  # ~288 degrees, lower right
        }

        # Compute target positions
        target_positions = {}
        # Moon
        angle = earth_orbit_angles[moon]
        target_positions[moon] = earth.get_center() + dist_earth[moon] * np.array([np.cos(angle), np.sin(angle), 0])
        # Sun
        angle = earth_orbit_angles[sun]
        target_sun = earth.get_center() + dist_earth[sun] * np.array([np.cos(angle), np.sin(angle), 0])
        target_positions[sun] = target_sun
        # Sun-orbiting bodies
        for p in sun_orbiting_bodies:
            rel_angle = sun_orbit_angles[p]
            target = target_sun + dist_sun[p] * np.array([np.cos(rel_angle), np.sin(rel_angle), 0])
            target_positions[p] = target

        # Animate planets to final positions
        moves = [obj.animate.move_to(pos) for obj, pos in target_positions.items()]
        self.play(*moves, run_time=3)

        # Now draw orbits at final centers
        sun_center_final = sun.get_center()
        moon_orbit = Circle(radius=dist_earth[moon], color=moon.color, stroke_width=2, stroke_opacity=0.7).move_to(earth.get_center())
        sun_orbit = Circle(radius=dist_earth[sun], color=sun.color, stroke_width=2, stroke_opacity=0.7).move_to(earth.get_center())
        merc_orbit = Circle(radius=dist_sun[mercury], color=mercury.color, stroke_width=2, stroke_opacity=0.7).move_to(sun_center_final)
        venus_orbit = Circle(radius=dist_sun[venus], color=venus.color, stroke_width=2, stroke_opacity=0.7).move_to(sun_center_final)
        mars_orbit = Circle(radius=dist_sun[mars], color=mars.color, stroke_width=2, stroke_opacity=0.7).move_to(sun_center_final)
        jupiter_orbit = Circle(radius=dist_sun[jupiter], color=jupiter.color, stroke_width=2, stroke_opacity=0.7).move_to(sun_center_final)
        saturn_orbit = Circle(radius=dist_sun[saturn], color=saturn.color, stroke_width=2, stroke_opacity=0.7).move_to(sun_center_final)
        orbits_group = VGroup(moon_orbit, sun_orbit, merc_orbit, venus_orbit, mars_orbit, jupiter_orbit, saturn_orbit)
        self.play(Create(orbits_group), run_time=2)
        self.wait(3)