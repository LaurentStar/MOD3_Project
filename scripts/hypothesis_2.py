formula = 'Carbon_Emissions ~ C(State) * C(Year)' # To be continued
model = ols(formula, df2).fit()
model.summary()
					#table = sm.stats.anova_lm(model, typ=2)
print(table)


# se = df[df['Region'] == 'south_east']['Carbon_Emissions'].to_numpy()
# ne = df[df['Region'] == 'north_east']['Carbon_Emissions'].to_numpy()
# mw = df[df['Region'] == 'mid_west']['Carbon_Emissions'].to_numpy()
# wc = df[df['Region'] == 'west_coast']['Carbon_Emissions'].to_numpy()


# regions = ['se', 'ne', 'mw', 'wc', 'sw']
# nCk_regions = list(combinations(regions, 2))
# hypothesis = []

# for region_pair in nCk_regions:
#     a = region_pair[0]
#     b = region_pair[1]
#     exec(f"hypothesis.append((stats.ttest_ind({a}, {b}), {region_pair}))")