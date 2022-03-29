global total_seats
global remaining

# Read input file and return array of requests
def read_file(file_name):
    request_array = []
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            request_array.append(line.split())
    return request_array

# Write result to Output file
def write_file(file_name, content):
    with open(file_name, 'w+') as f:
        if isinstance(content, str):
            f.write(content)
            f.write('\n')
        elif isinstance(content, list):
            for line in content:
                f.write(line)
                f.write('\n')
        else:
            pass

# Map seat row with row alphabet
def seat_map(number):
    map = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J"
    }
    return map[number]

# Validate input request
def reserve_seats(filename, output_file, rows, cols):
    reservations_reqs, result = read_file(filename), []
    global total_seats
    global remaining
    total_seats = rows * cols
    remaining = [cols] * rows
    for request in reservations_reqs:
        if len(request) == 2:
            request_number, requested_seats = request[0], request[1]
            # request to check available seats
            if requested_seats == 'A':
                out = request_number + " Available seats are: " + str(total_seats)
            # if requested seats are greater than total seats in Theater
            elif int(requested_seats) > (cols * rows):
                out = request_number + f" Current Request is invalid. Requested seats should be at most {cols*rows}."
            # if requested seats are less than 1
            elif int(requested_seats) <= 0:
                out = request_number + " Current Request is invalid. Requested Seats should at least be 1."
            else:
                out = request_number + " " + assign(int(requested_seats),rows,cols, 1)
            result.append(out)
        else:
            raise Exception("Invalid request. Request should be in form R### #.")
    write_file(output_file, result)
    return output_file

# assign seats for the request
def assign(req_seats, rows, cols, safe_row):
    global remaining
    global total_seats
    row = rows // 2 - 1
    down = False
    counter = safe_row
    res = ''
    buffer = 3

    # if requested seats are more than available seats
    if req_seats > total_seats:
        res = f"Remaining Seats are less than Requested Seats ({req_seats}). Max Seats Available {total_seats}."
        return res

    # if requested seats are available in single row
    while 0 <= row < rows:
        if req_seats <= remaining[row]:
            x = cols - remaining[row] + 1
            for i in range(x, x + req_seats):
                res += seat_map(row) + str(i) + ','
            seats = min(req_seats + buffer, remaining[row])
            remaining[row] -= seats
            total_seats -= seats
            return res

        if not down:
            row += counter
            counter += safe_row
            down = True
        else:
            row -= counter
            counter += safe_row
            down = False

    # if requested seats are not available in single row
    row = rows // 2 - 1
    counter = safe_row

    while req_seats > 0:
        if remaining[row] > 0:
            start = cols - remaining[row] + 1
            for i in range(start, cols + 1):
                if req_seats > 0:
                    res += seat_map(row) + str(i) + ','
                    req_seats -= 1
                    remaining[row] -= 1
                    total_seats -= 1
        if remaining[row] != 0:
            total_seats -= min(remaining[row], buffer)
            remaining[row] -= min(remaining[row], buffer)

        if not down:
            row += counter
            counter += safe_row
            down = True
        else:
            row -= counter
            counter += safe_row
            down = False
    return res
