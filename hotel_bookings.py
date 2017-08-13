def hotel(arrivals, departures, capacity):
    n_bookings = len(arrivals)
    assert n_bookings == len(departures)

    arrivals = sorted(arrivals)
    departures = sorted(departures)

    occupancy = 0
    arr_index = 0
    dep_index = 0
    while arr_index < n_bookings and dep_index < n_bookings:
        arr = arrivals[arr_index]
        dep = departures[dep_index]
        if arr < dep:
            occupancy += 1
            if occupancy > capacity:
                return False
            arr_index += 1
        else:  # dep <= arr
            occupancy -= 1
            dep_index += 1
    return True

assert hotel([1, 3, 5], [2, 6, 8], 1) == False