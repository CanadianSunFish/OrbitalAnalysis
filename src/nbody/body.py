import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

from src.utils import data


class Body:

    def __init__(self, pos, vel, mass) -> None:
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.acc = np.zeros(3)
        self.force = np.zeros(3)

    def gravity(self, other):

        r = self.pos - other.pos

        r_mag = np.linalg.norm(r)

        force = -data.G * self.mass * other.mass * r / (r_mag**3)

        return force

    def update(self, force, time_step):

        self.acc = force / self.mass

        self.vel += time_step * self.acc
        self.pos += time_step * self.vel


p1 = np.array([1.0, -1.3, -0.2])
p2 = np.array([0.3, 0.0, 0.0])
p3 = np.array([2.0, -0.5, 0.4])

v1 = np.array([0.1, -0.01, 0.05])
v2 = np.array([-0.13, 0.03, 0.04])
v3 = np.array([0.02, 0.02, 0.1])

test = Body(p1, v1, 2e8)
test2 = Body(p2, v2, 2e8)
test3 = Body(p3, v3, 2e8)

x = []
y = []
z = []

x1 = []
y1 = []
z1 = []

x2 = []
y2 = []
z2 = []

for i in range(125000):

    force1 = test.gravity(test2)
    force2 = test.gravity(test3)

    test.update(force1 + force2, 0.1)

    force3 = test2.gravity(test3)

    test2.update(-force1 + force3, 0.1)

    test3.update(-(force2 + force3), 0.1)

    x.append(test.pos[0])
    y.append(test.pos[1])
    z.append(test.pos[2])

    x1.append(test2.pos[0])
    y1.append(test2.pos[1])
    z1.append(test2.pos[2])

    x2.append(test3.pos[0])
    y2.append(test3.pos[1])
    z2.append(test3.pos[2])


print(x)

fig = plt.figure()
ax = plt.subplot(projection="3d")
ax.set(xlim=[-4, 4], ylim=[-4, 4], zlim=[-4, 4])

scat = ax.scatter(x[0], y[0], z[0])
scat2 = ax.scatter(x1[0], y1[0], z1[0])
scat3 = ax.scatter(x2[0], y2[0], z2[0])


def update(frame):

    scat._offsets3d = (x[:frame], y[:frame], z[:frame])
    scat2._offsets3d = (x1[:frame], y1[:frame], z1[:frame])
    scat3._offsets3d = (x2[:frame], y2[:frame], z2[:frame])

    return scat


ani = animation.FuncAnimation(fig=fig, func=update, frames=10000, interval=30)
plt.show()
plt.close()

# fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(8, 10), sharex=True)

# # Plot on each subplot
# ax1.plot(range(len(x)), x)
# ax1.set_title("X")
# ax1.set_ylabel("x")

# ax2.plot(range(len(y)), y)
# ax2.set_title("Y")
# ax2.set_ylabel("y")

# ax3.plot(range(len(z)), z)
# ax3.set_title("Z")
# ax3.set_xlabel("Time (0.5 s)")
# ax3.set_ylabel("z")

# ax4.plot(range(len(x1)), x1)
# ax4.set_title("X")
# ax4.set_ylabel("x")

# ax5.plot(range(len(y1)), y1)
# ax5.set_title("Y")
# ax5.set_ylabel("y")

# ax6.plot(range(len(z1)), z1)
# ax6.set_title("Z")
# ax6.set_xlabel("Time (0.5 s)")
# ax6.set_ylabel("z")

# plt.tight_layout()
# plt.show()
