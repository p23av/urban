import requests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd
import openpyxl

# --- REQUESTS ---
r_get = requests.get('https://api.github.com/events')
r_post = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(r_get.text)
print(r_get.json())
print(r_post)
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
r_auth = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(f'>>> auth: {r_auth.json()}')

# --- MATPLOTLIB ---
fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], linewidth=2, color='green', label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)

ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()

# --- PANDAS ---
df = pd.read_excel('./Импортные разъемы.xlsx')

print(df)

dff = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    dff.to_excel(writer)
