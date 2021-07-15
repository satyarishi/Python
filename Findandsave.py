'''def format_address(address_string):
    home_no = 0
    home_address = ' '
    parts = address_string.split()
    for part in parts:
        if part.isdigit():
            home_no = part
        else:
            home_address += part + ' '
    return "house number {} on street named {}".format(home_no, home_address)

print(format_address("123 Main Street"))

print(format_address("1001 1st Ave"))

print(format_address("55 North Center Drive"))
'''

def combine_guests(guests1, guests2):
    combined_dic = guests1
    for key2 in guests2:
        if key2 in guests1:
            pass
        else:
            combined_dic[key2] = guests2[key2]
    return combined_dic

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))