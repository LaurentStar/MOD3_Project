def region_maker(state, regions):
	"""
	When given a state of the United States,
	this function return the region it belong to 
	if given a region to check.
	
	Parameters
    ----------
		state : string of state name EG:('Texas').
		
        regions : A dictionary of regions for a country. 
			the regions values are list of string for the states).
			
	Returns
	-------
	region name for state
	"""
	for region in regions:
		if state in regions[region]:
			return region
			
def load_data_by_api(): 
	"""
	Loads carbon emission data from eia api for all states
	for the past 30 years. It saves this the dataframe as 
	a pickle object in the same directory as the python
	script
	
	Returns
	-------
	pandas data frame
	"""
	url =  "https://api.eia.gov/series" 

	PARMS = {'api_key': api_key,
             'series_id': 'EMISS.CO2-TOTV-TT-TO-DC.A' 
            }

	data = []

    #Initialize an empty dataframe to begin
	df = pd.DataFrame()

    # Call the api multiple times for each state
	for state in _STATES.values():

        # Reconstruct the series_id string to reflect the state
		PARMS['series_id'] = PARMS['series_id'][:21] + state + '.A'  
		response = requests.get(url, params=PARMS)
		data.append(response)


    # Iterate through all the responses saved in the list called 'data'
	for tmp in data:

        #Save the dataframe to a temporary spot called '_'
		_ = pd.DataFrame(tmp.json()['series'][0]['data'], columns = ['Year', 'Carbon_Emissions'])

        # Create a third column called 'State' and set the defualt value to the name of the state                 
		_['State'] = tmp.json()['series'][0]['name'].split(', ')[2]

        #update our main dataframe with additional rows
		df = pd.concat([df, _]) 

    # Pickle the data for safe keeping
	_ = os.path.join('data', 'dataframe_pickle')
	with open(_, 'ab') as file:
		pickle.dump(df, file)
    
	return df

	
def load_population_data(): 
	"""
	Loads population excel file and convert it to a data frame.
	Save a pickled data frame in the data folder
	Returns
	-------
	pandas cleaned population data frame
	"""

	_ = os.path.join('data', 'nst-est2019-01.xlsx')
	population_df = pd.read_excel(_)
	population_df.columns = population_df.iloc[2]
	population_df.rename(columns = {np.nan: 'States',         
									'Census': 'Census', 
									'Estimates Base': 'Estimates Base',             
									2010 : 2010,
									2011.0 : 2011,
									2012.0 : 2012,
									2013.0 : 2013,
									2014.0 : 2014,
									2015.0 : 2015,           
									2016.0 : 2016,           
									2017.0 : 2017,           
									2018.0 : 2018,
									2019.0 : 2019 
								   }, 
						 inplace=True)

	population_df.drop(range(3), inplace=True)

	population_df.drop(list(range(59, 66)), inplace=True)

	population_df['States'] = population_df['States'].map(lambda x: x.replace('.', ''))


	_ = os.path.join('data', 'population_dataframe_pickle')
	with open(_, 'ab') as file:
		pickle.dump(df, file)
    
	return population_df
	