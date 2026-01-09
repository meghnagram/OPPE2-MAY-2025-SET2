def total_revenue(sales_data):
    return sum(transanction['revenue'] for transanction in sales_data)

def product_wise_total_units_and_revenue(sales_data):
    total_units_revenue = {}
    for sale in sales_data:
        pid = sale['product_id']
        if pid not in total_units_revenue:
            total_units_revenue[pid] = (0,0)
        total_units_revenue[pid] = (
            total_units_revenue[pid][0]+sale['units_sold'], 
            total_units_revenue[pid][1]+sale['revenue']
        )
    return total_units_revenue

def top_selling_product(sales_data):
    total_units_revenue = product_wise_total_units_and_revenue(sales_data)
    return max(
        total_units_revenue,
        key=total_units_revenue.get
    )

def average_product_price(sales_data):
    total_units_revenue = product_wise_total_units_and_revenue(sales_data)

    return {
        pid: round(revenue/units,2)
        for pid, (units,revenue) in total_units_revenue.items()
    }


def analyse_sales_data(sales_data, task):
    
    
        if task == 'total_revenue':
            return total_revenue(sales_data)
        elif task == 'product_wise_total_units_and_revenue':
            return product_wise_total_units_and_revenue(sales_data)
        elif task == 'top_selling_product':
            return top_selling_product(sales_data)
        elif task == 'average_product_price':
            return average_product_price(sales_data)
        else:
            raise ValueError("Invalid task provided.")
    

# #Another Method:

# def analyse_sales_data(sales_data, task):
#     if task=='total_revenue':
#         sum=0
#         for i in sales_data:
#             sum +=i["revenue"]
#         return sum
#     if task=='product_wise_total_units_and_revenue':
#         d={}
#         unit=0
#         rev=0
        
#         for i in sales_data:
#             d[i["product_id"]]=0
#         for i in d.keys():
#             unit=0
#             rev=0
#             for j in sales_data:
#                 if i==j["product_id"]:
#                     unit += j["units_sold"]
#                     rev += j["revenue"]
#             d[i]=(unit,rev)
#         return d
#     if task=='top_selling_product':
#         d=analyse_sales_data(sales_data,'product_wise_total_units_and_revenue')
#         max_id=0
#         max_unit=0
#         max_rev=0
        
#         for k,v in d.items():
#             if v[0]>max_unit:
#                 max_id=k 
#                 max_unit=v[0]
#                 max_rev=v[1]
#             elif v[0]==max_unit:
#                 if v[1]>max_rev:
#                     max_id=k 
#                     max_unit=v[0]
#                     max_rev=v[1]
#         return max_id
#     if task=='average_product_price':
#         d=analyse_sales_data(sales_data,'product_wise_total_units_and_revenue')
#         d2={}
       
#         for k,v in d.items():
#             d2[k]=round(v[1]/v[0],2)
#         return d2
            
#   Sales Data Analysis
# You are provided with sales data represented as a list of dictionaries. Each dictionary contains the following keys:

# product_id (str): The unique identifier for a product.
# units_sold (int): The number of units sold in a transaction.
# revenue (int): The revenue generated from that transaction.
# There will be multiple entries for the same product_id. Implement a function analyse_sales_data(sales_data, task) where task is one of the following strings:

# total_revenue
# Returns the total revenue over all transanctions.
# product_wise_total_units_and_revenue
# Returns a dictionary with product_id as keys and a tuple with (the number of units sold for that product, total revenue generated from that product) as values.
# top_selling_product
# Returns the product_id of the product with the highest number of units sold.
# If there is a tie in units sold, the product with the higher total revenue is returned.
# average_product_price
# Returns a dictionary with product_id as keys and the average price computed as the (total revenue / total units_sold) over all the transanctions for the product rounded to 2 decimal places.
# NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.

# Example

# sales_data = [
#    {"product_id": "P101", "units_sold": 50, "revenue": 400},
#    {"product_id": "P102", "units_sold": 30, "revenue": 900},
#    {"product_id": "P101", "units_sold": 70, "revenue": 600},
#    {"product_id": "P103", "units_sold": 120, "revenue": 600}
# ]
# total_revenue -> 2500
# product_wise_total_units_and_revenue -> {'P101': (120, 1000), 'P102': (30, 900), 'P103': (120, 600)}
# top_selling_product -> 'P101' (P101 and P103 are tied on units, but P101 has higher revenue.)
# average_product_price -> {'P101': 8.33, 'P102': 30, 'P103': 5} (For P101, (400+600)/(50+70))          
            
    

