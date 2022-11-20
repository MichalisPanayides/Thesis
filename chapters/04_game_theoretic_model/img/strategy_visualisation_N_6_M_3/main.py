import ambulance_game as abg

num_of_servers = 1
system_capacity = 6
buffer_capacity = 3

for threshold in range(1, system_capacity + 1):
    latex_code = abg.markov.tikz.generate_code_for_tikz_figure(
        num_of_servers=num_of_servers,
        threshold=threshold,
        system_capacity=system_capacity,
        buffer_capacity=buffer_capacity,
    )

    with open("main_" + str(threshold) + ".tex", "w") as textfile:
        textfile.write(latex_code)
