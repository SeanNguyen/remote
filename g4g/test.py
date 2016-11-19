def find_subs(s):
    if not len(s):
        return [s]
    subs = find_subs(s[1:])
    return subs + map(lambda sub: s[0] + sub, subs)


def do(str1, str2):
    subs1 = find_subs(str1)
    subs2 = find_subs(str2)

    common_subs = []
    for sub1 in subs1:
        common_subs += [sub2 for sub2 in subs2 if sub2 == sub1]
    return max_count

number_of_test_cases = int(raw_input())

output_data = []
for i in xrange(number_of_test_cases):
    raw_input()
    str1 = raw_input()
    str2 = raw_input()
    output_data.append(do(str1, str2))

for output in output_data:
    print(output)
