from bifurcation_plot_tools import plot_everything

global x, y, xres, yres, dt, r
# la asta o sa-i dai "overload" in alte fisiere
def update(x,y,r, dt):

    dx_dt = y
    dy_dt = -r * (x**2 -1) * y -x 

    nextx = x + dx_dt * dt
    nexty = y + dy_dt * dt
    x,y = nextx, nexty


plot_everything(update_func=update)
