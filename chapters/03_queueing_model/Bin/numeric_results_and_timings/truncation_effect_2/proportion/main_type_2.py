from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import ambulance_game as abg


def output_to_file(str_list, filename="demo.csv"):
    with open(filename, "a") as f:
        f.write(str_list + "\n")


lambda_1 = 4
mu = 2
num_of_servers = 5
threshold = 12
target = 1
seed_num = 1
warm_up_time = 150
num_of_trials = 30
runtime = 10000

lambda_2_space = np.linspace(1, 10, 6)
all_capacity_values = (15, 30, 60)

all_sim_unbound_props = []
all_sim_bound_props_low = []
all_sim_bound_props_mid = []
all_sim_bound_props_high = []

all_markov_props_low = []
all_markov_props_mid = []
all_markov_props_high = []
for lambda_2 in lambda_2_space:
    # Unbounded simulation
    (
        _,
        _,
        unbounded_simulation_results,
    ) = abg.simulation.get_mean_proportion_of_individuals_within_target_for_multiple_runs(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=float("inf"),
        buffer_capacity=float("inf"),
        seed_num=seed_num,
        num_of_trials=num_of_trials,
        runtime=runtime,
        target=target,
    )
    all_sim_unbound_props.append(unbounded_simulation_results)

    for capacity_value in all_capacity_values:
        # Markov
        markov_proportions = abg.markov.proportion_within_target_using_markov_state_probabilities(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=capacity_value,
            buffer_capacity=capacity_value,
            class_type=1,
            target=target,
        )

        # Bounded simulation
        (
            _,
            _,
            bounded_simulation_results,
        ) = abg.simulation.get_mean_proportion_of_individuals_within_target_for_multiple_runs(
            lambda_2=lambda_2,
            lambda_1=lambda_1,
            mu=mu,
            num_of_servers=num_of_servers,
            threshold=threshold,
            system_capacity=capacity_value,
            buffer_capacity=capacity_value,
            seed_num=seed_num,
            num_of_trials=num_of_trials,
            runtime=runtime,
            target=target,
        )
        if capacity_value == all_capacity_values[0]:
            all_markov_props_low.append(markov_proportions)
            all_sim_bound_props_low.append(bounded_simulation_results)
        elif capacity_value == all_capacity_values[1]:
            all_markov_props_mid.append(markov_proportions)
            all_sim_bound_props_mid.append(bounded_simulation_results)
        elif capacity_value == all_capacity_values[2]:
            all_markov_props_high.append(markov_proportions)
            all_sim_bound_props_high.append(bounded_simulation_results)
        else:
            raise ValueError("Invalid capacity value")


for row in all_sim_unbound_props:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_unbound_props_type_2.csv",
    )


for row in all_sim_bound_props_low:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_props_low_type_2.csv",
    )


for row in all_sim_bound_props_mid:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_props_mid_type_2.csv",
    )


for row in all_sim_bound_props_high:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/sim_bound_props_high_type_2.csv",
    )


for row in all_markov_props_low:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_props_low_type_2.csv",
    )


for row in all_markov_props_mid:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_props_mid_type_2.csv",
    )


for row in all_markov_props_high:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/markov_props_high_type_2.csv",
    )

