# (*
# Q2-8: 20 points

# Recall the 'foreach' function and the 'get_at' function.
# For instance, list_foreach(xs)(work) applies 'work' to
# each element in the given list 'xs'; list_get_at(xs)(i)
# returns the element at position 'i' in 'xs' if 'i' is a
# valid index; otherwise the Subscript exception is raised.

# Please implement in *Python* a function 'foreach_to_get_at'
# that turns a 'foreach' function into a 'get_at' function.

# (*
# Following is the type for 'foreach_to_get_at' in ocaml:
# fun foreach_to_get_at
#   (foreach: ('xs, 'x0) foreach): ('xs -> int -> 'x0) = ...
# *)

#
# *)

def foreach_to_get_at(foreach):# your implementation below
  def get_at(xs, i):
    result = None
    found = False

    def work(element):
      nonlocal found, result, i
      if not found:
        if i == 0:
          result = element
          found = True
        else:
          i -= 1
    foreach(xs, work)
    if not found:
      raise IndexError
    return result
  return get_at
