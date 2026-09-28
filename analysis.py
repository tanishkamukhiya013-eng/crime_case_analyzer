def get_priority(evidence):
    if evidence >= 3:
        return "High"
    elif evidence == 2:
        return "Medium"
    else:
        return "Low"