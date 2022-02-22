def vote(age):
    if 0 < age < 18:
        return "Not Eligible for vote and pension"
    elif 18 <= age < 60:
        return "Eligible for vote only"
    else:
        return "Eligible for vote and pension"


# 0< age and 18>age