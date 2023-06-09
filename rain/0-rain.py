#!/usr/bin/python3
"""#Amount of water retained after it rains in square units"""


def rain(walls):
    """
    #Amount of water retained after it rains.

    Args:
        walls (list): non-negative integers .

    Returns:
        int: The total number of square units of water retained.

    """

    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Calculate the maximum height to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    water_units = 0
    # Calculate the amount of water retained above each wall
    for i in range(n):
        water_units += min(left_max[i], right_max[i]) - walls[i]

    return #!/usr/bin/python3
"""#Amount of water retained after it rains in square units"""


def rain(walls):
    """
    #Amount of water retained after it rains.

    Args:
        walls (list): non-negative integers .

    Returns:
        int: The total number of square units of water retained.

    """

    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum height to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Calculate the maximum height to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    rain_water = 0
    # Calculate the amount of water retained above each wall
    for i in range(n):
        rain_water += min(left_max[i], right_max[i]) - walls[i]
        
    return rain_water
