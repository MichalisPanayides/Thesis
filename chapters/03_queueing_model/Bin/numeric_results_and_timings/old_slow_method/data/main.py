import time

import numpy as np
import ambulance_game as abg

lambda_2 = 4

lambda_1 = 2
mu = 3
num_of_servers = 3
threshold = 8
buffer_capacity = 15
warm_up_time = 100
runtime = 10000

capacities = (10, 30, 50)


def output_to_file(str_list, filename="demo.csv"):
    with open(filename, "a") as f:
        f.write(str_list + "\n")


simulation_single_trial_unbounded = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=float("inf"),
        buffer_capacity=float("inf"),
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=1,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_single_trial_unbounded.append(end_time - start_time)
output_to_file(
    str(simulation_single_trial_unbounded), "simulation_single_trial_unbounded.csv"
)
print("simulation_single_trial_unbounded.csv created")

simulation_single_trial_bounded_10 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=10,
        buffer_capacity=10,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=1,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_single_trial_bounded_10.append(end_time - start_time)
output_to_file(
    str(simulation_single_trial_bounded_10),
    "simulation_single_trial_bounded_10.csv",
)
print("simulation_single_trial_bounded_10.csv created")

simulation_single_trial_bounded_30 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=30,
        buffer_capacity=30,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=1,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_single_trial_bounded_30.append(end_time - start_time)
output_to_file(
    str(simulation_single_trial_bounded_30),
    "simulation_single_trial_bounded_30.csv",
)
print("simulation_single_trial_bounded_30.csv created")


simulation_single_trial_bounded_50 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=50,
        buffer_capacity=50,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=1,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_single_trial_bounded_50.append(end_time - start_time)
output_to_file(
    str(simulation_single_trial_bounded_50),
    "simulation_single_trial_bounded_50.csv",
)
print("simulation_single_trial_bounded_50.csv created")


simulation_hundred_trials_unbounded = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=float("inf"),
        buffer_capacity=float("inf"),
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=100,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_hundred_trials_unbounded.append(end_time - start_time)
output_to_file(
    str(simulation_hundred_trials_unbounded),
    "simulation_hundred_trials_unbounded.csv",
)
print("simulation_hundred_trials_unbounded.csv created")


simulation_hundred_trials_bounded_10 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=10,
        buffer_capacity=10,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=100,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_hundred_trials_bounded_10.append(end_time - start_time)
output_to_file(
    str(simulation_hundred_trials_bounded_10),
    "simulation_hundred_trials_bounded_10.csv",
)
print("simulation_hundred_trials_bounded_10.csv created")


simulation_hundred_trials_bounded_30 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=30,
        buffer_capacity=30,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=100,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_hundred_trials_bounded_30.append(end_time - start_time)
output_to_file(
    str(simulation_hundred_trials_bounded_30),
    "simulation_hundred_trials_bounded_30.csv",
)
print("simulation_hundred_trials_bounded_30.csv created")


simulation_hundred_trials_bounded_50 = []
for _ in range(2):
    start_time = time.time()
    abg.simulation.get_multiple_runs_results(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=50,
        buffer_capacity=50,
        seed_num=None,
        warm_up_time=warm_up_time,
        num_of_trials=100,
        runtime=runtime,
        class_type=None,
    )
    end_time = time.time()
    simulation_hundred_trials_bounded_50.append(end_time - start_time)
output_to_file(
    str(simulation_hundred_trials_bounded_50),
    "simulation_hundred_trials_bounded_50.csv",
)
print("simulation_hundred_trials_bounded_50.csv created")


markov_waiting_formula_bounded_10 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=10,
        buffer_capacity=10,
        class_type=None,
    )
    end_time = time.time()
    markov_waiting_formula_bounded_10.append(end_time - start_time)
output_to_file(
    str(markov_waiting_formula_bounded_10), "markov_waiting_formula_bounded_10.csv"
)
print("markov_waiting_formula_bounded_10.csv created")

markov_waiting_formula_bounded_30 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=30,
        buffer_capacity=30,
        class_type=None,
    )
    end_time = time.time()
    markov_waiting_formula_bounded_30.append(end_time - start_time)
output_to_file(
    str(markov_waiting_formula_bounded_30), "markov_waiting_formula_bounded_30.csv"
)
print("markov_waiting_formula_bounded_30.csv created")

markov_waiting_formula_bounded_50 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_waiting_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=50,
        buffer_capacity=50,
        class_type=None,
    )
    end_time = time.time()
    markov_waiting_formula_bounded_50.append(end_time - start_time)
output_to_file(
    str(markov_waiting_formula_bounded_50), "markov_waiting_formula_bounded_50.csv"
)
print("markov_waiting_formula_bounded_50.csv created")


markov_blocking_formula_bounded_10 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=10,
        buffer_capacity=10,
    )
    end_time = time.time()
    markov_blocking_formula_bounded_10.append(end_time - start_time)
output_to_file(
    str(markov_blocking_formula_bounded_10),
    "markov_blocking_formula_bounded_10.csv",
)
print("markov_blocking_formula_bounded_10.csv created")

markov_blocking_formula_bounded_30 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=30,
        buffer_capacity=30,
    )
    end_time = time.time()
    markov_blocking_formula_bounded_30.append(end_time - start_time)
output_to_file(
    str(markov_blocking_formula_bounded_30),
    "markov_blocking_formula_bounded_30.csv",
)
print("markov_blocking_formula_bounded_30.csv created")

markov_blocking_formula_bounded_50 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.get_mean_blocking_time_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=50,
        buffer_capacity=50,
    )
    end_time = time.time()
    markov_blocking_formula_bounded_50.append(end_time - start_time)
output_to_file(
    str(markov_blocking_formula_bounded_50),
    "markov_blocking_formula_bounded_50.csv",
)
print("markov_blocking_formula_bounded_50.csv created")

markov_proportion_formula_bounded_10 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=10,
        buffer_capacity=10,
        class_type=None,
        target=0.5,
    )
    end_time = time.time()
    markov_proportion_formula_bounded_10.append(end_time - start_time)
output_to_file(
    str(markov_proportion_formula_bounded_10),
    "markov_proportion_formula_bounded_10.csv",
)
print("markov_proportion_formula_bounded_10.csv created")

markov_proportion_formula_bounded_30 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=30,
        buffer_capacity=30,
        class_type=None,
        target=0.5,
    )
    end_time = time.time()
    markov_proportion_formula_bounded_30.append(end_time - start_time)
output_to_file(
    str(markov_proportion_formula_bounded_30),
    "markov_proportion_formula_bounded_30.csv",
)
print("markov_proportion_formula_bounded_30.csv created")

markov_proportion_formula_bounded_50 = []
for _ in range(2):
    start_time = time.time()
    abg.markov.proportion_within_target_using_markov_state_probabilities(
        lambda_2=lambda_2,
        lambda_1=lambda_1,
        mu=mu,
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=50,
        buffer_capacity=50,
        class_type=None,
        target=0.5,
    )
    end_time = time.time()
    markov_proportion_formula_bounded_50.append(end_time - start_time)
output_to_file(
    str(markov_proportion_formula_bounded_50),
    "markov_proportion_formula_bounded_50.csv",
)
print("markov_proportion_formula_bounded_50.csv created")
