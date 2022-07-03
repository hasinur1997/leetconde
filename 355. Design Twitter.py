# Problem Link https://leetcode.com/problems/design-twitter/

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.timestamp = 0

    def post(self, user_id, tweet_id):
        if user_id in self.tweets:
            self.tweets[user_id].append((self.timestamp, tweet_id))
        else:
            self.tweets[user_id] = [(self.timestamp, tweet_id)]

        self.timestamp += 1

    def get_news_feed(self, user_id):
        tweets = []
        followers = []

        if user_id in self.tweets:
            tweets += self.tweets[user_id]

        for follower in self.followers:
            if user_id in self.followers[follower]:
                followers.append(follower)

        for i in followers:
            if i in self.tweets:
                tweets += self.tweets[i]

        tweets.sort(reverse=True)

        return [tweet_id for timestamp, tweet_id in tweets[:10]]

    def follow(self, follower_id, followee_id):
        if followee_id in self.followers:
            self.followers[followee_id].append(follower_id)
        else:
            self.followers[followee_id] = [follower_id]

    def unfollow(self, follower_id, followee_id):
        if followee_id not in self.followers:
            return

        if follower_id in self.followers[followee_id]:
            self.followers[followee_id].remove(follower_id)





obj = Twitter()
obj.post(1, 5)
obj.follow(1,2)
obj.post(2, 6)

print(obj.get_news_feed(1))

