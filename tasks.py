from invoke import task


@task
def compile(c):
    """
    Compile the LaTeX document.
    """
    c.run(f"latexmk -xelatex main.tex")
