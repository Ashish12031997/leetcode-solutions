def handle_order(inventory, order):
  """Handles a fractional share order.

  Args:
    inventory: A list of tuples (stock, quantity) representing the current inventory.
    order: A list of lists [stock, action, quantity, price] representing the order.

  Returns:
    The updated inventory.
  """

  stock, action, quantity, price = order

  # Find the stock in the inventory
  stock_index = next((i for i, (s, _) in enumerate(inventory) if s == stock), None)

  if action == "B":  # Buy order
    if stock_index is None:
      inventory.append([stock, quantity])
    else:
      inventory[stock_index][1] += quantity

    # Ensure inventory is less than 1
    while inventory[stock_index][1] >= 1:
      inventory[stock_index][1] -= 1
      # Simulate buying a whole share from the exchange
      # ... (Replace with actual exchange interaction logic)

  elif action == "S":  # Sell order
    if stock_index is None:
      raise ValueError("Insufficient inventory for sell order")
    elif inventory[stock_index][1] < quantity:
      raise ValueError("Insufficient inventory for sell order")
    else:
      inventory[stock_index][1] -= quantity

    # Ensure inventory is less than 1
    while inventory[stock_index][1] >= 1:
      inventory[stock_index][1] -= 1
      # Simulate selling a whole share to the exchange
      # ... (Replace with actual exchange interaction logic)

  return inventory

# Example usage
inventory = [["AAPL", 0.99]]
orders = [["AAPL", "B", 0.42, 100]]

inventory = handle_order(inventory, orders[0])
print(inventory)  # Output: [['AAPL', 0.57]]
