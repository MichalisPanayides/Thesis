from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg


def output_to_file(str_list, filename="demo.csv"):
    with open(filename, "a") as f:
        f.write(str_list + "\n")


lambda_1 = 2
mu = 3
num_of_servers = 3
threshold = 8
seed_num = 1
warm_up_time = 100
num_of_trials = 20
runtime = 10000

lambda_2_space = np.linspace(2, 6, 6)
all_capacity_values = (10, 30, 50)

all_sim_unbound_waiting_times = []
all_sim_bound_waiting_times_low = []
all_sim_bound_waiting_times_mid = []
all_sim_bound_waiting_times_high = []

all_markov_waiting_times_low = []
all_markov_waiting_times_mid = []
all_markov_waiting_times_high = []
for lambda_2 in lambda_2_space:
    # Unbounded simulation
    unbounded_simulation_results = abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=float("inf"),
        buffer_capacity=float("inf"),
        seed_num=seed_num,
        warm_up_time=warm_up_time,
        num_of_trials=num_of_trials,
        runtime=runtime,
        class_type=None,
    )
    all_sim_unbound_waiting_times.append(
        [np.mean(w.waiting_times) for w in unbounded_simulation_results]
    )

    for capacity_value in all_capacity_values:
        # Markov
        markov_waiting_time = (
            abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
                lambda_2=lambda_2,
                lambda_1=lambda_1,
                mu=mu,
                num_of_servers=num_of_servers,
                threshold=threshold,
                system_capacity=capacity_value,
                buffer_capacity=capacity_value,
                class_type=None,
            )
        )
        # Bounded simulation
        bounded_simulation_results = abg.simulation.get_multiple_runs_results(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=capacity_value,
            buffer_capacity=capacity_value,
            seed_num=seed_num,
            warm_up_time=warm_up_time,
            num_of_trials=num_of_trials,
            runtime=runtime,
            class_type=None,
        )

        if capacity_value == all_capacity_values[0]:
            all_markov_waiting_times_low.append(markov_waiting_time)
            all_sim_bound_waiting_times_low.append(
                [np.mean(w.waiting_times) for w in bounded_simulation_results]
            )
        elif capacity_value == all_capacity_values[1]:
            all_markov_waiting_times_mid.append(markov_waiting_time)
            all_sim_bound_waiting_times_mid.append(
                [np.mean(w.waiting_times) for w in bounded_simulation_results]
            )
        elif capacity_value == all_capacity_values[2]:
            all_markov_waiting_times_high.append(markov_waiting_time)
            all_sim_bound_waiting_times_high.append(
                [np.mean(w.waiting_times) for w in bounded_simulation_results]
            )
        else:
            raise ValueError("Invalid capacity value")

# Waiting time both individuals
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
for index, (ax, all_markov_times, all_bounded_sim_times) in enumerate(
    zip(
        [ax1, ax2, ax3],
        [
            all_markov_waiting_times_low,
            all_markov_waiting_times_mid,
            all_markov_waiting_times_high,
        ],
        [
            all_sim_bound_waiting_times_low,
            all_sim_bound_waiting_times_mid,
            all_sim_bound_waiting_times_high,
        ],
    )
):
    ax.violinplot(
        all_sim_unbound_waiting_times,
        positions=lambda_2_space,
        showmeans=True,
        widths=0.3,
    )
    ax.violinplot(
        all_bounded_sim_times,
        positions=lambda_2_space,
        showmeans=True,
        widths=0.3,
    )
    ax.plot(
        lambda_2_space,
        all_markov_times,
        color="red",
    )

    legend_elements = [
        Line2D([0], [0], color="red", lw=2, label="Finite state Markov chain"),
        Patch(facecolor="tab:blue", label="Simulation", alpha=0.6),
        Patch(facecolor="tab:orange", label="Truncated simulation", alpha=0.6),
    ]
    ax.legend(handles=legend_elements, loc="upper left")
    ax.set_title(f"$N$ = $M$ = {all_capacity_values[index]}")
    ax.set_xlabel("$\lambda_2$")
    ax.set_ylabel("Waiting time")

plt.suptitle("Truncation effect on waiting time")
plt.savefig("demo.pdf", transparent=True)

output_to_file(str(all_sim_unbound_waiting_times), "sim_unbound_waiting_times.csv")
output_to_file(str(all_sim_bound_waiting_times_low), "sim_bound_waiting_times_low.csv")
output_to_file(str(all_sim_bound_waiting_times_mid), "sim_bound_waiting_times_mid.csv")
output_to_file(
    str(all_sim_bound_waiting_times_high), "sim_bound_waiting_times_high.csv"
)
output_to_file(str(all_markov_waiting_times_low), "markov_waiting_times_low.csv")
output_to_file(str(all_markov_waiting_times_mid), "markov_waiting_times_mid.csv")
output_to_file(str(all_markov_waiting_times_high), "markov_waiting_times_high.csv")
