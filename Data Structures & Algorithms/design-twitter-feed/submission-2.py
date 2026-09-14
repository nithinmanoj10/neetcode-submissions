class Twitter:

    def __init__(self):
        self.all_tweets = []                    # (tweetId, userId)
        self.follow_info = defaultdict(set)     # {followerId : followeeId}
        self.tweet_idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.all_tweets.append((self.tweet_idx, tweetId, userId))
        self.tweet_idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follower_tweets = [(-tweet_idx, tweetId) for tweet_idx, tweetId, tweetUserId in self.all_tweets if tweetUserId in self.follow_info[userId] or tweetUserId == userId]

        heapq.heapify(follower_tweets)
        result = []

        while len(follower_tweets) > 0 and len(result) < 10:
            _, tweetId = heapq.heappop(follower_tweets)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_info[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_info[followerId]:
            self.follow_info[followerId].remove(followeeId)
