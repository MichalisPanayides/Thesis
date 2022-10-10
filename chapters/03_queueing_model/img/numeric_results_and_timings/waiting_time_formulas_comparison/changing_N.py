import time

import ambulance_game as abg
import matplotlib.pyplot as plt
import numpy as np


def output_to_file(str_list, filename="demo.csv"):
    with open(filename, "a") as f:
        f.write(str_list + "\n")


lambda_1 = 5
lambda_2 = 5
mu = 3
num_of_servers = 4
threshold = 10
system_capacity = 15
buffer_capacity = 15


waiting_formulas = (
    abg.markov.mean_waiting_time_formula_using_recursive_approach,
    abg.markov.mean_waiting_time_formula_using_direct_approach,
    abg.markov.mean_waiting_time_formula_using_closed_form_approach,
)


num_of_trials = 20
start, end = 10, 70
system_capapcity_space = np.linspace(start, end, end - start + 1, dtype=int)


all_durations_sys = []
all_waiting_times_sys = []
for system_capacity_i in system_capapcity_space:
    waiting_times = [0, 0, 0]
    durations = [0, 0, 0]
    for i, selected_waiting_formula in enumerate(waiting_formulas):
        for _ in range(num_of_trials):
            start_time = time.time()
            waiting_times[
                i
            ] = abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
                lambda_1=lambda_1,
                lambda_2=lambda_2,
                mu=mu,
                num_of_servers=num_of_servers,
                threshold=threshold,
                system_capacity=system_capacity_i,
                buffer_capacity=buffer_capacity,
                class_type=None,
                waiting_formula=selected_waiting_formula,
            )
            end_time = time.time()
            durations[i] += end_time - start_time
        durations[i] /= num_of_trials
    if not np.allclose(waiting_times[0], waiting_times[1], waiting_times[2]):
        print(system_capacity_i, end="\t")
        print(waiting_times)
    all_durations_sys.append(durations)
    all_waiting_times_sys.append(waiting_times)

for row in all_durations_sys:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/algorithm_duration_over_N.csv",
    )

for row in all_waiting_times_sys:
    output_to_file(
        str_list=str(row).replace("[", "").replace("]", ""),
        filename="data/waiting_times_over_N.csv",
    )
