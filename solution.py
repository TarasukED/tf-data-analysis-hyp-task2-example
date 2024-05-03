import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1742143281 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = ks_2samp(sample1, sample2)
    alpha = 0.04
    return p_value < alpha
