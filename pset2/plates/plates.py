def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def ends_with_nums(s):
    non_num_index = 0
    s.reverse()
    for c in s:
        if c.isLetter:
            break
        non_num_index+=1
    s.reverse()
    s = s[:non_num_index]
    print(s)
        
        

def is_valid(s):
    """
    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”
    """
    if 
        s.isalnum()
        and s[0].isalnum()
        and s[1].isalnum()
        and len(s) == 6
        and ends_with_nums(s)
        :
        pass
    pass


main()
