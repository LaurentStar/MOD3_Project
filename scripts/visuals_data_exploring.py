fig, ax = plt.subplots(ncols=1, nrows=2,figsize=(10, 15))
sns.distplot(a=df['Carbon_Emissions'], 
             ax=ax[0]).set_title('CO2_Emissions Distribution (million metric tons');#.figure.savefig("carbon_emissions_distrubtion.png")

sns.barplot(x="Carbon_Emissions", 
            y=df.sort_values(by=['Carbon_Emissions'], ascending=False).index, 
            data=df.sort_values(by=['Carbon_Emissions'], ascending=False),
            label="Total",
            ax=ax[1],
            color = 'r').set_title('CO2_Emissions by state (million metric tons)' );#.figure.savefig("carbon_emissions_by_state.png");
plt.tight_layout()