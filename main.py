from manim import *
import numpy as np

class FirstScene(Scene):
    def construct(self):

        # we were taught the following basic electrical quantities:
        vir_text = MathTex(r"V = IR", font_size = 40).move_to([-1, 0, 0])
        pvi_text = MathTex(r"P = VI", font_size = 40, substrings_to_isolate="P").move_to([1, 0, 0])

        self.play(Create(vir_text), run_time=0.8)
        self.wait(0.5)
        self.play(Create(pvi_text), run_time=0.8)

        self.wait(1)
        rvi_tex = MathTex(r"R = \frac{V}{I}", substrings_to_isolate="R", font_size=40).move_to([-1, 0, 0])
        self.play( Transform( vir_text, rvi_tex), run_time=0.8)

        # these quentities here are scalar and are used in basic dc analysis
        self.wait(3)
        dc_text = Text("DC", font_size=40, color=MAROON_A).move_to([-3, 1, 0])
        self.play(Create(dc_text), run_time=0.3)

        self.wait(1.5)
        dc_group = VGroup(*[dc_text, vir_text, pvi_text])
        self.play(dc_group.animate(run_time=0.8).shift(DOWN * 2), run_time=0.8)

                 
        # however, these are a simpler representation of how ac circuits are analyzed using the complex plane
        self.wait(0.4)
        ac_text = Text("AC", font_size=40, color=MAROON_B).move_to([-3, 2.5, 0])
        self.play(Create(ac_text), run_time=0.3)

        self.wait(2)
        # the impedance
        impedance_formula = MathTex(r"Z = R + jX", substrings_to_isolate=["Z", "R", "jX"], font_size=40).move_to([-1.5, 1.5, 0])
        self.play(Create(impedance_formula), run_time=0.5)
        # Z...
        z_pos = impedance_formula.get_part_by_tex("Z").copy().get_center()
        imp_text_pos = (impedance_formula.get_part_by_tex("Z")
            .copy()
            .shift(DOWN)
            .get_center())
        arrow_to_impedance = Arrow(start=z_pos, end=imp_text_pos, color=GOLD) 
        impedance_text = (
            Text("Impedance", font_size=30, color=GREEN_A) 
            .move_to(imp_text_pos)
        )
        self.play(Create(arrow_to_impedance))
        self.play(Create(impedance_text))

        # the apparent power
        self.wait(0.5)
        app_pow_formula = MathTex(r"S = P + jQ", substrings_to_isolate=["S", "P", "jQ"], font_size=40).move_to([1.5, 1.5, 0])
        self.play(Create(app_pow_formula), run_time=0.5)
        # S...
        s_pos = app_pow_formula.get_part_by_tex("S").copy().get_center()
        app_pow_text_pos = (app_pow_formula.get_part_by_tex("S")
            .copy()
            .shift(DOWN)
            .get_center())
        arrow_to_app_pow = Arrow(start=s_pos, end=app_pow_text_pos, color=GOLD) 
        app_pow_text = (
            Text("Apparent\nPower", font_size=30, color=GREEN_A) 
            .move_to(app_pow_text_pos)
            .shift(DOWN * 0.1) # needed the shift, as the next line took up space
        )
        self.play(Create(arrow_to_app_pow))
        self.play(Create(app_pow_text))


        # now notice how the R resistance is a component of the impedance Z, 
        self.wait(2)
        vir_highlight_r= MathTex(r"R = \frac{V}{I}", substrings_to_isolate="R", font_size=40).move_to(vir_text.get_center())
        vir_highlight_r.set_color_by_tex('R', BLUE)
        self.play(Transform(vir_text, vir_highlight_r), run_time=0.5)
        self.wait(0.2)
        impedance_r_highlight = impedance_formula.copy()
        impedance_r_highlight.set_color_by_tex('R', BLUE)
        self.play(Transform(impedance_formula, impedance_r_highlight), run_time=0.5)
         
        # and the P power is a component of the apparent Power S
        self.wait(2.0)
        pvi_p_highlighted = MathTex(r"P = VI", substrings_to_isolate="P", font_size=40).move_to(pvi_text.get_center())
        pvi_p_highlighted.set_color_by_tex('P', RED)
        self.wait(1.0)
        self.play(Transform(pvi_text, pvi_p_highlighted), run_time=0.5)
        app_pow_formula_p_highlighted = app_pow_formula.copy()
        app_pow_formula_p_highlighted.set_color_by_tex('P', RED)
        self.play(Transform(app_pow_formula, app_pow_formula_p_highlighted), run_time=0.5)

        # Because in DC, these two imaginary values are not used.
        self.wait(1.5)
        circle1 = Circle(radius=0.4).move_to(impedance_r_highlight.get_part_by_tex("jX").get_center())
        circle2 = Circle(radius=0.4).move_to(app_pow_formula.get_part_by_tex("jQ").get_center())
        self.play(Create(circle1))
        self.play(Create(circle2))

        self.wait(1)

        self.play(FadeOut(dc_group), run_time=0.5)
        self.play(FadeOut(VGroup(*[circle1, circle2, arrow_to_app_pow, arrow_to_impedance])), run_time=0.5)
        run_time = 0.5
        scale = 2
        app_pow_text_no_nline = (
            Text("Apparent Power", font_size=30, color=GREEN_A) 
            .move_to(app_pow_text_pos)
            .shift([-3, -1.2, 0]) # needed the shift, as the next line took up space
        )
        self.play(
            impedance_formula.animate(run_time=run_time).shift(DOWN * 1).scale(scale),
            impedance_text.animate(run_time=run_time).shift([-0.5, 0.8, 0]),
            app_pow_formula.animate(run_time=run_time).shift([-3, -3, 0]).scale(scale),
            app_pow_text.animate(run_time=run_time).shift([-2, -1, 0]),
            Transform(app_pow_text, app_pow_text_no_nline,  run_time=run_time)
        )
        impedance_formula_x = impedance_formula.get_center()[0]
         
        # But in AC, we need these

        # The Reactance...
        jx_part = impedance_formula.get_part_by_tex("jX")
        jx_start_arrow = jx_part.copy().shift(RIGHT * 0.4).get_center()
        reactance_text_pos = jx_part.copy().shift(RIGHT * 2).get_center()
        reactance_text = Text("Reactance", font_size=30).move_to(reactance_text_pos).shift(RIGHT)
        arrow_to_reactance = Arrow(start=jx_start_arrow, end=reactance_text_pos, color=GOLD)
        self.play(Create(arrow_to_reactance), run_time=0.5)
        self.play(Create(reactance_text), run_time=1)


        # and reactive power...
        jx_part = app_pow_formula.get_part_by_tex("jQ")
        jx_start_arrow = jx_part.copy().shift(RIGHT * 0.4).get_center()
        react_pow_text_pos = jx_part.copy().shift(RIGHT * 2).get_center()
        react_pow_text = Text("Reactive\nPower", font_size=30).move_to(react_pow_text_pos).shift([1, -0.25, 0])
        arrow_to_react_pow = Arrow(start=jx_start_arrow, end=react_pow_text_pos, color=GOLD)
        self.play(Create(arrow_to_react_pow), run_time=0.5)
        self.play(Create(react_pow_text), run_time=1)

        
class SecondScene(Scene):
    def construct(self):
        ac_title = Text("AC", color=MAROON_B, font_size=40).move_to([-3, 2.5, 0])
        self.add(ac_title)
        self.wait(2)
        # now to see why this is the case, lets first look at reactance
        # reactance can either be capacitance due to a capacitative load
        # or inductance due to an inductive load
        # in ac, capacitative loads smoothens the change in voltage,
        # delaying the peak amplitude of the voltage
        # this can be described as the current leading the voltage

def main():
    print("Hello from write-up!")


if __name__ == "__main__":
    main()
