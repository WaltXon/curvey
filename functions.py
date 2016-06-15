from config import config

def get_products():
    products=[]
    for product, params in config['curves'].iteritems():
        if params!={}:
            products.append(product)
        else:
            continue
    return products


def annual_to_monthly_rate(annual_rate):
    return ((1+annual_rate)**(1/12.))-1