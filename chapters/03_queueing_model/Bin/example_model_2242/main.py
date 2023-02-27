import ambulance_game as abg

latex_code = abg.markov.tikz.generate_code_for_tikz_figure(2, 2, 4, 2)


with open("main.tex", "w") as textfile:
    textfile.write(latex_code)
