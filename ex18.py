def f_print_none():
  print(f"Input Value : no-arguments-passed")

def f_print_one(arg1):
  print(f"Input Value : {arg1}")

def f_print_two(arg1, arg2):
  print(f"Input Value : {arg1} & {arg2}")

def f_print_many(*args):
  print(f"No. of Input Values : {len(args)}")
  print(f" - args[0] : {args[0]}")
  print(f" - args[1] : {args[1]}")
  print(f" - args[2] : {args[2]}")

f_print_none()
f_print_one("input1-only")
f_print_two("input-1", "input-2")
f_print_many("input-1*", "input-2*", "input-3*")