"""
Code to generate the animated heatmaps
"""
import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg


# Parameters
lambda_2 = 0.3
lambda_1 = 0.3
mu_space = np.linspace(0.03, 0.3, 10)
num_of_servers = 5
threshold = num_of_servers
system_capacity = 20
buffer_capacity = 20

runtime = 10000
num_of_trials = 10
seed_num = 0

fig_num = 0
for mu in mu_space:
    plt.figure(figsize=(20, 10))
    (
        sim_state_probabilities_array,
        markov_state_probabilities_array,
        diff_states_probabilities_array,
    ) = abg.comparisons.get_heatmaps(
        lambda_2,
        lambda_1,
        mu,
        num_of_servers,
        threshold,
        system_capacity,
        buffer_capacity,
        runtime=runtime,
        num_of_trials=num_of_trials,
        seed_num=seed_num,
    )

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))

    pos1 = ax1.imshow(sim_state_probabilities_array, cmap="cividis")
    ax1.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    ax1.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )
    ax1.set_title("Simulation state probabilities", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Individuals in node 1", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Individuals in node 2", fontsize=11, fontweight="bold")
    fig.colorbar(pos1, ax=ax1)

    pos2 = ax2.imshow(markov_state_probabilities_array, cmap="cividis")
    ax2.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    ax2.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )

    ax2.set_title("Markov chain state probabilities", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Individuals in node 1", fontsize=11, fontweight="bold")
    ax2.set_ylabel("Individuals in node 2", fontsize=11, fontweight="bold")
    fig.colorbar(pos2, ax=ax2)

    pos3 = ax3.imshow(diff_states_probabilities_array, cmap="viridis")
    ax3.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    ax3.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )
    ax3.set_title(
        "Simulation and Markov chain state\nprobability differences",
        fontsize=11,
        fontweight="bold",
    )
    ax3.set_xlabel("Individuals in node 1", fontsize=11, fontweight="bold")
    ax3.set_ylabel("Individuals in node 2", fontsize=11, fontweight="bold")
    fig.colorbar(pos3, ax=ax3)

    fig_num += 1
    plt.savefig("main_" + str(fig_num) + ".pdf")
    plt.close()
