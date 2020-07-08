from math import fabs


class User:
    rank = -8
    progress = 0

    def inc_progress(self, activity_rank):
        if activity_rank > 8 or activity_rank < -8:
            raise ValueError
        rank_delta = activity_rank - self.rank
        # print('afab', (activity_rank / fabs(activity_rank))
        #       * (self.rank / fabs(self.rank)))
        if (activity_rank / fabs(activity_rank))\
                * (self.rank / fabs(self.rank)) < 0:
            rank_delta = (rank_delta / fabs(rank_delta))\
                         * (fabs(rank_delta) - 1)
        print(f'Rank delta: {rank_delta}')
        if int(rank_delta) == 0:
            self.progress += 3
        elif int(rank_delta) == -1:
            self.progress += 1
        elif int(rank_delta) >= 1:
            self.progress += int(rank_delta * rank_delta * 10)

        rank_delta = 0
        if self.progress >= 100:
            rank_delta = self.progress // 100

        if int(self.rank) < 0 <= int(self.rank + rank_delta):
            rank_delta += 1
        self.rank += rank_delta
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
        self.progress = self.progress % 100

        return 0


if __name__ == '__main__':
    user = User()

    print(f'user progress: {user.progress}, user.rank: {user.rank}')
    user.inc_progress(-7)
    print(f'user progress: {user.progress}, user.rank: {user.rank}')
    user.inc_progress(-2)
    print(f'user progress: {user.progress}, user.rank: {user.rank}')
    user.inc_progress(2)
    print(f'user progress: {user.progress}, user.rank: {user.rank}')
    user.inc_progress(3)
    print(f'user progress: {user.progress}, user.rank: {user.rank}')
    user.inc_progress(-1)
    print(f'user progress: {user.progress}, user.rank: {user.rank}')