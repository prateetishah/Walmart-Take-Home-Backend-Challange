import sys
import logging
from movieSeating import reserve_seats

if __name__ == "__main__":

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        try:
            reservation_req_file = open(input_file)
        except IOError:
            print("Unable to open input file.")
            sys.exit()
        row, col, safe_row, buffer = 10, 20, 1, 3
        output_file = "output_file_" + input_file
        reserve_seats(input_file, output_file, row, col)
        print(f"Outputfile {output_file} is generated.")
    else:
        print("Please Enter required arguements")
        sys.exit()




