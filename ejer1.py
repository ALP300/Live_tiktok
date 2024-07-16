import matplotlib.pyplot as plt
import numpy as np

def plot_flow_lines(source=True, save=False):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    # Define the grid
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    
    # Define the potential function for source or sink
    Z = np.log(np.sqrt(X*2 + Y*2))
    if not source:
        Z = -Z

    # Define the stream function
    stream_function = np.arctan2(Y, X)
    if not source:
        stream_function = -stream_function

    # Plot equipotential lines
    ax.contour(X, Y, Z, levels=np.linspace(-2, 2, 25), colors='blue', linestyles='dotted')

    # Plot streamlines
    ax.streamplot(X, Y, X/np.sqrt(X*2 + Y2), Y/np.sqrt(X2 + Y*2), color='red')

    # Plot source or sink point
    ax.plot(0, 0, 'ro')

    ax.set_title("Source" if source else "Sink")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    
    if save:
        plt.savefig(f"{'source' if source else 'sink'}.png")

    plt.show()

# Plot source
plot_flow_lines(source=True)

# Plot sink
plot_flow_lines(source=False)