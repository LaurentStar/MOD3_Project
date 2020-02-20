_  = os.path.join('data', 'dataframe_pickle')
with open(_, 'rb') as file:
    df = pickle.load(file)
df = df.groupby('State').sum()
df['Region'] = df.index.map(lambda x: region_maker(x, _REGIONS)) 

population_df = load_population_data()