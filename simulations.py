import random
import time


class MultipleSimulations:
    k = None
    n = None
    p = None
    totalstreaklist = None
    largeststreaklist = None

    def __init__(self, setk, setn, setp):
        self.k = setk
        self.n = setn
        self.p = setp
        self.totalstreaklist = []
        self.largeststreaklist = []

    def simulate(self):
        for l in range(self.k):
            trial = UpDown(self.p)
            trial.onetrial(self.n)
            self.largeststreaklist.append(trial.largeststreak)
            self.addnewstreaks(trial.streakCount, self.totalstreaklist)

    def addnewstreaks(self, newstreak, streaklist):
        if len(newstreak) > len(streaklist):
            for j in range(len(streaklist)):
                streaklist[j] += newstreak[j]
            for j in range(len(streaklist), len(newstreak)):
                streaklist.append(newstreak[j])
        else:
            for j in range(len(newstreak)):
                streaklist[j] += newstreak[j]

    def largeststreak(self):
        return len(self.totalstreaklist)

    def averagestreaks(self):
        returnaverage = []
        for i in range(len(self.totalstreaklist)):
            streakAverage = self.totalstreaklist[i] / self.k
            # print(streakAverage)
            returnaverage.append(streakAverage)
        return returnaverage


class UpDown:
    change = None
    largeststreak = None
    probability = None
    streakCount = None # first index represents the count of 1

    def __init__(self, p):
        self.largeststreak = 0
        self.probability = p
        self.change = []
        self.streakCount = []

    # runs one trial of coin flips recording data in the lists of this individual class
    def onetrial(self, n):
        currentstreak = 0
        recentflip = None
        for i in range(n):
            # down logic
            if random.random() > self.probability:
                self.change.append(-1)  # tracks that it was down at the current index in the up array
                if i == 0:
                    currentstreak += 1
                elif recentflip == -1:
                    currentstreak += 1
                    # in case the streak doesn't get cut off before the end
                    if i == n - 1:
                        self.countstreak(currentstreak, self.streakCount)
                else:
                    self.countstreak(currentstreak, self.streakCount)
                    currentstreak = 1
                recentflip = -1

                if currentstreak > self.largeststreak:
                    self.largeststreak = currentstreak
            # up logic
            else:
                self.change.append(1)
                if i == 0:
                    currentstreak += 1
                elif recentflip == 1:
                    currentstreak += 1
                    # in case the streak doesn't get cut off before the end
                    if i == n - 1:
                        self.countstreak(currentstreak, self.streakCount)
                else:
                    self.countstreak(currentstreak, self.streakCount)
                    currentstreak = 1
                recentflip = 1

                if currentstreak > self.largeststreak:
                    self.largeststreak = currentstreak

    # records the end of the streak in the streakCount array
    # appends the list if it hasn't reached the streak length yet until the length of the largest streak
    def countstreak(self, newstreak, streaklist):
        if newstreak > len(streaklist):
            for x in range(len(streaklist), newstreak):
                if x == newstreak - 1:
                    streaklist.append(1)
                else:
                    streaklist.append(0)
        else:
            streaklist[newstreak - 1] += 1 # increases the counter by 1


def main():
    test = MultipleSimulations(100, 100, 0.6)
    test.simulate()
    print(test.largeststreak())
    print(test.largeststreaklist)
    print(test.totalstreaklist)
    print(test.averagestreaks())



start_time = time.time()
main()
end_time = time.time()
print (end_time - start_time, "seconds")
