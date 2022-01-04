"""
Time Complexity: O(n)
"""


def tweet_fun(test_cases):
    if test_cases < 1:
        print("Enter number greater than 1 for test cases")
    for i in range(test_cases):
        n_tweets = int(input())  # Input number of Tweets
        if n_tweets < 1:
            print("Enter number greater than 1 for no. of tweets")
        twee_dic = {}
        for j in range(n_tweets):
            tweet = input()  # Enter Tweets-> user name and tweet id separated by a space

            # Splitting the Tweet by space as we want to count the maximum frequency of a particular tweets
            tweet_split = tweet.split(" ")
            twee_dic[tweet_split[0]] = twee_dic.get(tweet_split[0], 0) + 1

        # Use of pre-defined function "sorted" to sort the dictionary on the basis of max count i.e decreasing order by value
        tweet_list = sorted(twee_dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        temp_dic = {}
        flag = False
        for k in range(1, len(tweet_list)):
            temp_dic[tweet_list[k - 1][0]] = tweet_list[k - 1][1]
            if tweet_list[k][1] == tweet_list[k - 1][1]:
                temp_dic[tweet_list[k][0]] = tweet_list[k][1]
            else:
                if k == 0:
                    print(tweet_list[k - 1][0], tweet_list[k - 1][1])
                    flag = True
                    break
                else:
                    break
        x = sorted(temp_dic.items())
        if not flag:
            for j in x:
                print(j[0], j[1])


test_cases = int(input())  # Input number of Test Cases
tweet_fun(test_cases)
