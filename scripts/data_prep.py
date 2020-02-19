load_data_by_api()
_  = os.path.join('data', 'dataframe_pickle')
with open(_, 'rb') as file:
    df = pickle.load(file)
	
load_population_data()
_ = os.path.join('data', 'population_dataframe_pickle')
with open(_, 'rb') as file:
    population_df = pickle.load(file)