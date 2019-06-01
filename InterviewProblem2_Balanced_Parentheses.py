
def get_balanced(s):
    open_count = 0
    closed_count = 0
    max_balanced = 0
    found_open = 0
    found_closed = 0

    for i in range(len(s)):
        if s[i] == '(':
            found_open = 1
            open_count += 1

        if found_open and s[i] == ')':
            found_closed = 1
            closed_count += 1

        if found_closed:
            temp = min(closed_count, open_count)*2
            if temp >= max_balanced:
                max_balanced = temp
            if i+1 <= len(s)-1:
                if s[i] != s[i+1]:
                    found_closed = 0
                    found_open = 0
                    open_count =0
                    closed_count=0
    return max_balanced
