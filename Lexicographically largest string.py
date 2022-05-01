"""Given a string S and an integer K, the task is to generate lexicographically the largest string
possible from the given string, by removing characters also,
that consists of at most K consecutive similar characters.

Input: S = “baccc”, K = 2
Output: ccbca

Input: S = “ccbbb”, K = 2
Output: ccbb
"""


def next_available_char(charset, start):
    # Traverse charset from start-1
    for i in range(start - 1,
                   -1, -1):
        if charset[i] > 0:
            charset[i] -= 1
            return chr(i + ord('a'))

    # If no character can be
    # appended
    return '\0'


def largest_string(s, k):
    n = len(s)

    # Stores the frequency of
    # characters
    charset = [0] * 26

    new_string = ""

    for i in s:
        charset[ord(i) -
                ord('a')] += 1

    # Traverse the string
    for i in range(25, -1, -1):
        count = 0

        # Append larger character
        while charset[i] > 0:
            new_string += chr(i + ord('a'))

            # Decrease count in
            # charset
            charset[i] -= 1

            # Increase count
            count += 1

            # Check if count reached
            # to charLimit
            if (charset[i] > 0 and
                    count == k):

                # Find nearest lower char
                next_ = next_available_char(charset, i)

                # If no character can be
                # appended
                if next_ == '\0':
                    return new_string

                # Append nearest lower
                # character
                new_string += next_

                # Reset count for next
                # calculation
                count = 0

    return new_string


# Driver code
if __name__ == "__main__":
    S = "ccbbb"

    K = 2
    print(largest_string(S, K))



