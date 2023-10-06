(* ************************************************ *)

(*
Q2-6: 10 points

The function list_reverse return the reverse of a given list.
Please give an implementation of list_reverse based on list_foldright
(not list_foldleft).
*)

(* ************************************************ *)

let list_reverse(xs: 'a list): 'a list = 
  let append_to_end x acc_fn = fun lst -> acc_fn (x :: lst)in
    let final_fn = list_foldright
append_to_end xs(fun x -> x) in
  final_fn[]
;;
