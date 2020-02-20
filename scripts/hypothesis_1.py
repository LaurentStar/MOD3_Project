_ = df['Population_Sum'].sum()
expected_frequency = []
expected_frequency.append(np.round(df[df['Region']=='south']['Population_Sum'].sum()/_, 3)) 
expected_frequency.append(np.round(df[df['Region']=='west']['Population_Sum'].sum()/_, 3))
expected_frequency.append(np.round(df[df['Region']=='mid_west']['Population_Sum'].sum()/_, 3))
expected_frequency.append(np.round(df[df['Region']=='north_east']['Population_Sum'].sum()/_, 3))

_ = df['Carbon_Emissions'].sum()
observed_frequency = []
observed_frequency.append(np.round(df[df['Region']=='south']['Carbon_Emissions'].sum()/_, 3)) 
observed_frequency.append(np.round(df[df['Region']=='west']['Carbon_Emissions'].sum()/_, 3))
observed_frequency.append(np.round(df[df['Region']=='mid_west']['Carbon_Emissions'].sum()/_, 3))
observed_frequency.append(np.round(df[df['Region']=='north_east']['Carbon_Emissions'].sum()/_, 3))

chi = stats.chisquare(f_obs=observed_frequency, f_exp=expected_frequency)
print(chi)