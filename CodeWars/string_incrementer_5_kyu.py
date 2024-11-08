"""./string_incrementer_5_kyu.py"""

def increment_string(string: str):
    """Increment a string that represents a number."""
    nums_in_str = ""

    for i in string[::-1]:
        if i.isdigit():
            nums_in_str += i
        else:
            break

    nums_in_str = nums_in_str[::-1]
    len_str = len(string) - len(nums_in_str)

    if nums_in_str == '':
        nums_in_str = '0'

    end_part = str(int(nums_in_str) + 1)

    if len(end_part) != len(nums_in_str):
        end_part = '0' * (len(nums_in_str) - len(end_part)) + end_part

    return "".join(string[:len_str] + end_part)


# Second Solve
# def increment_string(string: str) -> str:
#     # Find the position where the numeric suffix starts
#     num_start = len(string)
#     for i in range(len(string) - 1, -1, -1):
#         if not string[i].isdigit():
#             num_start = i + 1
#             break

#     # Split the string into the prefix and numeric suffix
#     prefix = string[:num_start]
#     num_suffix = string[num_start:]

#     if not num_suffix:  # No numeric suffix found, append '1'
#         return prefix + '1'

#     # Increment the numeric suffix and format with leading zeros if needed
#     incremented_num = str(int(num_suffix) + 1).zfill(len(num_suffix))
#     return prefix + incremented_num


print(increment_string("foo") == "foo1", increment_string("foo"), "foo1")
print(increment_string("foobar001") == "foobar002", increment_string("foobar001"), "foobar002")
print(increment_string("foobar1") == "foobar2", increment_string("foobar1"), "foobar2")
print(increment_string("foobar00") == "foobar01", increment_string("foobar00"), "foobar01")
print(increment_string("foobar99") == "foobar100", increment_string("foobar99"), "foobar100")
print(increment_string("foobar099") == "foobar100", increment_string("foobar099"), "foobar100")
print(increment_string("fo99obar99") == "fo99obar100", increment_string("fo99obar99"), "fo99obar100")
print(increment_string("") == "1", increment_string(""), "1")
