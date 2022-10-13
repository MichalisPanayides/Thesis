import ambulance_game as abg

latex_code = [
    tree
    for tree in abg.markov.tikz.generate_code_for_tikz_spanning_trees_rooted_at_00(
        1, 1, 3, 1
    )
]

for pos, tree in enumerate(latex_code):
    with open("main_" + str(pos) + ".tex", "w") as textfile:
        textfile.write(tree)
