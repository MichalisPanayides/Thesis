import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np

A = np.array([
    [4, 1, 3],
    [2, 0, 2],
    [3, 4, 1]]
)
B = np.array([
    [4, 5, 1],
    [2, 3, 2],
    [6, 4, 0]]
)
game = nash.Game(A, B)

#####################
## Fictitious Play ##
#####################

np.random.seed(0)
play_counts = tuple(game.fictitious_play(iterations=1000))

probabilities_row = [
    row_play_counts / np.sum(row_play_counts)
    for row_play_counts, col_play_counts in play_counts[1:]
]
probabilities_col = [
    col_play_counts / np.sum(col_play_counts)
    for row_play_counts, col_play_counts in play_counts[1:]
]
plt.figure()
for number, strategy in enumerate(zip(*probabilities_row)):
    plt.plot(strategy, label=f"$s_{number}$")
plt.title("Row Player Strategies")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.legend()
plt.savefig("fictitious_row.pdf");

plt.figure()
for number, strategy in enumerate(zip(*probabilities_col)):
    plt.plot(strategy, label=f"$s_{number}$")
plt.title("Column Player Strategies")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.legend()
plt.savefig("fictitious_col.pdf");


################################
## Stochastic Fictitious play ##
################################

np.random.seed(0)
play_counts_and_distributions = tuple(
    game.stochastic_fictitious_play(iterations=1000)
)
play_count, distribution = play_counts_and_distributions[-1]

probabilities_row = [
    row_play_counts / np.sum(row_play_counts)
    if np.sum(row_play_counts) != 0
    else row_play_counts + 1 / len(row_play_counts)
    for (row_play_counts, col_play_counts), _ in play_counts_and_distributions]
plt.figure()
for number, strategy in enumerate(zip(*probabilities_row)):
    plt.plot(strategy, label=f"$s_{number}$")
plt.title("Row Player Strategies")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.legend()
plt.savefig("stochastic_row.pdf");


probabilities_col = [
    col_play_counts / np.sum(col_play_counts)
    if np.sum(col_play_counts) != 0
    else col_play_counts + 1 / len(col_play_counts)
    for (row_play_counts, col_play_counts), _ in play_counts_and_distributions]
plt.figure()
for number, strategy in enumerate(zip(*probabilities_col)):
    plt.plot(strategy, label=f"$s_{number}$")
plt.title("Column Player Strategies")
plt.xlabel("Iteration")
plt.ylabel("Probability")
plt.legend()
plt.savefig("stochastic_col.pdf");


####################################
## Assymetric Replicator Dynamics ##
####################################

np.random.seed(0)
xs, ys = game.asymmetric_replicator_dynamics(
    timepoints=np.linspace(0, 100, 100),
)
plt.figure()
plt.plot(xs)
plt.title("Row Player Strategies")
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.legend(['$s_1$', '$s_2$', '$s_3$'])
plt.savefig("asymmetric_rd_row.pdf");

plt.figure()
plt.plot(ys)
plt.title("Column Player Strategies")
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.legend(['$s_1$', '$s_2$', '$s_3$'])
plt.savefig("asymmetric_rd_col.pdf");


######################################
## Asymmetric Replicator Dynamics 2 ##
######################################

A = np.array([
    [4, 1],
    [2, 5],
])
B = np.array([
    [4, 5],
    [2, 3],
])
game = nash.Game(A, B)

x0 = np.array([0.9, 0.1])
y0 = np.array([0.9, 0.1])
xs, ys = game.asymmetric_replicator_dynamics(
    timepoints=np.linspace(0, 20, 100),
    x0=x0,
    y0=y0,
)

plt.figure()
plt.plot(xs)
plt.title("Row Player Strategies")
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.legend(['$s_1$', '$s_2$', '$s_3$'])
plt.savefig("asymmetric_rd_2_row.pdf");

plt.figure()
plt.plot(ys)
plt.title("Column Player Strategies")
plt.xlabel("Timepoints")
plt.ylabel("Probability")
plt.legend(['$s_1$', '$s_2$', '$s_3$'])
plt.savefig("asymmetric_rd_2_col.pdf");
