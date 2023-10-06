(* ************************************************ *)

(*
Q2-5: 5 points
The function list_last returns the last element of a given
list. Please give a NON-RECURSIVE implementation of list_last
based on pattern matching and list_foldright. If the given list
is empty, raise the Empty exception
*)

(* ************************************************ *)

exception Empty
let list_last(xs: 'a list): 'a = 
  match xs with
    [] -> raise Empty
    _ -> list_foldright(fun x acc_opt -> match acc_opt with
      None -> Some x
      Some_ -> acc_opt)xs None
;;
