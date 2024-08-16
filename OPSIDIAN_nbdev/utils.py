# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_utils.ipynb.

# %% auto 0
__all__ = ['gradient_to_spline_angle']

# %% ../nbs/02_utils.ipynb 3
import math
def gradient_to_spline_angle(m:float # Gradient of the spline in the x-z plane.
                             )->float: # Angle of the spline starting from the north direction going anti-clockwise.
    "Function to convert the gradient of the spline in the x-z plane to the angle of the spline starting from the north direction going anti-clockwise."
    if m == float('inf'):
        angle = 0
    elif m <= 0:
        angle = math.pi / 2 - math.atan(-m)
    else:
        angle = math.atan(m) + math.pi / 2
    return angle
