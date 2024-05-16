def process(matrix):
    # Initializing variables to store Mario's and Princess's positions.
    m = [0, 0]
    p = [0, 0]
    # matrix to find Mario and Princess.
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 'm':  
                m = [i, j]
            elif col == 'p': 
                p = [i, j]

    # Initializing list to store the moves taken by Mario to rescue the Princess.
    moves = []

    # Loop until Mario reaches the Princess.
    while True:
        # Check Mario's position relative to Princess's position
        # adding appropriate move to the list.
        if m[0] - p[0] < 0:
            moves.append("DOWN")
            m[0] += 1
        elif m[0] - p[0] > 0:
            moves.append("UP")
            m[0] -= 1
        if m[1] - p[1] > 0:
            moves.append("LEFT")
            m[1] -= 1
        elif m[1] - p[1] < 0:
            moves.append("RIGHT")
            m[1] += 1
        # If Mario reaches the princcess location then exit the loop
        if m == p:
            break
    # Return the list of moves taken by Mario to rescue the Princess
    return moves


matrix = ["---", "-m-", "p--"]

rescue = process(matrix)
print("Mario has successfully rescue princess:")
print(rescue)
