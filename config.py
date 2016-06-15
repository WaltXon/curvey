config={
    'curves': {
            'oil': {
                    'QiPerMonth': 19400,
                    'QfPerMonth': 15,
                    'DiPerYear': .81,
                    'b': 1.0,
                    'Dmin': 6,
                    'EUR': 789000,
                    },
            'gas':{
                    'QiPerMonth': 111000,
                    'QfPerMonth': 0,
                    'DiPerYear': .64,
                    'b': 1.0,
                    'Dmin': 5,
                    'EUR': 6581000,
                    },
            'ngl':{},
        },
    'taxes':{
            'ad_val': .025,
            'severance': {
                            'oil': 0.46,
                            'gas':.075,
                        }

            },
    'expenses': {
            'fixed': 10000,
            'variable': {
                        'oil': .03,
                        'gas':0.0,
            },
    },
    'capital':{
            'idc': 3.5*10**6,
            'icc': 3.0*10**6,
            'land':5.0*10**5,
    },
    'economic_life_max': 50*12,
    'production_delay': 3,
}