"""
Estimator class computes point estimates, confidence intervals, mean, and variance.

This class is designed for calculating statistics such as mean, variance, and confidence intervals for a stream of data points. It supports both relative and absolute precision, allowing flexibility in precision requirements. The Estimator class is particularly useful for monitoring and analyzing data streams in real-time or batch processing scenarios.

Attributes:
    - conf_pct: Confidence level for computing confidence intervals.
    - epsilon: Precision of the confidence intervals.
    - relative: Flag indicating whether precision is relative or absolute.
    - k: Number of values processed so far.
    - sum: Running sum of values.
    - v: Running value of (k-1) * variance.
    - z: CI normal quantile based on the confidence level.
    - conf_str: String representation of the confidence level.
    - observations: List to store the observed values.

Methods:
    - reset(): Resets the internal state of the estimator.
    - process_next_val(value): Processes the next data point and updates internal statistics.
    - get_variance(): Calculates and returns the variance.
    - get_mean(): Calculates and returns the mean.
    - get_conf_interval(): Calculates and returns the confidence interval.

Example usage:
    estimator = Estimator(conf_pct=95, epsilon=0.01, relative=True)
    estimator.process_next_val(10)
    print(estimator.get_mean())
    print(estimator.get_variance())
    print(estimator.get_conf_interval())
"""

class Estimator:
    """ Computes point estimates and confidence intervals """
    def __init__(self, conf_pct = 95, epsilon = 0.01, relative = True):
        self.epsilon = epsilon # precison of CI
        self.relative = relative # relative or absolute precision
        self.k = 0  # number of values processed so far
        self.sum = 0.0  # running sum of values
        self.v = 0.0  # running value of (k-1)*variance
        self.z = norm.ppf(0.5 + (conf_pct / 200))  # CI normal quantile
        self.conf_str = str(conf_pct) + "%"  # string of form "xx%" for xx% CI
        self.observations = []

    def reset(self):
        self.k = 0
        self.sum = 0
        self.v = 0

    def process_next_val(self, value):
        self.k += 1
        if self.k > 1:
            diff = self.sum - (self.k - 1) * value
            self.v += diff/self.k * diff/(self.k-1)
        self.sum += value

    def get_next_val(self, value):
        self.observations.append(value)
        if not self.regenerative:
          self.observations_squared.append(value ** 2) # added for 1b part III

    def get_variance(self):
        return self.v/(self.k-1) if self.k > 1 else 0

    def get_mean(self):
        return self.sum/self.k if self.k >= 1 else 0

    def get_conf_interval(self):
        hw = self.z * math.sqrt(self.get_variance()/self.k)
        point_est = self.get_mean()
        c_low = point_est - hw
        c_high = point_est + hw
        rstr = "{0} Confidence Interval: [ {1:.4f}, {2:.4f} ]  (hw = {3:.4f})"
        return rstr.format(self.conf_str, c_low, c_high, hw)
