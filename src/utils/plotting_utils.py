import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt

from pprint import pprint
from typing import Optional
from pyvista import examples

from src.satellite import launch_pos as lp
from src.satellite import sat_orbit as sat
from src.utils import data
from src.utils import states


def get_planet_texture(planet):
    planet = planet.lower()
    if planet == "sun":
        sun = examples.planets.load_sun(radius=data.sun["equ_r"].value)
        sun_texture = examples.planets.download_sun_surface(texture=True)
        return sun, sun_texture
    if planet == "mercury":
        mercury = examples.planets.load_mercury(radius=data.mercury["equ_r"].value)
        mercury_texture = examples.planets.download_mercury_surface(texture=True)
        return mercury, mercury_texture
    if planet == "venus":
        venus = examples.planets.load_venus(radius=data.venus["equ_r"].value)
        venus_texture = examples.planets.download_venus_surface(texture=True)
        return venus, venus_texture
    if planet == "earth":
        earth = examples.planets.load_earth(radius=data.earth["equ_r"].value)
        earth_texture = examples.load_globe_texture()
        return earth, earth_texture
    if planet == "mars":
        mars = examples.planets.load_mars(radius=data.mars["equ_r"].value)
        mars_texture = examples.planets.download_mars_surface(texture=True)
        return mars, mars_texture
    if planet == "jupiter":
        jupiter = examples.planets.load_jupiter(radius=data.jupiter["equ_r"].value / 10)
        jupiter_texture = examples.planets.download_jupiter_surface(texture=True)
        return jupiter, jupiter_texture
    if planet == "saturn":
        saturn = examples.planets.load_saturn(radius=data.saturn["equ_r".value])

    return


