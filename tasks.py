import pathlib
import re
import subprocess
import sys
import yaml

from invoke import task
import proselint as plnt

import known


@task
def compile(c):
    """
    Compile the LaTeX document.
    """
    c.run("latexmk -interaction=nonstopmode --xelatex -f -shell-escape main.tex")


@task
def spellcheck(c):
    """
    Check the spelling of all .tex files
    """
    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    exit_codes = [0]
    for path in all_tex_files:
        latex = path.read_text()
        aspell_output = subprocess.check_output(
            ["aspell", "-t", "--list", "--lang=en_GB"], input=latex, text=True
        )
        errors = set(aspell_output.split("\n")) - {""}
        incorrect_words = set()
        for error in errors:
            if not any(
                re.fullmatch(word.lower(), error.lower()) for word in known.words
            ):
                incorrect_words.add(error)

        if len(incorrect_words) > 0:
            print(f"In {path} the following words are not known: ")
            for string in sorted(incorrect_words):
                print(string)
            exit_codes.append(1)
    sys.exit(max(exit_codes))


@task
def proselint(c):
    """
    Check the prose of all .tex files using the proselint tool. The steps that
    this function performs are:
        1. Open the .proselint.yaml file and read in what errors should be
        ignored and what files should be ignored.
        2. Find all .tex files and remove the files that should be ignored.
        3. For each .tex file:
            a. Read in the file
            b. Remove all unnecessary lines that should not be checked
            c. Get the errors from proselint
            d. Remove the errors that were expected
            e. Print the errors
    """

    def remove_expected_errors(path, errors, errors_to_ignore):
        """
        Remove general errors that were expected from the error list
        """
        updated_errors = []
        for error in errors:
            if [error[0], str(path)] not in errors_to_ignore:
                updated_errors.append(error)

        return updated_errors
    
    def remove_unnecessary_lines(text):
        """
        Remove code blocks, equations, tikzpictures and all includegraphics
        commands from the text to be checked by proselint. Also remove the
        command begin{center} and end{center} from the text since it flags
        an error of using inconsistent spelling of centre. Note that the lines
        that are removed are replaced by the same number of empty new lines.
        This is done to keep the line numbers in the error messages correct.
        """
        updated_text = text

        code_block_regex = r"\\begin\{lstlisting\}.*?\\end\{lstlisting\}"
        code_blocks = re.findall(code_block_regex, text, re.DOTALL)
        for code_block in code_blocks:
            updated_text = updated_text.replace(code_block, "\n" * (code_block.count("\n")))

        equation_regex = r"\\begin\{equation\}.*?\\end\{equation\}"
        all_equations = re.findall(equation_regex, text, re.DOTALL)
        for equation in all_equations:
            updated_text = updated_text.replace(equation, "\n" * (equation.count("\n")))

        equation_regex_2 = r"\\begin\{equation\*\}.*?\\end\{equation\*\}"
        all_equations_2 = re.findall(equation_regex_2, text, re.DOTALL)
        for equation in all_equations_2:
            updated_text = updated_text.replace(equation, "\n" * (equation.count("\n")))

        align_regex = r"\\begin\{align\}.*?\\end\{align\}"
        all_aligns = re.findall(align_regex, text, re.DOTALL)
        for align in all_aligns:
            updated_text = updated_text.replace(align, "\n" * (align.count("\n")))

        tikz_regex = r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}"
        all_tikz = re.findall(tikz_regex, text, re.DOTALL)
        for tikz in all_tikz:
            updated_text = updated_text.replace(tikz, "\n" * (tikz.count("\n")))
        
        includegraphics_regex = r"\\includegraphics.*?\}"
        includegraphics = re.findall(includegraphics_regex, text, re.DOTALL)
        for includegraphic in includegraphics:
            updated_text = updated_text.replace(includegraphic, "")

        updated_text = updated_text.replace("\\centering", " ")
        updated_text = updated_text.replace("\\begin{center}", " ")
        updated_text = updated_text.replace("\\end{center}", " ")
        
        return updated_text

    def exclude_tex_files(file_paths, files_to_ignore):
        """
        Remove files that should be ignored from the list of files to be
        checked. These files are specified in the .proselint_config file.
        """
        updated_files = []
        # Return the file_paths that do not contain any of the files_to_ignore

        for file_path in file_paths:
            if not any(
                file_to_ignore in str(file_path)
                for file_to_ignore in files_to_ignore
            ):
                updated_files.append(file_path)
        return updated_files


    with open(".proselint.yaml", 'r') as f:
        config = yaml.safe_load(f)
        
    errors_to_ignore = config["errors_to_ignore"]
    files_to_ignore = config["files_to_ignore"]

    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    all_included_tex_files = exclude_tex_files(all_tex_files, files_to_ignore)

    exit_codes = [0]
    for path in all_included_tex_files:
        with open(path, "r") as f:
            text = "\n" + f.read()
        
        updated_text = remove_unnecessary_lines(text)
        errors = plnt.tools.lint(updated_text)
        errors = remove_expected_errors(path, errors, errors_to_ignore)
        if errors:
            print(f"In {path} the following errors were found: ")
            for error in errors:
                print(error)
            exit_codes.append(1)
        else:
            print(f"No errors found in {path}")
    sys.exit(max(exit_codes))


@task
def alex(c):
    """
    Check for inconsiderate and insensitive writing of all .tex files
    """
    exception_files = ["packages.tex", "Frontmatter\\acknowledgements.tex"]
    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    for file in all_tex_files:
        if str(file) not in exception_files:
            if "Bin" not in str(file):
                c.run(f"alex {file}")


@task
def doctests(c):
    """
    Run doctests
    """
    c.run('python -m pytest --doctest-glob="*.tex"')


@task
def runall(c):
    """
    Run all tasks
    """
    print("Doctests:")
    doctests(c)
    print("\n\nAlex:")
    alex(c)
    print("\n\nProselint:")
    proselint(c)
