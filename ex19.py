def party_plan(no_of_cake_pieces, no_of_plates):
  print(f"No. of Plates: {no_of_plates}")
  print(f"No. of Plates: {no_of_cake_pieces}")

print("1. Function can be called directly with Values")
party_plan(30, 25)

l_no_of_cakes = 28
l_no_of_plates = 30
print("2. Function can be called directly with Variables")
party_plan(l_no_of_cakes, l_no_of_plates)

print("3. Function can be called with arithmetic or logical expressions")
party_plan((15+15), (25+15))

print("4. Combining Variables with arithmetic expressions in Function call")
party_plan((l_no_of_cakes+10), (l_no_of_plates+5))
