def quarter_of(month):
    quarter1 = [1, 2, 3]
    quarter2 = [4, 5, 6]
    quarter3 = [7, 8, 9]
    quarter4 = [10, 11, 12]

    return (
        1
        if month in quarter1
        else 2
        if month in quarter2
        else 3
        if month in quarter3
        else 4
    )
