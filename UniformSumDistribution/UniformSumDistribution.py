import numpy as np
import scipy.stats as stats
from scipy.stats import rv_continuous
from scipy.special import comb

class UniformSumDistribution(rv_continuous):
    "The Irwin-Hall distribution, named for Joseph Irwin and Phillip Hall, \
    is the distribution that governs the sum of independent random variables, \
    each with the standard uniform distribution. It is also known as the uniform sum distribution."

    def __init__(self, n, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.n = n

    def _pdf(self, x):
        n = self.n
        y = []
        if type(x) == int:
            x = [x]
        for x in x:
            y.append(np.sum([(-1) ** k * (-k + x) ** (n - 1) * comb(n, k) for k in
                             range(0, int(np.floor(x)) + 1)]) / np.math.factorial(n - 1))
        return y

    def _cdf(self, x):
        n = self.n
        y = []
        if type(x) == int:
            x = [x]
        for x in x:
            y.append(np.sum(
                [(-1) ** k * (-k + x) ** n * comb(n, k) for k in range(0, int(np.floor(x)) + 1)]) / np.math.factorial(
                n))
        return y

    def _stats(self):
        mean = self.n / 2
        variance = self.n / 12
        skew = 0
        kurtosis = -6 / (5 * self.n)
        return mean, variance, skew, kurtosis

    def _sf(self, x):
        y = []
        if type(x) == int:
            x = [x]
        for x in x:
            y.append(1.0 - self._cdf(x)[0])
        return y