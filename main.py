import pandas as pd
import numpy as np
i = pd.Index(["AbC", "de", "FGHI", "j", "kLm"])
other = (
    np.array(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            np.array(["f", "g", "h", "i", "j"]),
            np.array(["f", "a", "b", "f", "a"]),
            np.array(["f", "a", "b", "f", "a"]),
            np.array(["1", "2", "3", "4", "5"]),
            np.array(["f", "a", "b", "f", "a"]),
    np.array(["f", "g", "h", "i", "j"]),
)
print(i.str.cat(other))
x =  np.array(["f", "g", "h", "i", "j"])
print(i.str.cat(x))