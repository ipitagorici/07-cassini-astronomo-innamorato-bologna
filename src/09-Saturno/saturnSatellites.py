from manim import *
import numpy as np


class Satellites(ThreeDScene):
    def construct(self):
        my_tex_template = TexTemplate()
        my_tex_template.preamble += r"\usepackage{musixtex}"        
        
        saturn_axes = Axes(
            (-1, 1, 1), (-1, 1, 1),
            4, 4,
            tips=False
        ).shift(LEFT * 3.5).shift(UP * 0.8)

        saturn = Circle(1.5, YELLOW_A).set_fill(opacity=0.5) \
            .move_to(saturn_axes.get_center())

        satellite_trackers = [ValueTracker(0.00000000000001), ValueTracker(0.00000000000001),
                              ValueTracker(0.00000000000001)]

        orbit_radius = ValueTracker(0.00000000000001)

        saturn_orbit = always_redraw(lambda:
            Circle(orbit_radius.get_value() * 2, color=DARK_BROWN) \
            .move_to(saturn_axes.get_center()))

        saturn_orbit_equations = [
            lambda t: np.array([
                1.25 * np.cos(t),
                1.25 * np.sin(t),
                0,
            ]),
            lambda t: np.array([
                1 * np.cos(t),
                1 * np.sin(t),
                0,
            ]),
            lambda t: np.array([
                1.5 * np.cos(t),
                1.5 * np.sin(t),
                0,
            ]),
        ]

        saturn_orbit_functions = [
            always_redraw(lambda:
                saturn_axes.plot_parametric_curve(
                    saturn_orbit_equations[0],
                    t_range=[0, satellite_trackers[0].get_value()],
                ).set_opacity(0)
            ),
            always_redraw(lambda:
                saturn_axes.plot_parametric_curve(
                    saturn_orbit_equations[1],
                    t_range=[0, satellite_trackers[1].get_value()],
                ).set_opacity(0)
            ),
            always_redraw(lambda:
                saturn_axes.plot_parametric_curve(
                    saturn_orbit_equations[2],
                    t_range=[0 , satellite_trackers[2].get_value()],
                ).set_opacity(0)
            ),
        ]

        satellites = []

        axes = Axes(
            (0, 4*PI, PI/3), (-1, 1, 1),
            5.5, 3,
            tips=False
        ).shift(RIGHT * 4).shift(UP)

        satellite_equations = [lambda x: np.sin(x),
                               lambda x: np.sin(2*x),
                               lambda x: np.sin(x/2)]
        satellite_functions = [
            always_redraw(lambda: axes.plot(satellite_equations[0], x_range=[0, satellite_trackers[0].get_value()])),
            always_redraw(lambda: axes.plot(satellite_equations[1], x_range=[0, satellite_trackers[1].get_value()])),
            always_redraw(lambda: axes.plot(satellite_equations[2], x_range=[0, satellite_trackers[2].get_value()])), ]

        self.play(Create(saturn))
        self.play(Create(saturn_orbit))

        self.play(Create(axes))

        satellites_groups = VGroup()

        for i in range(0, 3):
            if i == 0:
                self.play(orbit_radius.animate.set_value(1.25))
            elif i == 1:
                self.play(orbit_radius.animate.set_value(1))
            else:
                self.play(orbit_radius.animate.set_value(1.5))
            self.add(saturn_orbit_functions[i])

            current_satellite = always_redraw(lambda: Dot(saturn_orbit_functions[i].get_start(), 0.2, color=DARK_BROWN)
                .move_to(saturn_orbit_functions[i].get_end()))

            self.play(Create(current_satellite))
            satellites.append(current_satellite)

            self.add(satellite_functions[i])

            self.play(satellite_trackers[i].animate.set_value(4 * PI),
                      run_time=4, rate_func=linear)

            satellite_group = VGroup(saturn.copy(), satellites[i].copy(), saturn_orbit.copy(), axes.copy(),
                satellite_functions[i].copy())
            satellites_groups.add(satellite_group)
            self.play(satellites_groups[i].animate.scale(0.2))

            if i == 0:
                self.play(satellites_groups[i].animate.to_corner(DL))
            elif i == 1:
                self.play(satellites_groups[i].animate.to_edge(DOWN))
            else:
                self.play(satellites_groups[i].animate.to_corner(DR))

            self.play(satellite_trackers[i].animate.set_value(0.00000000000001))
            frozen_satellite_snapshot = satellites[i].copy().clear_updaters()
            self.remove(satellites[i])
            self.add(frozen_satellite_snapshot)
            self.play(FadeOut(frozen_satellite_snapshot, run_time=0.5))

            self.play(satellite_trackers[i].animate.set_value(0.00000000000001))

            self.remove(satellite_functions[i])
            self.remove(saturn_orbit_functions[i])

        saturn_orbit_snapshot = saturn_orbit.copy().clear_updaters()
        self.add(saturn_orbit_snapshot)
        self.remove(saturn_orbit)
        self.play(FadeOut(saturn, saturn_orbit_snapshot, axes))

        self.play(satellites_groups.animate.shift(UP*3))

        axes = Axes(
            (-PI, PI, PI/4), (-1.5, 1.5, 1),
            5.5, 3,
            tips=False
        ).shift(RIGHT * 4).shift(UP)
        BLUE_FIGO = ManimColor("#3679ff")
        t = ValueTracker(1.5)
        final_satellite_tracker = ValueTracker(-PI+0.0000000000001)
        final_satellite_equation = lambda x: -t.get_value() * 2.718**(-(x+.065)**2) *np.sin(-3 * (np.arctan((x+.065)) + 2) * PI * (x+.065))
        final_satellite_function = always_redraw(
            lambda: axes.plot(final_satellite_equation, x_range=[-PI, final_satellite_tracker.get_value()],color=BLUE_FIGO))
        final_satellite_group = VGroup(axes, final_satellite_function)

        orbit_radius.set_value(1.5)
        saturn_group = VGroup(
            saturn, saturn_orbit, saturn_orbit_functions[0], saturn_orbit_functions[1], saturn_orbit_functions[2]
        )

        self.play(Transform(satellites_groups, final_satellite_group, replace_mobject_with_target_in_scene=True))
        self.play(GrowFromEdge(saturn_group, RIGHT))

        saturn_sphere = (Sphere(saturn.get_center(), saturn.get_width() / 2,)
            .set_color(YELLOW_A).set_fill(opacity=0.5))
        self.play(Transform(saturn, saturn_sphere, replace_mobject_with_target_in_scene=True))

        self.play(self.camera.phi_tracker.animate.set_value(90 * DEGREES), axes.animate.rotate(90 * DEGREES, axis=X_AXIS))

        satellites_spheres = [
            always_redraw(lambda: Sphere(satellites[0].get_center(), satellites[0].get_width() / 2)
                .set_color(DARK_BROWN).move_to(saturn_orbit_functions[0].get_end())),
            always_redraw(lambda: Sphere(satellites[1].get_center(), satellites[1].get_width() / 2)
            .set_color(DARK_BROWN).move_to(saturn_orbit_functions[1].get_end())),
            always_redraw(lambda: Sphere(satellites[2].get_center(), satellites[2].get_width() / 2)
            .set_color(DARK_BROWN).move_to(saturn_orbit_functions[2].get_end()))
        ]
        self.play(FadeIn(satellites_spheres[0], satellites_spheres[1], satellites_spheres[2]))
        self.play(satellite_trackers[0].animate.set_value(16*PI),
                  satellite_trackers[1].animate.set_value(8*PI),
                  satellite_trackers[2].animate.set_value(4*PI),
                  final_satellite_tracker.animate.set_value(PI),
                  run_time=8, rate_func=linear)

        self.play(axes.animate.rotate(-90 * DEGREES, axis=X_AXIS), FadeOut(final_satellite_function))
        
        pentagram = VGroup(
            Line(axes.c2p(-PI, PI/4), axes.c2p(PI-2, PI/4)),
            Line(axes.c2p(-PI, PI/8), axes.c2p(PI-2, PI/8)),
            Line(axes.c2p(-PI, 0), axes.c2p(PI-2, 0)),
            Line(axes.c2p(-PI, -PI/8), axes.c2p(PI-2, -PI/8)),
            Line(axes.c2p(-PI, -PI/4), axes.c2p(PI-2, -PI/4)),
        )
        treble_clef_tex = Tex(r"\begin{music}\trebleclef\end{music}",
            tex_template=my_tex_template,
            font_size=60
        )
        treble_clef_tex.move_to(pentagram[2].get_start())
        pentagram.add(treble_clef_tex)
        
        self.play(
            Transform(axes, pentagram, replace_mobject_with_target_in_scene=True),
            self.camera.phi_tracker.animate.set_value(0 * DEGREES))
        
        satellites_notes_dots = VGroup(
            Dot((pentagram[4].get_start()[0]+0.5, pentagram[4].get_start()[1], 0), radius=0.1),
            Dot((pentagram[2].get_start()[0]+2, pentagram[2].get_start()[1], 0), radius=0.1),
            Dot((pentagram[0].get_end()[0]-0.5, pentagram[0].get_end()[1], 0), radius=0.1)
        )
        satellites_notes = VGroup(
            VGroup(
                satellites_notes_dots[0],
                Line(
                    (satellites_notes_dots[0].get_center()[0]+0.05, satellites_notes_dots[0].get_center()[1], 0),
                    (satellites_notes_dots[0].get_center()[0]+0.05, satellites_notes_dots[0].get_center()[1] - 0.5, 0)
                )
            ),
            VGroup(
                satellites_notes_dots[1],
                Line(
                    (satellites_notes_dots[1].get_center()[0]+0.05, satellites_notes_dots[1].get_center()[1], 0),
                    (satellites_notes_dots[1].get_center()[0]+0.05, satellites_notes_dots[1].get_center()[1] + 0.5, 0)
                )
            ),
            VGroup(
                satellites_notes_dots[2],
                Line(
                    (satellites_notes_dots[2].get_center()[0]+0.05, satellites_notes_dots[2].get_center()[1], 0),
                    (satellites_notes_dots[2].get_center()[0]+0.05, satellites_notes_dots[2].get_center()[1] + 0.5, 0)
                )
            )
        )
        
        self.play(
            Transform(satellites_spheres[0], satellites_notes[0], replace_mobject_with_target_in_scene=True),
            Transform(satellites_spheres[1], satellites_notes[1], replace_mobject_with_target_in_scene=True),
            Transform(satellites_spheres[2], satellites_notes[2], replace_mobject_with_target_in_scene=True)
        )

        self.wait(2)
