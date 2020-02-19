def region_maker(state, regions):
    for region in regions:
        if state in regions[region]:
            return region