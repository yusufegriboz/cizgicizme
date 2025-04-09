from pylab import *
import matplotlib.pyplot as plt

x = [2,-3,-1.5,3]
y = [3,1,-2.5,-2]
color=['m','g','r','b']
fig = plt.figure()
ax = fig.add_subplot(111)
scatter(x,y, s=100 ,marker='o', c=color)

# Döngüdeki taşma sorunu halloldu
for i in range(len(x)):
    plt.plot(x[i:i+2], y[i:i+2], 'ro-')

left, right = ax.get_xlim()
low, high = ax.get_ylim()

# 1. bölgedeki (2, 3) ve 4. bölgedeki (3, -2) noktayı birleştiren çizgiyi ekliyoruz
plt.plot([x[0], x[3]], [y[0], y[3]], 'b-', lw=2)  # 1. ve 4. bölgeyi birleştiren çizgi

# Yatay ve dikey okları çiz
arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.15)
arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.15)

# Eksen çizgisi
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)

# Grid
grid(True)

show()
