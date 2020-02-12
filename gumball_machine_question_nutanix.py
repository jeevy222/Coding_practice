machines_dict = {}


def reduce(dictionary, rate):
    for y in dictionary:
        dictionary[y] -= rate


rate = 10


def discarder(days, colors):
    if days < 4:
        return 0.0
    discarded_value = 0.0
    for i in range(days):
        if len(machines_dict) < 3:  # initially filling
            machines_dict[colors[i]] = 1000
            reduce(machines_dict, rate)
        elif colors[i] in machines_dict:  # refilling existing color
            machines_dict[colors[i]] = 1000
            reduce(machines_dict, rate)
        elif colors[i] not in machines_dict:  # replacing a color, trigger a discard
            min_key = min(machines_dict, key=machines_dict.get)
            dollar_value = min(machines_dict.values()) / 100
            discarded_value = discarded_value + dollar_value
            del machines_dict[min_key]
            machines_dict[colors[i]] = 1000
            reduce(machines_dict, rate)
        print(machines_dict)
    # return calculated value
    return "{0:.1f}".format(discarded_value)