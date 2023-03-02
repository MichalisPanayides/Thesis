# Workforce Behaviours In Healthcare Systems

This repository contains the source files to compile the thesis titled
"Workforce Behaviours In Healthcare Systems" submitted in partial fulfilment of
the requirements for the degree of Doctor of Philosophy at Cardiff University.

## Clone the repository

To clone the repository run the following command in the terminal:

```bash
$ git clone https://github.com/MichalisPanayides/Thesis.git
```

## Create the virtual environment

All code for the research and testing of this thesis is written in `Python` and
the libraries used are specified in `environment.yml`.
To create and activate the environment run the following commands in the
terminal:

```bash
$ conda env create -f environment.yml
$ conda activate thesis
```

## Compiling the thesis document

To compile the `.pdf` of this thesis run the following command in the terminal:

```bash
$ inv compile
```

## Doctests

All code presented in this thesis is tested and verified using `doctests`. To
run the doctests run the following command in the terminal:

```bash
$ inv doctest
```

## Spell checking

To run the spellchecker the thesis run the following command in the terminal
to check the spelling of the thesis:

```bash
$ sudo apt-get install aspell
$ inv spellcheck
```

Note that `aspell` is currently only available for Linux and Mac OS X.

## Proselint

`Proselint` is a linter for prose. It checks the text for stylistic errors,
consistency issues, and common grammar mistakes.
To run the `proselint` checker run the following command in the terminal:

```bash
$ inv proselint
```

## Alex

To install and run the `alex` checker for insensitive and inconsiderate writing
run the following command in the terminal:

```bash
$ npm install alex --global
$ inv alex
```
