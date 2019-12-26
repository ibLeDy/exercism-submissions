class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        print(self.scores)

    def latest(self):
        scores = self.scores[-1]
        return scores

    def personal_best(self):
        self.scores.sort()
        scores = self.scores[-1]
        return scores

    def personal_top_three(self):
        self.scores.sort(reverse=True)
        scores = self.scores[0:3]
        return scores
