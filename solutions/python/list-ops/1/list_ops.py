def append(list1, list2):
    return list1 + list2

def concat(lists):
    output = []
    for lis in lists:
        output.extend(lis)
    return output


def filter(function, list):
    output = []
    for val in list:
        if function(val) is True:
            output.append(val)
    return output


def length(list):
    counter = 0
    for val in list:
        counter += 1
    return counter


def map(function, list):
    return [function(val) for val in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
