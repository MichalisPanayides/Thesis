import pathlib
import re
import subprocess
import sys

from invoke import task
import proselint as plnt

import known


@task
def compile(c):
    """
    Compile the LaTeX document.
    """
    c.run(f"latexmk -xelatex main.tex")


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
    Check the spelling of all .tex files
    """

    def remove_expected_errors(errors):
        """
        Remove general errors that were expected from the error list
        """
        expected_errors = [
            "annotations.misc",
            "typography.symbols.ellipsis",
            "typography.symbols.sentence_spacing",
        ]
        updated_errors = []
        for error in errors:
            if error[0] not in expected_errors:
                updated_errors.append(error)
        return updated_errors

    def remove_specific_errors(errors):
        """
        Remove some very specific errors that are expected. The specific errors
        are stored in a way such that:
            specific_errors[i] = (error_name, error_line)

        Known errors: 
            - spelling consistency on line 53 for centre/center
            - not using curly quotes in code block (for docstring)
        """
        specific_errors = [
            ("consistency.spelling", 54),
            ("typography.symbols.curly_quotes", 79),
        ]
        updated_errors = []
        for error in errors:
            if (error[0], error[2]) not in specific_errors:
                updated_errors.append(error)
        return updated_errors

    def exclude_tex_files_for_imgs(file_paths):
        """
        Remove files that contain images (mainly tikz) from the list of files
        to run proselint on
        """
        updated_files = []
        for file_path in file_paths:
            if "img" not in str(file_path):
                updated_files.append(file_path)
        return updated_files

    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    all_tex_files_without_imgs = exclude_tex_files_for_imgs(all_tex_files)
    exit_codes = [0]
    for path in all_tex_files_without_imgs:
        with open(path, "r") as f:
            text = "\n\n" + f.read()
            errors = plnt.tools.lint(text)
        errors = remove_expected_errors(errors)
        errors = remove_specific_errors(errors)
        if errors:
            print(f"In {path} the following errors were found: ")
            for error in errors:
                print(error)
            exit_codes.append(1)
    sys.exit(max(exit_codes))


@task
def alex(c):
    """
    Check for inconsiderate and insensitive writing of all .tex files
    """
    exception_files = ["packages.tex"]
    all_tex_files = list(pathlib.Path().glob("**/*.tex"))
    for file in all_tex_files:
        if str(file) not in exception_files:
            c.run(f"alex {file}")

