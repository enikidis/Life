import matplotlib.pyplot as plt


def run_popup(grid, step_fn, delay=0.05):
    """Run an interactive popup window until any key is pressed."""
    running = True

    def on_key(event):
        nonlocal running
        running = False

    plt.ion()
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect("key_press_event", on_key)

    while running:
        ax.clear()
        ax.imshow(grid, cmap="binary", interpolation="nearest")
        ax.axis("off")
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(delay)
        grid = step_fn(grid)

    plt.close(fig)
