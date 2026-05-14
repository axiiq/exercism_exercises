"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*numbers):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
       An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return [*numbers]

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]) The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    fixed_list = []

    first_wagon = each_wagons_id[0]
    second_wagon = each_wagons_id[1]

    for id_w in each_wagons_id:
        if id_w == first_wagon or id_w == second_wagon: continue
        fixed_list.append(id_w)
        if id_w == 1:
            for missing_id in missing_wagons:
                fixed_list.append(missing_id)
    fixed_list.append(first_wagon)
    fixed_list.append(second_wagon)
    return fixed_list

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops = [value for value in kwargs.values()]
    full_route = route
    full_route["stops"] = stops

    return full_route
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended = route

    for key, value in more_route_information.items():
        extended[key] = value
    
    return extended


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[tuple]) The list of rows of wagons.

    Returns:
        list[tuple]: the list of rows of wagons.
    """
    depot = []
    for num in range(3):
        depot.append([])
        for row in wagons_rows:
            depot[num].append(row[num])
    return depot
