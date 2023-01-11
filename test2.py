import re

def remove_dup(string):
    str_length = len(string)
    result =re.sub(r'([A-B])\1+', r'\1', string)
    res_length = len(result)
    return str_length - res_length


print(remove_dup('AABAAB'))