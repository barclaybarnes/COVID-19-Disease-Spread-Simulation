import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import CheckButtons, Slider, Button
from matplotlib.gridspec import GridSpec

def animate_epidemic_curve(csv_file="simulation_results.csv"):
    df = pd.read_csv(csv_file)
    days = df["day"].values
    S = df["S"].values
    E = df["E"].values
    I = df["I"].values
    R = df["R"].values
    V = df["V"].values

    fig = plt.figure(figsize=(14, 6))
    gs = GridSpec(2, 2, height_ratios=[12, 1], width_ratios=[4, 1], hspace=0.3, wspace=0.3)

    ax = fig.add_subplot(gs[0, 0])
    ax.set_xlim(days.min(), days.max())
    ax.set_ylim(0, max(S.max(), E.max(), I.max(), R.max(), V.max()) * 1.1)
    ax.set_xlabel("Day")
    ax.set_ylabel("Population")
    ax.set_title("COVID-19 Simulation (SEIRV) — Animated")

    line_S, = ax.plot([], [], 'b-', label="Susceptible")
    line_E, = ax.plot([], [], 'orange', label="Exposed")
    line_I, = ax.plot([], [], 'r-', label="Infected", linewidth=2)
    line_R, = ax.plot([], [], 'g-', label="Recovered")
    line_V, = ax.plot([], [], 'purple', label="Vaccinated")
    ax.legend(loc="upper right")

    # Checkboxes in separate panel
    check_ax = fig.add_subplot(gs[0, 1])
    check_ax.axis('off')
    labels = ["Susceptible", "Exposed", "Infected", "Recovered", "Vaccinated"]
    visibility = [True, True, True, True, True]
    check = CheckButtons(check_ax, labels, visibility)
    lines = [line_S, line_E, line_I, line_R, line_V]

    def func(label):
        idx = labels.index(label)
        lines[idx].set_visible(not lines[idx].get_visible())
        plt.draw()
    check.on_clicked(func)

    # Text box for SEIRV counts and day
    count_text = ax.text(1.05, 0.5, "", transform=ax.transAxes, va="center", fontsize=12,
                         bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7))

    # Slider and Play/Pause button
    slider_ax = fig.add_subplot(gs[1, 0])
    slider = Slider(slider_ax, "Day", days.min(), days.max(), valinit=days.min(), valstep=1)
    button_ax = fig.add_subplot(gs[1, 1])
    play_button = Button(button_ax, "Play", color="lightgray", hovercolor="gray")

    playing = [True]
    current_frame = [days.min()]

    def update(current_day):
        line_S.set_data(days[:current_day], S[:current_day])
        line_E.set_data(days[:current_day], E[:current_day])
        line_I.set_data(days[:current_day], I[:current_day])
        line_R.set_data(days[:current_day], R[:current_day])
        line_V.set_data(days[:current_day], V[:current_day])
        ax.set_title(f"COVID-19 Simulation (SEIRV) — Day {current_day}")
        idx = current_day - 1 if current_day > 0 else 0
        count_text.set_text(
            f"Day: {days[idx]}\n"
            f"S: {S[idx]}\n"
            f"E: {E[idx]}\n"
            f"I: {I[idx]}\n"
            f"R: {R[idx]}\n"
            f"V: {V[idx]}"
        )
        return line_S, line_E, line_I, line_R, line_V, count_text

    def slider_update(val):
        playing[0] = False
        play_button.label.set_text("Play")
        current_frame[0] = int(val)
        update(current_frame[0])
        plt.draw()
    slider.on_changed(slider_update)

    def play_pause(event):
        if not playing[0]:
            # If at end, reset to start
            if current_frame[0] >= days.max():
                current_frame[0] = days.min()
                slider.set_val(current_frame[0])
                update(current_frame[0])
        playing[0] = not playing[0]
        play_button.label.set_text("Pause" if playing[0] else "Play")
    play_button.on_clicked(play_pause)

    def anim_update(frame):
        if playing[0]:
            if current_frame[0] < days.max():
                current_frame[0] += 1
                slider.eventson = False
                slider.set_val(current_frame[0])
                slider.eventson = True
                update(current_frame[0])
            else:
                playing[0] = False
                play_button.label.set_text("Play")
        return line_S, line_E, line_I, line_R, line_V, count_text

    ani = FuncAnimation(fig, anim_update, frames=range(days.min(), days.max()+2), interval=50, blit=False, repeat=False)
    plt.show()

if __name__ == "__main__":
    animate_epidemic_curve("simulation_results.csv")
