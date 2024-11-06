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


print(increment_string("foo") == "foo1", increment_string("foo"), "foo1")
print(increment_string("foobar001") == "foobar002", increment_string("foobar001"), "foobar002")
print(increment_string("foobar1") == "foobar2", increment_string("foobar1"), "foobar2")
print(increment_string("foobar00") == "foobar01", increment_string("foobar00"), "foobar01")
print(increment_string("foobar99") == "foobar100", increment_string("foobar99"), "foobar100")
print(increment_string("foobar099") == "foobar100", increment_string("foobar099"), "foobar100")
print(increment_string("fo99obar99") == "fo99obar100", increment_string("fo99obar99"), "fo99obar100")
print(increment_string("") == "1", increment_string(""), "1")
