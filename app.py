import app
import math
from app_components import clear_background
from events.input import Buttons, BUTTON_TYPES


class CatApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.happy_timer = 0

    def update(self, delta):
        self.happy_timer = max(0, self.happy_timer - 1)
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()
        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.button_states.clear()
            self.happy_timer += 20

    def draw(self, ctx):
        clear_background(ctx)
        # whiskies
        for i in [-1, 1]:
            ctx.rgb(1, 1, 1).begin_path()
            ctx.move_to(i * 40, 50)
            ctx.line_to(i * 100, 70)
            ctx.stroke()
            ctx.rgb(1, 1, 1).begin_path()
            ctx.move_to(i * 40, 30)
            ctx.line_to(i * 100, 10)
            ctx.stroke()
            ctx.rgb(1, 1, 1).begin_path()
            ctx.move_to(i * 45, 40)
            ctx.line_to(i * 110, 40)
            ctx.stroke()
            # eyesies
            if self.happy_timer != 0:
                ctx.rgb(.75,.75,.75).begin_path()
                old = ctx.line_width
                ctx.line_width = 6
                ctx.move_to(i * 70, -15).line_to(i * 30, -30).stroke()
                ctx.line_width = old
            else:
                ctx.rgb(1,1,1).arc(i * 40, -30, 20, 0, 2 * math.pi, True).fill()
            #ctx.rgb(.5,.5,.5).arc(i * 30, -50, 5, 0, 2 * math.pi, True).fill()
            #arc_start = 0 if i == -1 else 0.5 * math.pi
            #arc_end =  0.5 * math.pi if i == -1 else math.pi
            #ctx.rgb(1, 1, 1).arc(i * 20, 0, 20, arc_start, arc_end, True).stroke()
        # noseies
        #ctx.rgb(1, 1, 1).begin_path()
        #ctx.move_to(0, 50).line_to(10, 30).line_to(-10, 30).close_path()
        #ctx.fill()
        ctx.rgb(1,1,1).begin_path()
        ctx.line_width = 6
        sf = 1 + (.5 * (min(1, (self.happy_timer / 10) * 2)))
        ctx.move_to(-20 * sf, 30).line_to(-10 * sf, 50).line_to(0, 30).line_to(10 * sf, 50).line_to(20 * sf, 30).stroke()

__app_export__ = CatApp
