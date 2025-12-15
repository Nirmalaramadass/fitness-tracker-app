import os
import sys
import random

# Ensure project root is on path so we can import existing modules
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    import ml_model
except Exception:
    ml_model = None

try:
    import diet_recommendation
except Exception:
    diet_recommendation = None


class DataProvider:
    """Adapter that exposes simple data methods used by the UI.

    It will reuse functions from existing project modules if available,
    otherwise it falls back to simulated data for testing on desktop/emulator.
    """

    def __init__(self):
        self._step_base = 1000

    def get_current_steps(self):
        # Prefer an ml_model-provided realtime reader if available
        try:
            if ml_model and hasattr(ml_model, 'get_current_steps'):
                return int(ml_model.get_current_steps())
        except Exception:
            pass
        # fallback: simulated incremental steps
        self._step_base += random.randint(0, 20)
        return self._step_base

    def get_current_calories(self):
        try:
            if ml_model and hasattr(ml_model, 'get_current_calories'):
                return float(ml_model.get_current_calories())
        except Exception:
            pass
        # fallback: simple proportional calories
        return round(self._step_base * 0.04, 1)

    def get_day_series(self, days=7):
        # Try to reuse historical methods, else simulate day-wise totals
        try:
            if diet_recommendation and hasattr(diet_recommendation, 'get_history'):
                return diet_recommendation.get_history(days)
        except Exception:
            pass
        # simulated last `days` values
        base = max(1000, self._step_base - 2000)
        return [base + random.randint(-500, 2500) for _ in range(days)]
