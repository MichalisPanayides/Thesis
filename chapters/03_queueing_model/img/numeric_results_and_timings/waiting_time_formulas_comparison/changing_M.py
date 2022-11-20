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


num_of_trials = 50
start, end = 10, 70
buffer_capacity_space = np.linspace(start, end, end - start + 1, dtype=int)


waiting_times = [[] for _ in range(3)]
durations = [[] for _ in range(3)]
for buffer_capacity_i in buffer_capacity_space:
    for i, selected_waiting_formula in enumerate(waiting_formulas):
        for _ in range(num_of_trials):
            start_time = time.time()
            waiting_times[i].append(
                abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
                    lambda_1=lambda_1,
                    lambda_2=lambda_2,
                    mu=mu,
                    num_of_servers=num_of_servers,
                    threshold=threshold,
                    system_capacity=system_capacity,
                    buffer_capacity=buffer_capacity_i,
                    class_type=None,
                    waiting_formula=selected_waiting_formula,
                )
            )
            end_time = time.time()
            durations[i].append(end_time - start_time)


filenames = [
    "data/waiting_time_recursive_M.csv",
    "data/waiting_time_direct_M.csv",
    "data/waiting_time_closed_form_M.csv",
]

filenames_duration = [
    "data/duration_recursive_M.csv",
    "data/duration_direct_M.csv",
    "data/duration_closed_form_M.csv",
]


for values, filename in zip(waiting_times, filenames):
    for trial in range(end - start + 1):
        output_to_file(
            str_list=str(values[trial * num_of_trials : (trial + 1) * num_of_trials])
            .replace("[", "")
            .replace("]", ""),
            filename=filename,
        )

for values, filename in zip(durations, filenames_duration):
    for trial in range(end - start + 1):
        output_to_file(
            str_list=str(values[trial * num_of_trials : (trial + 1) * num_of_trials])
            .replace("[", "")
            .replace("]", ""),
            filename=filename,
        )
