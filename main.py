from manim import *

class CreateCircle(Scene):
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
        # the impedance
        ac_text = Text("AC", font_size=40, color=MAROON_B).move_to([-3, 2.5, 0])
        self.play(Create(ac_text), run_time=0.3)

        self.wait(2)
        impedance_text = MathTex(r"Z = R + jX", substrings_to_isolate=["R", "jX"], font_size=40).move_to([1.5, 1.5, 0])
        self.play(Create(impedance_text), run_time=0.5)

        # the apparent power
        self.wait(0.5)
        app_pow_text = MathTex(r"S = P + jQ", substrings_to_isolate=["P", "jQ"], font_size=40).move_to([-1.5, 1.5, 0])
        self.play(Create(app_pow_text), run_time=0.5)


        # now notice how the P power is a component of the apparent Power S
        self.wait(2.0)
        pvi_p_highlighted = MathTex(r"P = VI", substrings_to_isolate="P", font_size=40).move_to(pvi_text.get_center())
        pvi_p_highlighted.set_color_by_tex('P', RED)
        self.wait(1.0)
        self.play(Transform(pvi_text, pvi_p_highlighted), run_time=0.5)
        app_pow_text_p_highlighted = app_pow_text.copy()
        app_pow_text_p_highlighted.set_color_by_tex('P', RED)
        self.play(Transform(app_pow_text, app_pow_text_p_highlighted), run_time=0.5)

        # and the R resistance is a component of impedance Z, 
        self.wait(2)
        impedance_r_highlight = impedance_text.copy()
        impedance_r_highlight.set_color_by_tex('R', BLUE)
        self.play(Transform(impedance_text, impedance_r_highlight), run_time=0.5)
        self.wait(0.2)
        vir_highlight_r= MathTex(r"R = \frac{V}{I}", substrings_to_isolate="R", font_size=40).move_to(vir_text.get_center())
        vir_highlight_r.set_color_by_tex('R', BLUE)
        self.play(Transform(vir_text, vir_highlight_r), run_time=0.5)

        # Because in DC, these two imaginary values are not used.
        self.wait(1.5)
        circle1 = Circle(radius=0.4).move_to(impedance_r_highlight.get_part_by_tex("jX").get_center())
        circle2 = Circle(radius=0.4).move_to(app_pow_text.get_part_by_tex("jQ").get_center())
        self.play(Create(circle1))
        self.play(Create(circle2))

        # But in AC, we need them, the reactive power, and the reactance...
        

         
        # now how does the complex plane help in representing these?
        # first of... it is important to understand how complex numbers allow the representation of both magnitude and angle in one equation... aka vectors
        # the imaginary number j implies a 90-degree rotation... signifying the y axis  
        # this allows us to model sinusoidal waves easier
        # where the magnitude of the vector is the amplitude
        # and the angle formed is the phase shift
        # since we use phases instead of angles
        # this is termed as a phasor, phase and vector
        #
        # now see the significance of using complex numbers?
        # complex numbers allow us to use basic complex algebra in performing arithmetic on waveforms
        # sinosoidal waves are difficult to work with using only trigonometric identities
        # And this allows the reactance and reactive power to be represented as variables X and Q
        # ILLUSTRATE:
        #
        # first lets start with reactance...
        # well... it can either be capacitance or inductance
        # capacitance causes the current to lead the voltage
        # this means that the current reaches its peak before the voltage does...
        # while inductance causes the current to lag the voltage
        # meaning its current reaches its peak after the voltage's...
        # ILLUSTRATE: show clearly and slow stop speaking for now...
        #
        # 
        #
        # because of reactance you know have a phaseshift between the current and the voltage
        # what this means though, is that the power cannot be calculated by simple means of VI anymore
        # 
        #
        # Here we see the impedance 
        # 
        # Now what is this reactance?
        # 
        # 
        # then introduce phasors
        # 
        # then introduce impedance
        # how it relates to current lag voltage
        # how it relates to power

        # In electronics, we initially were taught of voltage and resistance as simple scalar quantities
        # however, they are simpler representations of what they could be represented in the complex plain
        # Where there is the real axis and the imaginary axis
        # 
        # resistance is actually the real component of a what we call impedance
        # And the imaginary component being the reactance.
        # Reactance is not imaginary by itself — it’s a real quantity.
        # We place it on the imaginary axis simply to represent that it creates a phase shift between voltage and current.
        # ILLUSTRATE
        # 
        # using the complex plane, we can compute for the total impedance with the pythagorean theorem, and use the resistance and reactance
        # ILLUSTRATE
        # 
        # here the phase shift is zero when there is no reactance, and non-zero otherwise
        # ILLUSTRATE
        # 
        # This same phase shift is the phase-shift between the current and the voltage
        # ILLUSTRATE
        #
        # therefore, the reactance causes the phase-shift between the current and the voltage
        # causing the the current to either lag the voltage or lead it.
        # ILLUSTRATE
        #
        # the current leads the voltage if its peak comes first before the voltage
        # or the phase angle between the two are greater than zero
        # ILLUSTRATE
        #
        # and the current lags the voltage otherwise
        # ILLUSTRATE
        # 
        # now what is the significance of reactance
        # In the real world, there cannot be wires with zero impedance... note that I now use the term impedance instead of resistance
        # for instance, say you have a dc circuit with some resistor
        # ideally, your total impedance is equal to the total resistance
        # however, you lengthen that wire, and there will be a natural reactance, thereby increasing the impedance
        # now there are types of reactance, capacitance and inductance...

def main():
    print("Hello from write-up!")


if __name__ == "__main__":
    main()
