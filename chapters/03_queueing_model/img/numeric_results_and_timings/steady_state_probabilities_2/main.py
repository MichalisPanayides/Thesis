"""
Code to generate the animated heatmaps
"""
import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg

# Parameters
lambda_2 = 1
lambda_1 = 1.5
mu = 0.7
num_of_servers_space = np.linspace(1, 6, 6, dtype=int)
threshold = 13
system_capacity = 20
buffer_capacity = 20

runtime = 10000
num_of_trials = 10
seed_num = 0

fig = 0
for num_of_servers in num_of_servers_space:
    plt.figure(figsize=(20, 10))
    (
        sim_state_probabilities_array,
        markov_state_probabilities_array,
        diff_states_probabilities_array,
    ) = abg.comparisons.get_heatmaps(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=int(num_of_servers),
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
        runtime=runtime,
        num_of_trials=num_of_trials,
        seed_num=seed_num,
    )
    grid = plt.GridSpec(2, 4)

    plt.subplot(grid[0, 0:2])

    plt.imshow(sim_state_probabilities_array, cmap="cividis")
    plt.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    plt.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )
    plt.title("Simulation state probabilities", fontsize=11, fontweight="bold")
    plt.xlabel("Individuals in service area", fontsize=11, fontweight="bold")
    plt.ylabel("Individuals in buffer centre", fontsize=11, fontweight="bold")
    plt.colorbar()

    plt.subplot(grid[0, 2:4])
    plt.imshow(markov_state_probabilities_array, cmap="cividis")
    plt.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    plt.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )

    plt.title("Markov chain state probabilities", fontsize=11, fontweight="bold")
    plt.xlabel("Individuals in service area", fontsize=11, fontweight="bold")
    plt.ylabel("Individuals in buffer centre", fontsize=11, fontweight="bold")
    plt.colorbar()

    plt.subplot(grid[1, 1:3])
    plt.imshow(diff_states_probabilities_array, cmap="viridis")
    plt.hlines(
        y=np.arange(0, system_capacity) + 0.5,
        xmin=np.full(system_capacity, -0.5),
        xmax=np.full(system_capacity, buffer_capacity + 0.5),
        color="grey",
    )
    plt.vlines(
        x=np.arange(0, buffer_capacity) + 0.5,
        ymin=np.full(buffer_capacity, -0.5),
        ymax=np.full(buffer_capacity, system_capacity + 0.5),
        color="grey",
    )
    plt.title(
        "Simulation and Markov chain state probability differences",
        fontsize=11,
        fontweight="bold",
    )
    plt.xlabel("Individuals in service area", fontsize=11, fontweight="bold")
    plt.ylabel("Individuals in buffer centre", fontsize=11, fontweight="bold")
    plt.colorbar()

    fig += 1
    plt.savefig("main_" + str(fig) + ".pdf")
    plt.close()
