def stairs_in_20(stairs):
    one_year_total = sum([amount for weekday in stairs for amount in weekday])
    twenty_year_estimate = one_year_total * 20
    return twenty_year_estimate
