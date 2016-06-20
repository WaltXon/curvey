import numpy as np
import pandas as pd

from config import config
from volumes import volumes
from pricing import pricing
from functions import annual_to_monthly_rate

vol=volumes()
prices=pricing()

econ=pd.concat([vol, prices], axis=1)
econ['gross_sales_oil']=econ['gross_volume_oil']*econ['price_oil']*config['working_interest']
econ['gross_sales_gas']=econ['gross_volume_gas']*econ['price_gas']*config['working_interest']
econ['gross_sales_ngl']=econ['gross_volume_ngl']*econ['price_ngl']*config['working_interest']
econ['gross_sales_total']=econ['gross_sales_oil']+econ['gross_sales_gas']+econ['gross_sales_ngl']

econ['severance_tax_oil']=econ['gross_sales_oil']*config['taxes']['severance']['oil']*config['working_interest']
econ['severance_tax_gas']=econ['gross_sales_gas']*config['taxes']['severance']['gas']*config['working_interest']
econ['severance_tax_ngl']=econ['gross_sales_ngl']*config['taxes']['severance']['oil']*config['working_interest']
econ['severance_total']=econ['severance_tax_oil']+econ['severance_tax_gas']+econ['severance_tax_ngl']

econ['expenses_fixed']=config['expenses']['fixed']*config['working_interest']
econ['expenses_variable']=(config['expenses']['variable']['oil']*econ['gross_sales_oil']+config['expenses']['variable']['gas']*econ['gross_sales_gas']+config['expenses']['variable']['ngl']*econ['gross_sales_ngl'])*config['working_interest']

econ['expenses_total']=(econ['expenses_variable']+config['expenses']['fixed'])*config['working_interest']

econ['gross_revenue_after_sevtax_and_expenses']=econ['gross_sales_total']-econ['severance_total']-econ['expenses_total']

econ['ad_valorum_tax']=econ['gross_revenue_after_sevtax_and_expenses']*config['taxes']['ad_valorum']

econ['gross_revenue_after_sevtax_and_expenses_and_advaltax']=econ['gross_revenue_after_sevtax_and_expenses']-econ['ad_valorum_tax']

econ['capital']=0.0
econ.ix[0,'capital']=(config['capital']['idc']+config['capital']['icc']+config['capital']['land'])*config['working_interest']

econ['gross_cash_flow']=econ['gross_revenue_after_sevtax_and_expenses_and_advaltax']-econ['capital']
econ['net_nondiscounted_cash_flow']=(econ['gross_revenue_after_sevtax_and_expenses_and_advaltax']*config['net_revenue_interest'])-econ['capital']

econ['cum_net_nondiscounted_cashflow']=econ['net_nondiscounted_cash_flow'].cumsum()
econ['net_discounted_cashflow']=econ['net_nondiscounted_cash_flow']/(1+annual_to_monthly_rate(config['discount_rate_annual']))**econ['standard_time']
econ['cum_net_discounted_cashflow']=econ['net_discounted_cashflow'].cumsum()


econ.to_excel(r'C:\Users\WaltN\Desktop\GitHub\curvey\output\econ.xlsx')


npv=round(np.npv(annual_to_monthly_rate(config['discount_rate_annual']),econ['net_nondiscounted_cash_flow']), 2)
irr=round(np.irr(econ['net_discounted_cashflow']), 2)

print('''
    NPV: ${}
    IRR: {}
    '''.format(npv, irr))