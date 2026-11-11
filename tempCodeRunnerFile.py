 if not stock_data: #inside a class start here
#             print("No stock records found")
#         else:
#             print("\nCurrent Stock Levels:")
#             for id, info in stock_data.items():
#                 status = "Normal"
#                 if info["quantity"] <= info["reorder_level"]:
#                     status = "Low Stock"
#                 print("ID:", id, "| Name:", info["name"], "| Qty:", info["quantity"], "| Status:", status) #stop here