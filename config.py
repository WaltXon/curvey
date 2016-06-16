import copy

inputs={
    'curves': {
            'oil': {
                    'Qi_monthly': 19400,
                    'Qf_monthly': 15,
                    'nominal_decline_annual': .81,
                    'b_factor': 1.0,
                    'Dmin_annual': 0.06,
                    'EUR': 789000,
                    },
            'gas':{
                    'Qi_monthly': 111000,
                    'Qf_monthly': 0,
                    'nominal_decline_annual': .64,
                    'b_factor': 1.0,
                    'Dmin_annual': 0.05,
                    'EUR': 6581000,
                    },
            'ngl':{},
        },
    'taxes':{
            'ad_val': .025,
            'severance': {
                            'oil': 0.046,
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
    'max_life_years': 50,
    'production_delay': 3,
    'start_date': '20160601',
    'standard_days_in_month': 30.4375,
    'standard_days_in_year': 365.25,

}

config=copy.copy(inputs)

for product, record in inputs['curves'].iteritems():
    if record !={}:
        if float(record['b_factor'])==1.0:
            config['curves'][product]['b_factor_adj']=1.001
        elif float(record['b_factor'])==0.0:
            config['curves'][product]['b_factor_adj']=0.001
        else:
            config['curves'][product]['b_factor_adj']=record['b_factor']

        config['curves'][product]['nominal_decline_monthly']=record['nominal_decline_annual']/12.0
        config['curves'][product]['Dmin_monthly']=record['Dmin_annual']/12.0

config['max_life_months']=inputs['max_life_years']*12
config['max_life_days']=inputs['max_life_years']*inputs['standard_days_in_year']
