# ===============================
# CREATE sales.csv FILE
# ===============================

import pandas as pd

# Creating sample retail sales dataset
data = {
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
                1011,1012,1013,1014,1015],
    "Date": ["2025-01-05","2025-01-12","2025-02-03","2025-02-18","2025-03-02",
             "2025-03-15","2025-04-01","2025-04-12","2025-05-05","2025-05-18",
             "2025-06-02","2025-06-20","2025-07-04","2025-07-19","2025-08-10"],
    "Region": ["East","West","North","South","East",
               "West","North","South","East","West",
               "North","South","East","West","North"],
    "Product": ["Laptop","Phone","Tablet","Monitor","Laptop",
                "Phone","Tablet","Monitor","Laptop","Phone",
                "Tablet","Monitor","Laptop","Phone","Tablet"],
    "Category": ["Electronics","Electronics","Electronics","Accessories","Electronics",
                 "Electronics","Electronics","Accessories","Electronics","Electronics",
                 "Electronics","Accessories","Electronics","Electronics","Electronics"],
    "Quantity": [2,3,1,4,3,2,5,2,4,1,3,2,2,3,4],
    "Price": [50000,20000,30000,15000,50000,20000,30000,15000,50000,20000,
              30000,15000,50000,20000,30000]
}

df = pd.DataFrame(data)

# Save file
file_path = "/Database/LabSession_Day23/sales.csv"
df.to_csv(file_path, index=False)

file_path