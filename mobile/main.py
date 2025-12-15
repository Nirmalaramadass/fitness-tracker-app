import os
import sys
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.utils import platform

from kivymd.app import MDApp

# add project root so existing modules can be imported by data_provider
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from mobile.data_provider import DataProvider

try:
    from kivy_garden.graph import MeshLinePlot
except Exception:
    MeshLinePlot = None


class MainScreen(object):
    pass


class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        kv_path = os.path.join(os.path.dirname(__file__), 'main.kv')
        self.root = Builder.load_file(kv_path)
        self.data = DataProvider()
        return self.root

    def on_start(self):
        self.plot = None
        if MeshLinePlot and self.root.ids.get('graph'):
            self.plot = MeshLinePlot(color=[0.2, 0.6, 1, 1])
            self.root.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self._tick, 1.0)

    def _tick(self, dt):
        steps = self.data.get_current_steps()
        calories = self.data.get_current_calories()
        if self.root.ids.get('steps_label'):
            self.root.ids.steps_label.text = str(steps)
        if self.root.ids.get('calories_label'):
            self.root.ids.calories_label.text = str(calories)
        # update graph
        if self.plot and self.root.ids.get('graph'):
            g = self.root.ids.graph
            pts = list(self.plot.points) if hasattr(self.plot, 'points') and self.plot.points else []
            # append new reading, keep max 30
            pts.append((len(pts), steps))
            if len(pts) > 30:
                pts = [(i, v) for i, v in enumerate(pts[-30:])]
                pts = [(i, v[1]) for i, v in enumerate(pts)]
            # normalize points to graph coordinates
            try:
                self.plot.points = pts
                g.xmax = max(30, len(pts))
                g.ymax = max(g.ymax, max([p[1] for p in pts]) * 1.2)
            except Exception:
                pass


if __name__ == '__main__':
    FitnessApp().run()
