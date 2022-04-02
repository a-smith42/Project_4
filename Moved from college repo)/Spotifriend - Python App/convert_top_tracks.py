import pandas as pd
#trackdata = pd.read_csv('C:\Users\Alicia\Desktop\_Year 4\Project_4\Demo_test\top50_songs', index_col=False, delimiter = ',')
trackdata = pd.read_csv('top50_songs.csv', index_col=False, delimiter =',')
trackdata.head()
#if possible separate track name and artist with another delimiter