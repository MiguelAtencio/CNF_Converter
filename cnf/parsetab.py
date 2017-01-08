
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '34FD917CD7826D0D909390F2A304462B'
    
_lr_action_items = {'Right':([4,5,6,10,11,12,13,],[-2,-6,10,-1,-5,-3,-4,]),'$end':([3,4,5,10,11,12,13,],[0,-2,-6,-1,-5,-3,-4,]),'Left':([0,1,2,7,8,9,],[2,2,2,2,2,2,]),'Inference':([3,4,5,6,10,11,12,13,],[7,-2,-6,7,-1,-5,-3,-4,]),'Not':([0,1,2,7,8,9,],[1,1,1,1,1,1,]),'Predicate':([0,1,2,7,8,9,],[4,4,4,4,4,4,]),'Or':([3,4,5,6,10,11,12,13,],[9,-2,-6,9,-1,9,-3,-4,]),'And':([3,4,5,6,10,11,12,13,],[8,-2,-6,8,-1,8,-3,8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,2,7,8,9,],[3,5,6,11,12,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> Left expression Right','expression',3,'p_expression_group','cnfconverter.py',56),
  ('expression -> Predicate','expression',1,'p_expression_predicate','cnfconverter.py',60),
  ('expression -> expression And expression','expression',3,'p_expression_binop','cnfconverter.py',64),
  ('expression -> expression Or expression','expression',3,'p_expression_binop','cnfconverter.py',65),
  ('expression -> expression Inference expression','expression',3,'p_expression_binop','cnfconverter.py',66),
  ('expression -> Not expression','expression',2,'p_expression_negative','cnfconverter.py',78),
]
