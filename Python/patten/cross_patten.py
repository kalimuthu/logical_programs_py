# Print string of odd length in ‘X’ format
# Difficulty Level : Basic

if __name__ == "__main__":
    input_str = input('Enter the string value : ')
    if input_str:
        len_input_str = len(input_str)
        y = len_input_str -1
        for row in range(0,len_input_str):
            for col in range(0,len_input_str):
                if col == row or col == y:
                    print(input_str[col],end = " "),
                else:
                    print(" ",end = " "),
            y = y -1
            print("")
            