class Plotter:

    def __init__(
        self, data, args: Optional[dict] = None, labels: Optional[tuple] = None
    ):

        _args = {
            "ax_size": (1, 2),
            "ax_figs": ["velocity", "position"],
            "background": "black",
            "fig_size": (24, 15),
            "legend": True,
            "multi_array": False,
            "radius": None,
            "show": True,
            "show_planets": False,
            "title": "Space",
            "xlabel": ["Time", "Time"],
            "ylabel": ["Velocity", "Position"],
            "launch": None,
            "target": None,
            "target_str": "Set Target Str",
        }

        if args is not None:
            for key in args.keys():
                _args[key] = args[key]

        self.args = _args

        self.data = data

        if labels is not None:
            self.labels = labels

        if self.args["multi_array"]:
            assert len(self.data) == len(
                self.labels
            ), "must have the same number of labels as you have planets"

    def print__args(self):
        pprint(self.args)

    def solar_system(self):
        """Plots the position array passed with associated labels and
        appropriate colors.

        Args:
            pos_arrays: tuple or array
                        an array or tuple of arrays each containing all information
                        needed to plot the orbit
            labels: tuple or array
                    list of labels that line up with each position array for
                    adding an accurate legend

        """
        plotter = pv.Plotter()

        if self.args["multi_array"] == True:

            for index, arr in enumerate(self.data):

                label = self.labels[index].lower()

                planet, texture = get_planet_texture(label)
                planet.translate(np.array(arr), inplace=True)

                plotter.add_mesh(planet, texture=texture, label=label.title())

        else:
            planet, texture = get_planet_texture(self.labels)
            planet.translate(np.array(self.data), inplace=True)
            plotter.add_mesh(planet, texture=texture, label=self.labels.title())

        sun = examples.planets.load_sun(radius=6963400)
        sun_texture = examples.planets.download_sun_surface(texture=True)
        plotter.add_mesh(sun, texture=sun_texture, label="Sun")

        plotter.camera_position = "iso"
        plotter.camera.zoom(0.8)

        plotter.set_background(self.args["background"])

        if self.args["legend"]:
            plotter.add_legend(
                bcolor=(0, 0, 0), border=False, size=[0.15, 0.15], face=None
            )

        if self.args["show"]:
            plotter.show()

    def satellite(self):
        plotter = pv.Plotter(window_size=[2100, 1400])
        plotter.set_background("black")
        Earth = examples.planets.load_earth(radius=6371000)
        earth_texture = examples.load_globe_texture()
        plotter.add_mesh(Earth, texture=earth_texture)

        orbit_points = np.column_stack(
            (self.data[0, :], self.data[1, :], self.data[2, :])
        )
        plotter.add_mesh(
            orbit_points,
            color="white",
            label="Orbit Trajectory",
            style="wireframe",
            point_size=1.5,
        )

        if self.args["launch"] is not None:
            launch_point = pv.PolyData(
                [self.args["launch"][0], self.args["launch"][1], self.args["launch"][2]]
            )
            plotter.add_mesh(
                launch_point,
                color="yellow",
                point_size=15,
                render_points_as_spheres=True,
                label="Launch",
            )

        if self.args["target"] is not None:
            target_point = pv.PolyData(
                [self.args["target"][0], self.args["target"][1], self.args["target"][2]]
            )
            plotter.add_mesh(
                target_point,
                color="#89CFF0",
                point_size=15,
                render_points_as_spheres=True,
                label=self.args["target_str"].title(),
            )

        if self.args["legend"]:
            plotter.add_legend(size=(0.15, 0.15), face=None, bcolor="black")

        _ = plotter.add_axes(
            color="white",
            line_width=3,
            cone_radius=0.2,
            shaft_length=0.7,
            tip_length=0.3,
            ambient=0.5,
            label_size=(0.4, 0.16),
        )
        if self.args["show"]:
            plotter.show()

    def states(self):

        plt.close()

        assert (self.args["ax_size"][0] * self.args["ax_size"][1]) == len(
            self.args["ax_figs"]
        )

        fig, ax = plt.subplots(
            self.args["ax_size"][0],
            self.args["ax_size"][1],
            figsize=self.args["fig_size"],
        )

        state_arr = states.get_states(self.data, self.args["ax_figs"])

        if np.ndim(ax) == 1:
            for row in range(len(ax)):
                ax[row].plot(range(len(state_arr[0])), state_arr[row])
                ax[row].set_xlabel(self.args["xlabel"][row])
                ax[row].set_ylabel(self.args["ylabel"][row])
        else:
            for row in range(len(ax)):
                for column in range(len(ax[0])):
                    ax[row][column].plot(
                        range(len(state_arr[row + column])), state_arr[row + column]
                    )
                    ax[row][column].set_xlabel()
                    ax[row][column].set_title(
                        self.args["ax_figs"][row + column].title()
                    )

        fig.suptitle(self.args["title"])

        plt.show()

    """
        v = np.sqrt(state[3,:]**2 + state[4,:]**2 + state[5,:]**2)
        r = np.sqrt(state[0,:]**2 + state[1,:]**2 + state[2,:]**2) - rplanet
        mass = state[6,:]
        t = np.linspace(0, period, 10000)

        index_a = np.argmax(r)
        index_p = np.argmin(r[1000:]) + 1000

        index_m = np.argmin(mass)
        print(min(mass))

        inclin = np.rad2deg(np.arctan2(state[2,:], np.sqrt(state[0,:]**2 + state[1,:]**2)))

        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(25, 14))
        fig.suptitle(f"Launch")
        ax0.plot(t, mass, label='Mass', c='red')
        ax0.set_title("Mass vs Time")
        ax0.set_xlabel("Time (s)")
        ax0.set_ylabel("Mass")
        ax0.annotate(f"Mass Min: {mass[index_m]:,.0f} kg", 
            xy=(t[index_m], mass[index_m]),
            xytext=(-120,0),
            textcoords='offset points', 
            arrowprops=dict(arrowstyle='->', 
                            connectionstyle='arc3,rad=0.3',     
                            color='black', 
                            linewidth=1.5)
                    )

        ax1.plot(t, r, label='Position', c='blue')
        ax1.set_title("Position vs Time")
        ax1.annotate(f"Apogee: {r[index_a]:,.0f} m", 
            xy=(t[index_a], r[index_a]),
            xytext=(-120,0),
            textcoords='offset points', 
            arrowprops=dict(arrowstyle='->', 
                            connectionstyle='arc3,rad=0.3',     
                            color='black', 
                            linewidth=1.5)
                    )
        ax1.annotate(f"Perigee: {r[index_p]:,.0f} m", 
            xy=(t[index_p], r[index_p]),
            xytext=(-125, -5),
            textcoords='offset points', 
            arrowprops=dict(arrowstyle='->', 
                            connectionstyle='arc3,rad=0.3',     
                            color='black', 
                            linewidth=1.5)
                    )
        plt.show()


        fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(25, 14))
        fig.suptitle(f"Launch")
        ax0.plot(t, v, label='Velocity', c='red')
        ax0.set_title("Velocity vs Time")
        ax0.set_xlabel("Time (s)")
        ax0.set_ylabel("Velocity")

        plt.show()
    """


if __name__ == "__main__":
    # SET DESIRED ORBIT HEIGHT > 99000m
    orbit_height = 100000.0  # m

    # Comparing with Rocket Lab's Electron 47 launch which had a starting velocity of 28570 km/h
    # for an elliptical orbit. This gave initial velocity of ~28000 km/h. Starting positions and
    # orbital path differ, however the similarity is encouraging.
    # orbit_height = 210000.6

    r = float(data.rplanet + orbit_height)

    # Set desired target position
    country = "united states"
    city = "salt lake city"

    # This gives us our starting positions and velocities
    get_pos = lp.LaunchPosition(country, city, r, data.G, data.mplanet)
    state_initial = get_pos._get_launch_pos()
    target = get_pos.target_pos

    # Pass starting positions and velocities into SatelliteOrbit class
    orbit = sat.SatelliteOrbit(state_initial, orbit_height, 0.6, city, anomoly=2)

    stateout = orbit._solve()
    # orbit._plot_states()

    plot = Plotter(data=stateout)
    plot.satellite()
