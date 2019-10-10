import simulations
import numpy as np
import csvParser
import graphing


class SingleIteration:
    index = None
    data_points = None
    p = None
    simulate_index = None
    real_streak_counts = None
    average_streaks = None

    def __init__(self, set_index):
        self.index = set_index
        self.p = float(csvParser.important_values_dict[self.index]['p value'])
        print(self.p)
        self.data_points = int(csvParser.important_values_dict[self.index]['number of data points'])
        print(self.data_points)
        self.simulate_index = simulations.MultipleSimulations(100, self.data_points, self.p)
        self.real_streak_counts = count_streaks(csvParser.streak_data_dict[self.index])
        print(self.real_streak_counts)

    def iterate(self):
        self.simulate_index.simulate()
        self.average_streaks = self.simulate_index.averagestreaks()
        graphing.dual_bar_chart(self.index, self.real_streak_counts, self.average_streaks)


def count_streaks(streak_list):
    counted_streaks = [1]
    current_streak = 1
    for i in range(1, len(streak_list)):
        if current_streak > int(streak_list[i]):
            if current_streak > len(counted_streaks):
                for j in range(len(counted_streaks), current_streak):
                    if j == current_streak - 1:
                        counted_streaks.append(1)
                    else:
                        counted_streaks.append(0)
            else:
                counted_streaks[current_streak - 1] += 1
        current_streak = int(streak_list[i])
    return counted_streaks

def iterate_indicies(symbols):
    for index in symbols:
        SingleIteration(index).iterate()


def main():
    iterate_indicies(csvParser.streak_data_indicies)

main()