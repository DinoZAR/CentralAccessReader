
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "]\xb5B\x13\x88\xf21\rs0m\x07\x81'\xaf\x92"
    
_lr_action_items = {'RIGHTBRACKET':([20,21,22,34,],[27,-18,-19,-17,]),'MULTIEXPR':([7,10,11,12,13,14,15,17,18,19,23,26,27,32,36,],[11,-8,-13,-14,-12,-11,-9,11,-15,-10,11,11,-16,-21,-20,]),'ASSIGNS':([4,5,9,27,],[7,-15,23,-16,]),'MULTINUMBEREDEXPR':([7,10,11,12,13,14,15,17,18,19,23,26,27,32,36,],[12,-8,-13,-14,-12,-11,-9,12,-15,-10,12,12,-16,-21,-20,]),'ANYEXPR':([7,10,11,12,13,14,15,17,18,19,23,26,27,32,36,],[13,-8,-13,-14,-12,-11,-9,13,-15,-10,13,13,-16,-21,-20,]),'OUTPUTS':([10,11,12,13,14,15,16,17,18,19,25,27,29,32,36,],[-8,-13,-14,-12,-11,-9,24,-7,-15,-10,-6,-16,35,-21,-20,]),'LEFTPAREN':([18,],[26,]),'LITERAL':([7,10,11,12,13,14,15,17,18,19,23,26,27,32,36,],[14,-8,-13,-14,-12,-11,-9,14,-15,-10,14,14,-16,-21,-20,]),'RIGHTPAREN':([10,11,12,13,14,15,17,18,19,25,26,27,32,33,36,],[-8,-13,-14,-12,-11,-9,-7,-15,-10,-6,32,-16,-21,36,-20,]),'LEFTBRACKET':([4,5,7,10,11,12,13,14,15,17,18,19,23,26,27,32,36,],[8,-15,8,-8,-13,-14,-12,-11,-9,8,-15,-10,8,8,-16,-21,-20,]),'COMMA':([21,22,],[28,-19,]),'STRING':([24,35,],[30,30,]),'ID':([0,2,7,8,10,11,12,13,14,15,17,18,19,23,26,27,28,30,31,32,36,37,],[5,5,18,22,-8,-13,-14,-12,-11,-9,18,-15,-10,18,18,-16,22,-22,-5,-21,-20,-4,]),'$end':([1,2,3,6,30,31,37,],[0,-3,-1,-2,-22,-5,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'xml':([7,17,23,26,],[10,10,10,10,]),'database':([0,],[1,]),'pattern':([0,2,],[2,2,]),'categValues':([8,28,],[20,34,]),'categValue':([8,28,],[21,21,]),'patterns':([0,2,],[3,6,]),'variable':([0,2,7,17,23,26,],[4,4,15,15,15,15,]),'output':([24,35,],[31,37,]),'expressions':([7,17,23,26,],[16,25,29,33,]),'expression':([7,17,23,26,],[17,17,17,17,]),'categories':([4,7,17,23,26,],[9,19,19,19,19,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> database","S'",1,None,None,None),
  ('database -> patterns','database',1,'p_program','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',74),
  ('patterns -> pattern patterns','patterns',2,'p_patterns','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',80),
  ('patterns -> pattern','patterns',1,'p_patterns','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',81),
  ('pattern -> variable categories ASSIGNS expressions OUTPUTS output','pattern',6,'p_pattern','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',90),
  ('pattern -> variable ASSIGNS expressions OUTPUTS output','pattern',5,'p_pattern','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',91),
  ('expressions -> expression expressions','expressions',2,'p_expressions','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',102),
  ('expressions -> expression','expressions',1,'p_expressions','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',103),
  ('expression -> xml','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',115),
  ('expression -> variable','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',116),
  ('expression -> categories','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',117),
  ('expression -> LITERAL','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',118),
  ('expression -> ANYEXPR','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',119),
  ('expression -> MULTIEXPR','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',120),
  ('expression -> MULTINUMBEREDEXPR','expression',1,'p_expression','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',121),
  ('variable -> ID','variable',1,'p_variable','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',131),
  ('categories -> LEFTBRACKET categValues RIGHTBRACKET','categories',3,'p_categories','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',138),
  ('categValues -> categValue COMMA categValues','categValues',3,'p_categValues','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',145),
  ('categValues -> categValue','categValues',1,'p_categValues','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',146),
  ('categValue -> ID','categValue',1,'p_categValue','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',157),
  ('xml -> ID LEFTPAREN expressions RIGHTPAREN','xml',4,'p_xml','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',164),
  ('xml -> ID LEFTPAREN RIGHTPAREN','xml',3,'p_xml','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',165),
  ('output -> STRING','output',1,'p_output','W:\\Nifty Prose Articulator\\workspace2\\another\\src\\mathml2\\database.py',176),
]
