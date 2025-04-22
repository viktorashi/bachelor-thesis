# deci pe asta poti sa-l folosesti pt orice sistem de ecuatii de 2 variabile si sa-ti faca plotu, gen doar schimbi acolo ce formula au ecuatiile and you're set
from matplotlib import pyplot

plot = pyplot.plot
axis = pyplot.axis
subplot = pyplot.subplot
title = pyplot.title
show = pyplot.show


#statica
global dt
dt = 0.01

#astea sunt overrided de subclase:
rs = [-1, -0.1, 0, .1, 1] 

def init_vars():
    global x, y, xres, yres
    x = y = 0.1
    xres = [x]
    yres = [y]

def observe():
    global x,y, xres, yres
    xres.append(x)
    yres.append(y)

def plot_phase_space(update_func):
    init_vars()
    global x,y, xres, yres ,r, dt
    for _ in range(10000):
        update_func(x,y, r, dt)
        observe()

    plot(xres, yres)
    axis('image')
    axis([-3,3,-3,3])
    title('r = ' + str(r))


def plot_everything(update_func):
    global r ,rs
    rs = [-1, -0.1, 0, .1, 1] 
    for i in range(len(rs)):
        subplot(1,len(rs), i+1)
        r = rs[i]
        plot_phase_space(update_func)
    show()

"""

la asta o sa-i dai "overload" in alte fisiere

def update():
    global x,y, xres, yres
    dx_dt = y
    dy_dt = -r * (x**2 -1) * y -x 

    nextx = x + dx_dt * dt
    nexty = y + dy_dt * dt
    x,y = nextx, nexty

si gen asa le dai call
plot_everything(update_func=update)

"""