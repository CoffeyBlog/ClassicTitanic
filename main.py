
#%%
from pathlib import Path
from matplotlib import pyplot as plt

import pandas as pd
import seaborn as sns

titanic_df = pd.read_csv(Path().joinpath('data', 'titanic.csv'))

sns.countplot(x='Survived',
              hue='Sex',
              data=titanic_df)
plt.show()

sns.countplot(x='Survived',
              hue='Pclass',
              data=titanic_df)
plt.show()


# Show me a sample of 10 rows
sample_titanic = titanic_df.sample(10)
print(sample_titanic)
