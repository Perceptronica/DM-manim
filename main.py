from manim import *
import numpy as np
import math

equation = Tex(
    "$p(x, y)$", " $=$ ", "${x^2}{y^6}$", " $-$ ", "${2x^4}{y^5}$", " $+$ ", "${x^6}{y^4}$", " $+$ ", "$y^{10}$",
    " $-$ ", "${10x}{y^9}$", " $-$ ", "${0.1x^8}{y^4}$",
    color=BLACK)
monoms = equation[2::2]
monoms_text = ["${x^2}{y^6}$", "${2x^4}{y^5}$", "${x^6}{y^4}$", "$y^{10}$", "${10x}{y^9}$", "${0.1x^8}{y^4}$"]
sign = ['', '$-$', '', '', '$-$', '$-$']
points = [(2, 6), (4, 5), (6, 4), (0, 10), (1, 9), (8, 4)]
monoms_func = [Tex(f"{sign[i]}{monoms_text[i]} $\mapsto ({points[i][0]}, {points[i][1]})$ \\", color=BLACK) for i in
               range(len(points))]
f1 = Tex(r"${\varphi_1^{(1,2)}} = x^2y^6 - 2x^4y^5 + x^6y^4 = x^2y^4(y - x^2)^2,$", color=BLACK)
f11 = Tex(r"$\forall k \in N_{\varphi_1^{(1,2)}} \Rightarrow \langle(1, 2), k\rangle = 14$", color=BLACK)
f2 = Tex(r"${\varphi_2^{(1,2)}} = -0.1x^8y^4, \forall k \in N_{\varphi_2^{(1,2)}} \Rightarrow \langle(1, 2), k\rangle = 16$", color=BLACK)
f3 = Tex(r"${\varphi_3^{(1,2)}} = -10xy^9, \forall k \in N_{\varphi_3^{(1,2)}} \Rightarrow \langle(1, 2), k\rangle = 19$", color=BLACK)
f4 = Tex(r"${\varphi_4^{(1,2)}} = y^{10}, \forall k \in N_{\varphi_4^{(1,2)}} \Rightarrow \langle(1, 2), k\rangle = 20$", color=BLACK)
H1 = Tex(
    r"$H_{\varphi^A_1} = $ \textbraceleft $x \in R^2 | x = 0$ \textbraceright $\cup$ \textbraceleft $x \in R^2 | y = 0$ \textbraceright $\cup$ \textbraceleft $x \in R^2 | y = x^2$ \textbraceright",
    color=BLACK)
p = Tex(
    r"$p(x, y) = \varphi_1^{(1, 2)}(x, y) + \varphi_2^{(1, 2)}(x, y) + \varphi_3^{(1, 2)}(x, y) + \varphi_4^{(1, 2)}(x, y)$",
    color=BLACK)
l3 = Tex(r"$(1, 1) \in H_{\varphi_1^{(1, 2)}}, \varphi_2^{(1, 2)}(1, 1) = -0,1 \Rightarrow (0, 0)$", color=BLACK)

