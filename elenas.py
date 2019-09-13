import pandas as pd

def read_csv_file(file):
    return pd.read_csv(file)

def calculate_ambassador_comission(DataFrame):
    return DataFrame["seller_commission_percent"] * DataFrame["price"]

def calculate_elenas_commission(DataFrame):
    return DataFrame["price"] * 0.12

def ambassadors(DataFrame):
    ambassadors_rows = DataFrame.loc[ : ,["seller_id", "total_commission"]]
    return ambassadors_rows.groupby(["seller_id"]).sum().reset_index()

def calculate_brand_revenue(DataFrame):
    brand_revenue_substractors = DataFrame["total_commission"] + DataFrame["elenas_commission"] + DataFrame["logistic_cost"]
    return DataFrame["price"] - brand_revenue_substractors

def brands(DataFrame):
    return DataFrame.groupby(["brand_name"])["total_revenue"].agg(total_commission='sum').reset_index()


# this function assigns the DataFrame values calling the related functions
def assign_values_to_DataFrame(DataFrame):
    DataFrame["total_commission"] = calculate_ambassador_comission(DataFrame)
    DataFrame["elenas_commission"] = calculate_elenas_commission(DataFrame)
    DataFrame["total_revenue"] = calculate_brand_revenue(DataFrame)
    return DataFrame

def generate_csv_files(DataFrame):
    ambassadors(DataFrame).to_csv('ambassadors.csv', index = False)
    brands(DataFrame).to_csv('brands.csv', index = False)


DataFrame = assign_values_to_DataFrame(read_csv_file("orders.csv"))
generate_csv_files(DataFrame)
