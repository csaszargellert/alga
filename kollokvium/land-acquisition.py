class ConvexHullOptimization:
    def __init__(self):
        self.slopes = []
        self.intercepts = []
        self.pointer = 0 # Tracks the best line for the previous query

    def is_bad(self, l1, l2, l3):
        """
        Checks if line `l2` is irrelevant between lines `l1` and `l3`.
        """
        # Cross multiplication to avoid precision issues in floating-point division
        return (self.intercepts[l3] - self.intercepts[l1]) * (self.slopes[l1] - self.slopes[l2]) < \
               (self.intercepts[l2] - self.intercepts[l1]) * (self.slopes[l1] - self.slopes[l3])

    def add_line(self, slope, intercept):
        """
        Adds a new line with given slope and intercept.
        """
        self.slopes.append(slope)
        self.intercepts.append(intercept)

        # Remove the second last line if it becomes irrelevant
        while len(self.slopes) >= 3 and self.is_bad(len(self.slopes) - 3, len(self.slopes) - 2, len(self.slopes) - 1):
            self.slopes.pop(-2)
            self.intercepts.pop(-2)

    def query(self, x):
        """
        Returns the minimum y-coordinate for a given x-coordinate by finding the best line.
        """
        # Adjust the pointer if it has gone out of bounds
        if self.pointer >= len(self.slopes):
            self.pointer = len(self.slopes) - 1

        # Move pointer to the right as long as it leads to a better result
        while self.pointer < len(self.slopes) - 1 and \
                self.slopes[self.pointer + 1] * x + self.intercepts[self.pointer + 1] < \
                self.slopes[self.pointer] * x + self.intercepts[self.pointer]:
            self.pointer += 1

        return self.slopes[self.pointer] * x + self.intercepts[self.pointer]


def minimum_cost_land_acquisition(plots):
    # Sort plots by width and filter by height to remove irrelevant plots
    plots.sort()
    filtered = []

    for width, height in plots:
        # Remove plots that are completely dominated by the current one
        while filtered and filtered[-1][1] <= height:
            filtered.pop()
        filtered.append((width, height))

    # Initialize Convex Hull Optimization
    cht = ConvexHullOptimization()

    # Add the first rectangle
    cht.add_line(filtered[0][1], 0) # slope = height, intercept = 0
    cost = 0

    # Process remaining rectangles
    for i in range(len(filtered)):
        width, height = filtered[i]
        cost = cht.query(width)
        if i < len(filtered) - 1:
            cht.add_line(filtered[i + 1][1], cost)

    return cost

if __name__ == "__main__":
    import sys

    plots = [tuple(map(int, line.split())) for line in sys.stdin.read().splitlines()[1:]]

    print(minimum_cost_land_acquisition(plots))