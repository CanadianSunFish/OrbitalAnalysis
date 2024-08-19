from astropy import units

import pyvista as pv
from pyvista import examples

m = units.m
km = units.km

g = units.g
kg = units.kg

s = units.s
day = units.day
bar = units.bar
mb = units.mb
N = units.newton
rad = units.rad
deg = units.deg
AU = units.AU

sun = {

    'equ_r'             : 6.957e8 * m

}

mercury = {

    'naif_id'           : 199,
    'g'                 : 3.701 * m / s**2,
    'mu'                : 2.2031868e13 * km**3 / s**2,
    'equ_r'             : 2440530 * m,
    'mass'              : 3.302e23 * kg,
    'atmo'              : 5e-15 * bar,
    'escape_v'          : 4435 * m/s,
    'rot'               : 1.24001e-6 * rad / s,
    'sol_day'           : 175.9421 * day,
    'sidereal_period'   : 87.969257 * day

}

venus = {

    'naif_id'           : 299,
    'g'                 : 8.870 * m / s**2,
    'mu'                : 3.248592e14 * km**3 / s**2,
    'equ_r'             : 6051893 * m,
    'mass'              : 48.685e23 * kg,
    'atmo'              : 90 * bar,
    'aphelion'          : 0.728213 * AU,
    'perihelion'        : 0.718440 * AU,
    'semi'              : 0.723332 * AU,
    'ecc'               : 0.006772, 
    'inclination'       : 3.86 * deg,
    'escape_v'          : 10361 * m/s,
    'synodic_period'    : 583.92 * day, 
    'sidereal_rate'     : 2.9924e-7 * rad / s,
    'sidereal_period'   : 243.0226 * day,

}

earth = {

    'naif_id'           : 399,
    'equ_g'             : 9.7803267715 * m / s**2,
    'polar_g'           : 9.8321863685 * m / s**2,
    'mu'                : 3.986004418e14 * m**3 / s**2,
    'equ_r'             : 6378000 * m,
    'polar_r'           : 6356000 * m,
    'mean_r'            : (6356000 + 6378000) / 2 * m,
    'mass'              : 5.97219e24 * kg,
    'atmo'              : 1.0 * bar,
    'aphelion'          : 152097597 * km ,
    'perihelion'        : 147098450 * km,
    'semi'              : 149598023 * km,
    'ecc'               : 0.0167086, 
    'inclination'       : 7.25 * deg,
    'escape_v'          : 11186 * m/s,
    'rot'               : 7.292115e-5 * rad / s,
    'sol_day'           : 86400.00 * s,
    'daily_motion'      : 0.01720279 * rad / day,
    'sidereal'          : 365.25636 * day

}

moon = {

    'naif_id'           : 301,
    'g'                 : 1.625 * m / s**2,
    'equ_r'             : 1738000 * m,
    'mass'              : 7.348e22 * kg,
    'atmo'              : 3e-15 * bar,
    'rot'               : 2.6617e-6 * rad / s,
    'sol_day'           : 29.5306 * day,
    'sidereal'          : 27.321582 * day

}

mars = {

    'naif_id'           : 499,
    'g'                 : 3.73 * m / s**2,
    'equ_r'             : 3396200.0 * m,
    'polar_r'           : 3376200.0 * m,
    'mean_r'            : ((3396200.0 + 3376200.0) / 2.0) * m,
    'mass'              : 0.64169e14 * kg,
    'atmo'              : 0.00636 * bar,

}

jupiter = {

    'naif_id'           : 599,
    'equ_r'             : 71492000.0 * m,
    'polar_r'           : 66854000.0 * m,
    'mean_r'            : ((71492000.0 + 66854000.0) / 2) * m,
    'mass'              : 1898.13e24 * kg,
    'g'                 : 25.92 * m / s**2          

}

_args = {
            'ax_size': (1, 2),
            'ax_figs': ['velocity', 'position'],
            'background': 'black',
            'fig_size': (24, 15),
            'legend': True,
            'multi_array': False,
            'show': True,
            'show_planets': False,
            'title': 'Space',
            'xlabel': ['Time', 'Time'],
            'ylabel': ['Velocity', 'Position'],
            'launch': None,
            'target': None,
            'target_str': 'Set Target Str'
        }


naif_id_dict = {
        199: 'MERCURY',
        299: 'VENUS',
        399: 'EARTH',
        301: 'MOON',
        499: 'MARS',
        599: 'JUPITER',
        699: 'SATURN',
        799: 'URANUS',
        899: 'NEPTUNE',
        999: 'PLUTO',
}


planet_order_dict = {
    1: 199,
    2: 299,
    3: 399,
    4: 301,
    5: 499,
    6: 599,
    7: 699,
    8: 799,
    9: 899,
    10: 999
}



def columns():
    return ['EC', 'QR', 'IN', 'OM', 'W', 'TP', 'N', 'MA', 'TA', 'A', 'AD', 'PR'] 





# print(examples.planets.__dir__())

# plotter = pv.Plotter(window_size=[2100,1400])
# plotter.set_background('black')
# inner = 60268.0 + 7000.0
# outer = 60268.0 + 80000.0
# saturn_rings = examples.planets.load_saturn_rings(inner=inner, outer=outer, c_res=50)
# saturn_rings_texture = examples.planets.download_saturn_rings(texture=True)
# saturn = examples.planets.load_saturn(radius=60268.0)
# saturn_texture = examples.planets.download_saturn_surface(texture=True)
# plotter.add_mesh(saturn_rings, texture=saturn_rings_texture)
# plotter.add_mesh(saturn, texture=saturn_texture)
# plotter.show()


color_map = {
    'earth': 'blue',
    'mars': 'red',
    'venus': 'gray',
    'mercury': 'green',
    'jupiter': 'brown',
    'neptune': 'darkblue'
}


jpl_api = ['VECTOR', 'ELEMENTS']


rplanet = 6371000
mplanet = 5.972e24
G = 6.6742e-11