import ambulance_game as abg

latex_code = abg.markov.tikz.generate_code_for_tikz_figure(1, 3, 5, 2)


with open("main.tex", "w") as textfile:
    textfile.write(latex_code)
