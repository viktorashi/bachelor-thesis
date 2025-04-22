from matplotlib import pyplot

plot = pyplot.plot
axis = pyplot.axis
subplot = pyplot.subplot
title = pyplot.title
show = pyplot.show

dt = 0.01

#absout tot codul de aici tre sa-i dai copy-paste ca sa incerci sa faci toata nebunia din nou cu alte functii si sa schimni valorile in functia de update() gen daor atat pare foarte usor de modularising dar pt ca nu stiu cum functioneaza globalele in python nu pot sa moara masa

def init_vars():
    global x, y, xres, yres
    x = y = 0.1
    xres = [x]
    yres = [y]

def observe():
    global x,y, xres, yres
    xres.append(x)
    yres.append(y)


def plot_phase_space():
    init_vars()
    for _ in range(100000):
        update()
        observe()

    plot(xres, yres)
    axis('image')
    axis([-3,3,-3,3])
    title('r = ' + str(r))

############### AICI SCHIMBI ######################

#r-urile pe care sa le schimbi sa vezi bifurcatia la ele daca e sau ba
rs = [-2, -1.5, -1, -0.5, 0] 

def update():
    global x,y, xres, yres
    dx_dt = 3 * (x - x**3/3 + y + r)
    dy_dt = - (x - 0.7 + 0.8* y)/3

    nextx = x + dx_dt * dt
    nexty = y + dy_dt * dt
    x,y = nextx, nexty


for i in range(len(rs)):
    subplot(1,len(rs), i+1)
    r = rs[i]
    plot_phase_space()
show()
