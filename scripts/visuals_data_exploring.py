fig, ax = plt.subplots(ncols=1, nrows=4,figsize=(10, 25))
sns.distplot(a=df['Carbon_Emissions'], 
             ax=ax[0]).set_title('CO2_Emissions Distribution (million metric tons');#.figure.savefig("carbon_emissions_distrubtion.png")

sns.barplot(x="Carbon_Emissions", 
            y=df.sort_values(by=['Carbon_Emissions'], ascending=False).index, 
            data=df.sort_values(by=['Carbon_Emissions'], ascending=False),
            label="Total",
            ax=ax[1],
            color = 'r').set_title('CO2_Emissions by state (million metric tons)' );#.figure.savefig("carbon_emissions_by_state.png");


sns.barplot(x="Carbon_Emissions", 
            y=df.sort_values(by=['Carbon_Emissions'], ascending=False).Region, 
            data=df.sort_values(by=['Carbon_Emissions'], ascending=False),
            label="Total",
            ax=ax[2],
            color = 'g').set_title('CO2_Emissions by region (million metric tons)' );#.figure.savefig("carbon_emissions_by_region.png");


_  = os.path.join('images', 'us_regdiv.png')
pil_im = Image.open(_) 
im_array = np.asarray(pil_im)
ax[3].imshow(im_array)

plt.tight_layout()
