import datetime
import numpy as np
import spiceypy as spice

today = datetime.datetime.today()

start = today.strftime("%Y-%m-%dT00:00:00")
end = datetime.date(2025, 1, 1).strftime("%Y-%m-%dT00:00:00")

# Loading the leap second kernel
LSK = "src/utils/kernels/lsk/naif0012.tls"
spice.furnsh(LSK)

# Working around J2000 ephemeris time
ephemeris_start = spice.utc2et(start)
ephemeris_end = spice.utc2et(end)

eph = np.arange(ephemeris_start, ephemeris_end, 10000)

# Loading spice kernel
FILENAME = "src/utils/kernels/spk/de432s.bsp"
spice.furnsh(FILENAME)

# TODO determine if the units are kilometers
mars = spice.spkezr("MARS BARYCENTER", ephemeris_start, "ECLIPJ2000", "NONE", "SUN")[0][
    :3
]
mercury = spice.spkezr(
    "MERCURY BARYCENTER", ephemeris_start, "ECLIPJ2000", "NONE", "SUN"
)[0][:3]
venus = spice.spkezr("VENUS BARYCENTER", ephemeris_start, "ECLIPJ2000", "NONE", "SUN")[
    0
][:3]
earth = spice.spkezr("EARTH", ephemeris_start, "ECLIPJ2000", "NONE", "SUN")[0][:3]
jupiter = (
    0.5
    * spice.spkezr("JUPITER BARYCENTER", ephemeris_start, "ECLIPJ2000", "NONE", "SUN")[
        0
    ][:3]
)

from plotting_utils import *

plot = Plotter(
    [mars, mercury, venus, earth, jupiter],
    args={"multi_array": True},
    labels=("mars", "mercury", "venus", "earth", "jupiter"),
)

plot.solar_system()


class Spice:

    def __init__(self, kernel, lsk, bodies, t0, tf):
        spice.furnsh(kernel)
        spice.furnsh(lsk)

        self.bodies = bodies

        eph0 = spice.utc2et(t0)
        ephf = spice.utc2et(tf)

        eph_array = np.arange(eph0, ephf, 1000)

        self.eph = eph_array

    def get_planetary_data(self):

        for body in self.bodies:
            data = spice.spkezr()

        return
