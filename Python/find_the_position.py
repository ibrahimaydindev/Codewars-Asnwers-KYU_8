import string


def position(alphabet):
    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase

    alphas = alphabetLower + alphabetUpper

    if alphabet in alphas:
        return f"Position of alphabet: {alphas.index(alphabet) + 1}"
