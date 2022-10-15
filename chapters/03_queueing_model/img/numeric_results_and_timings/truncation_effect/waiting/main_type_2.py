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
    print(lambda_2)
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
        class_type=1,
    )
    all_sim_unbound_waiting_times.append(
        [np.mean(w.waiting_times) for w in unbounded_simulation_results]
    )

    for capacity_value in all_capacity_values:
        # Markov
        markov_waiting_time = abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=capacity_value,
            buffer_capacity=capacity_value,
            class_type=1,
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
            class_type=1,
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


for row in all_sim_unbound_waiting_times:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_unbound_waiting_times_type_2.csv",
    )

for row in all_sim_bound_waiting_times_low:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_waiting_times_low_type_2.csv",
    )

for row in all_sim_bound_waiting_times_mid:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_waiting_times_mid_type_2.csv",
    )

for row in all_sim_bound_waiting_times_high:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_waiting_times_high_type_2.csv",
    )

for row in all_markov_waiting_times_low:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_waiting_times_low_type_2.csv",
    )

for row in all_markov_waiting_times_mid:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_waiting_times_mid_type_2.csv",
    )

for row in all_markov_waiting_times_high:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_waiting_times_high_type_2.csv",
    )
