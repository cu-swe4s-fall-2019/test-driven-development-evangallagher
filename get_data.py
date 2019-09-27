import sys


def read_stdin_col(col_num):
    """ This function returns an array of the stdin column

    Parameters
    -----------
    col_num : the column of data

    Returns
    --------
    L : a list containing the specified column
    """

    L = []

    # stdin may come from gen_data.sh
    for l in sys.stdin:
        A = l.rstrip().split()
        L.append(float(A[col_num]))
    return L
