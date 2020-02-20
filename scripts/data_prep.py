_  = os.path.join('data', 'dataframe_pickle')
with open(_, 'rb') as file:
    df = pickle.load(file)
df=df[df['Year'].isin(['2018','2017', '2016', '2015', '2016', '2015', '2014', '2013', '2012', '2011', '2010'])]
df = df.groupby('State').sum()
df['Region'] = df.index.map(lambda x: region_maker(x, _REGIONS)) 
df.sort_values('State', inplace=True)

population_df = load_population_data()
population_df = population_df.iloc[5:, ]
population_df.drop(['Census', 'Estimates Base', 2019], axis=1, inplace=True)
population_df.drop(16, axis=0, inplace=True)
population_df.sort_values('States', inplace=True)
population_df.set_index('States', inplace=True)

df = pd.concat([df, population_df.sum(axis = 1)], sort=False, axis=1)
df.rename(columns={0: "Population_Sum"}, inplace=True)


#Load data for hypothesis 2----------------------------------------------------------
_  = os.path.join('data', 'dataframe_pickle')
with open(_, 'rb') as file:
    df2 = pickle.load(file)
df2=df2[df2['Year'].isin(['2018','2017', '2016', '2015', '2016', '2015', '2014', '2013', '2012', '2011', '2010',])]