# Zaroori libraries import karna
import numpy as np
import matplotlib.pyplot as plt

# Satellites aur receiver ka location define karna
satellites = {
    'S1': (0, 5000),  # (x, y) coordinates in km
    'S2': (3000, 4000),
    'S3': (-3000, 3000),
    'S4': (5000, 1000),
    'S5': (-4000, -2000),
    'S6': (2000, -3000),
    'S7': (-5000, 500),  # Total of 7 satellites as in IRNSS
}

receiver = (1000, 2000)  # Receiver location in km

# Dono points ke darmiyan distance calculate karne ka function
def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Receiver se satellites tak ke distances calculate karna
distances = {sat: distance(receiver, coords) for sat, coords in satellites.items()}

# Plot ka setup
fig, ax = plt.subplots(figsize=(8, 8))

# Satellites ko plot karna
for sat, coords in satellites.items():
    ax.scatter(coords[0], coords[1], label=sat, color='blue', s=100)

# Receiver ko plot karna
ax.scatter(receiver[0], receiver[1], label='Receiver', color='red', s=150)

# Points ko annotate karna
for sat, coords in satellites.items():
    ax.annotate(sat, (coords[0], coords[1]), textcoords="offset points", xytext=(0,10), ha='center')

# Labels aur grid add karna
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_title("IRNSS Signal Simulation")

# Legend dikhana
plt.legend()

# Grid show karna
plt.grid(True)

# Plot ko display karna
plt.show()

# Receiver se satellites tak ki distances print karna
print("Receiver se satellites tak ki distances:")
for sat, dist in distances.items():
    print(f"{sat}: {dist:.2f} km")