class Scene1(Scene):
    def construct(self):
        myTexTemplate = TexTemplate(tex_compiler="xelatex",
                                    output_format='.xdv', preamble=r"""
            \usepackage{cmap}
            \usepackage[english, russian]{babel}
            \usepackage[utf8]{inputenc}
            \usepackage[T2A,T1]{fontenc}
            \usepackage{mathtext}
            \usepackage{amsmath, amsfonts, amssymb, amsthm, mathtools}
            \usepackage{lmodern}
            """)
        MathTex.set_default(tex_template=myTexTemplate)
        Tex.set_default(tex_template=myTexTemplate)
        register_font("Computer Modern Roman")
        self.camera.background_color = WHITE
        self.play(Write(equation))
        self.wait(7.5)


        self.play(FadeToColor(monoms, color=RED))
        self.wait(3.5)
        text = Text("одночлены", font_size=30, color=BLACK)
        text.shift(DOWN)
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))
        self.play(FadeToColor(monoms, color=BLACK))
        self.play(equation.animate.to_edge(UP))
        self.wait()
        text = Text("векторы степеней:", font_size=30, color=BLACK)
        text.shift(2.65 * UP)
        self.play(FadeIn(text))
        #self.wait()
        monoms_func[0].shift(2 * UP)
        monoms_func[1].shift(1 * UP)
        # monoms_func[2].shift()
        monoms_func[3].shift(DOWN)
        monoms_func[4].shift(2 * DOWN)
        monoms_func[5].shift(3 * DOWN)
        for i in range(len(monoms)):
            self.play(FadeToColor(monoms[i], color=RED, run_time=0.2))
            self.play(Write(monoms_func[i], run_time=0.5))
            self.play(FadeToColor(monoms[i], color=BLACK, run_time=0.2))
        self.wait()
        self.play(FadeOut(text, run_time=0.2))
        for i in range(len(monoms)):
            self.play(FadeOut(monoms_func[i], run_time=0.2))
        Np = Tex("$N_p = \{$", "$(2, 6)$", ",", " $(4, 5)$", ",", " $(6, 4)$", ",", " $(0, 10)$", ",", " $(1, 9)$", ",",
                 " $(8, 4)$", "$\}$", color=BLACK)
        Np.shift(1.2 * UP)
        self.play(Write(Np, run_time=0.5))
        text1 = Text("носитель полинома", font_size=25, color=BLACK)
        text1.shift(0.6 * UP)
        self.play(FadeIn(text1))
        self.wait()
        CoNp = Tex("$Co \ N_p = Co\{$", "$(2, 6)$", ",", " $(4, 5)$", ",", " $(6, 4)$", ",", " $(0, 10)$", ",",
                   " $(1, 9)$", ",", " $(8, 4)$", "$\}$", color=BLACK)
        self.play(Write(CoNp, run_time=0.5))
        self.wait()
        text2 = Text("многогранник Ньютона", font_size=25, color=BLACK)
        text2.shift(0.6 * DOWN)
        self.play(FadeIn(text2))
        self.wait()
        self.play(FadeOut(text1, run_time=0.2))
        self.play(FadeOut(CoNp, run_time=0.2))
        self.play(FadeOut(text2, run_time=0.2))
        self.wait()
        self.play(Np.animate.shift(UP))
        self.play(Np.animate.scale(0.75))
        self.play(Np.animate.to_edge(RIGHT), equation.animate.to_edge(RIGHT))
        self.wait()

        plane = NumberPlane(x_length=5, y_length=5, background_line_style={"stroke_color": BLACK},
                            axis_config={'color': 'BLACK', 'include_numbers': True}, x_range=[0, 11], y_range=[0, 11])
        x = plane.get_x_axis()
        x.numbers.set_color(BLACK)
        y = plane.get_y_axis()
        y.numbers.set_color(BLACK)
        y.numbers.edge = LEFT
        # plane.to_edge(DOWN)
        plane.to_edge(LEFT)
        # plane.shift(2 * RIGHT)
        y_label = plane.get_y_axis_label(Text("k2", font_size=14), edge=LEFT, direction=LEFT).set_color(BLACK)
        x_label = plane.get_x_axis_label(Text("k1", font_size=14)).set_color(BLACK)
        y_label.shift(2.5 * UP)
        grid_labels = VGroup(x_label, y_label)
        self.play(Create(plane))
        self.add(grid_labels)
        self.wait()

        def draw_point(coord):
            return plane.plot_line_graph(
                x_values=[coord[0]],
                y_values=[coord[1]],
                line_color=BLACK,
                vertex_dot_style=dict(stroke_width=2, fill_color=BLACK)
            )

        Np_coords = Np[1::2]
        for i in range(len(points)):
            self.play(FadeToColor(Np_coords[i], color=RED, run_time=0.2))
            self.play(Write(draw_point(points[i]), run_time=0.2))
            self.play(FadeToColor(Np_coords[i], color=BLACK, run_time=0.2))
            self.wait()
        self.play(FadeOut(Np, run_time=0.2))
        self.play(Write(plane.plot_line_graph(x_values=[0, 2, 4, 6, 8, 0],
                                              y_values=[10, 6, 5, 4, 4, 10],
                                              line_color=BLACK,
                                              add_vertex_dots=False
                                              )))
        vertices_coords = [
            [0, 10],
            [2, 6],
            [4, 5],
            [6, 4],
            [8, 4]
        ]
        vertices = [plane.coords_to_point(x, y) for x, y in vertices_coords]
        # print(vertices)
        # Создаем объект полигона
        polygon = Polygon(*vertices, fill_color=GRAY, fill_opacity=0.4)
        polygon.set_stroke(color=GRAY, width=0.01, opacity=1)
        self.play(Create(polygon))
        # plane.shift(UP)
        self.wait()
        vertices_coords = [
            [0, 10],
            [2, 6],
            [6, 4],
            [8, 4]
        ]
        for i in vertices_coords:
            self.play(FadeToColor(draw_point(i), color=BLUE, run_time=0.1))
        self.wait()
        for i in vertices_coords:
            self.play(FadeToColor(draw_point(i), color=BLACK, run_time=0.1))
        self.wait()
        self.play(Write(plane.plot_line_graph(x_values=[0, 2, 4, 6, 8, 0],
                                              y_values=[10, 6, 5, 4, 4, 10],
                                              line_color=BLUE,
                                              add_vertex_dots=False
                                              )))
        self.wait()
        self.play(Write(plane.plot_line_graph(x_values=[0, 2, 4, 6, 8, 0],
                                              y_values=[10, 6, 5, 4, 4, 10],
                                              line_color=BLACK,
                                              add_vertex_dots=False
                                              )))
        self.wait()
        self.play(FadeToColor(polygon, color=BLACK))
        self.wait()
        self.play(FadeToColor(polygon, color=GRAY))
        # text = Text(r"Привет, мир!", color=BLACK).scale(1.5)
        # self.play(Write(text))
        # self.wait()
        # ТЕОРЕМА И ЛЕММА ОТДЕЛЬНО
        obj = ["media/images/o1.jpg", "media/images/o2.jpg", "media/images/o3.jpg", "media/images/o4.jpg",
               "media/images/th1.jpg", "media/images/lemm1.jpg", "media/images/lemm2.jpg"]
        for i in range(len(obj)):
            o = ImageMobject(obj[i])
            o.scale(0.8)
            o.to_edge(RIGHT)
            self.play(FadeIn(o))
            self.wait()
            self.play(FadeOut(o))
        '''
        text = Text("выпуклая оболочка - многогранник Ньютона", font_size=30, color=BLACK)
        text.shift(3.25*DOWN)
        self.wait()
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
        ###!!!
        text = Text("(0, 0) - локальный минимум?", font_size=30, color=BLACK)
        text.shift(3.25*DOWN)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.play(FadeToColor(draw_point((0, 0)), color=BLUE, run_time=1))
        text = Text("какие мономы находятся в юго-западной части?", font_size=30, color=BLACK)
        text.shift(3.25*DOWN)
        self.play(FadeIn(text))
        '''

        points2 = [
            [0, 10],
            [2, 6],
            [6, 4],
            [8, 4]
        ]
        N = plane.coords_to_point(0, 0)
        k = 0
        n = 0
        # graph_text = Tex("грани юго-азапдной части:", "размерности 0:", "(0, 10)")
        for i in points2:
            PC = plane.coords_to_point(i[0], i[1])
            rectangle = Rectangle(width=abs(PC[0] - N[0]), height=abs(PC[1] - N[1]), fill_color=RED, fill_opacity=0.7)
            rectangle.set_stroke(color=RED, width=1, opacity=1)
            rectangle.next_to(plane.coords_to_point(0, 0), RIGHT + UP, buff=0)
            self.play(Create(rectangle))
            # self.play(FadeToColor(monoms[k], color=RED_C, run_time=0.2))
            self.wait()
            # self.play(FadeToColor(monoms[k], color=BLACK, run_time=0.2))
            self.wait(2)
            flag = False
            for j in points2:
                if i != j:
                    if j[0] <= i[0] and j[1] <= i[1]:
                        flag = True
                        self.play(FadeToColor(draw_point(i), color=RED_C, run_time=0.2))
                        # self.play(FadeToColor(monoms_func[k], color=RED_C, run_time=0.2))
                        break
            if not (flag):
                # self.play(FadeToColor(monoms_func[k], color=GREEN, run_time=0.2))
                # text = Tex(f"({i[0]},{i[1]})", color=BLACK)
                # text.shift(5*RIGHT+n*DOWN+2*UP)
                # self.play(Write(text, run_time=0.2))
                self.play(FadeToColor(draw_point(i), color=GREEN, run_time=0.2))
                n += 1
            self.play(FadeOut(rectangle))
            k += 1
        text = [Text("грани юго-западной части:", font_size=22, color=BLACK), Text("- размерности 0:", font_size=22, color=BLACK),
                Text("\t{(0, 10), (2, 6), (6, 4)}", font_size=22, color=BLACK), Text("- размерности 1:", font_size=22, color=BLACK),
                Text("\t{[(0, 10),(2, 6)], [(2, 6), (6, 4)]}", font_size=22, color=BLACK)]
        self.play(Write(plane.plot_line_graph(x_values=[0, 2, 4, 6],
                                              y_values=[10, 6, 5, 4],
                                              line_color=GREEN,
                                              add_vertex_dots=False,
                                              stroke_width=4
                                              )))
        for i in range(len(text)):
            text[i].shift((2-0.4*i) * UP + 4 * RIGHT)
            self.play(FadeIn(text[i]))
            self.wait(2)
        self.wait()
        text1 = Text("главные квазиоднородные формы:", font_size=22, color=BLACK)
        main_quasi = Tex("${x^2}{y^6}$, ", "${x^6}{y^4}$, ", "$y^{10}$, ", "$y^{10}+{x^2}{y^6}$", color=BLACK)
        text1.shift(0.4*DOWN+4*RIGHT)
        self.play(FadeIn(text1))
        self.wait()
        main_quasi.scale(0.6)
        main_quasi.shift(0.8*DOWN+4*RIGHT)

        self.play(Write(main_quasi))
        text2 = Text("неотрицательны и невырождены\nв слабом смысле", font_size=22, color=BLACK)
        text2.shift(1.3*DOWN+4*RIGHT)
        self.play(FadeIn(text2))
        text3 = Tex("${x^2}{y^6} - 2{x^4}{y^5} + {x^6}{y^4} = {x^2}{y^2}(y-{x^2})^2$",color=BLACK)
        text3.scale(0.6)
        text3.shift(1.85*DOWN+4*RIGHT)
        text4 = Text("неотрицательна, но вырожденная,\nтак как при x = 1, y = 1 дает 0.", font_size=22, color=BLACK)
        text4.shift(2.35*DOWN+4*RIGHT)
        self.play(Write(text3))
        self.wait()
        self.play(FadeIn(text4))
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()
        text = Text("Разложим p на сумму главных (1,2)-квазиоднородных форм:", font_size=30, color=BLACK)
        text.to_edge(UP)
        self.play(FadeIn(text))
        self.wait()
        obj = [p, f1, f11, f2, f3, f4, l3.to_edge(LEFT)]
        for i in range(len(obj)):
            obj[i].shift((2.5-i)*UP)
            self.play(Write(obj[i]))
        text5 = Text("не локальный минимум", font_size=30, color=BLACK)
        text5.scale(0.7)
        text5.shift(3.5*DOWN)
        text5.to_edge(RIGHT)
        self.play(FadeIn(text5))
        self.wait(5)
