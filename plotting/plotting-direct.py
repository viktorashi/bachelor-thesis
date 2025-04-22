from matplotlib import pyplot

plot = pyplot.plot
axis = pyplot.axis
subplot = pyplot.subplot
title = pyplot.title
show = pyplot.show

dt = 0.01

#pt vna-der-pol

def init_vars():
    global x, y, xres, yres
    x = y = 0.1
    xres = [x]
    yres = [y]

def observe():
    global x,y, xres, yres
    xres.append(x)
    yres.append(y)

def update():
    global x,y, xres, yres
    dx_dt = y
    dy_dt = -r * (x**2 -1) * y -x 

    nextx = x + dx_dt * dt
    nexty = y + dy_dt * dt
    x,y = nextx, nexty

def plot_phase_space():
    init_vars()
    for _ in range(10000):
        update()
        observe()

    plot(xres, yres)
    axis('image')
    axis([-3,3,-3,3])
    title('r = ' + str(r))

def plot_everything():
    global r ,rs
    rs = [-1, -0.1, 0, .1, 1] 
    for i in range(len(rs)):
        subplot(1,len(rs), i+1)
        r = rs[i]
        plot_phase_space()
    show()

plot_everything()
