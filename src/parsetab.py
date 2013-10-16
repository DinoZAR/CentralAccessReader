
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xba(v\x19\xe6\xfd\xab\t\xddh|/\xee]\xc5\xad'
    
_lr_action_items = {'RIGHTBRACKET':([24,25,26,42,],[32,-21,-22,-20,]),'MULTIEXPR':([10,14,15,16,17,18,19,21,22,23,27,30,32,37,44,50,52,54,],[15,-11,-16,-17,-15,-14,-12,15,-18,-13,15,15,-19,-26,-25,15,-24,-23,]),'ASSIGNS':([5,7,12,32,41,],[10,-18,27,-19,47,]),'MULTINUMBEREDEXPR':([10,14,15,16,17,18,19,21,22,23,27,30,32,37,44,50,52,54,],[16,-11,-16,-17,-15,-14,-12,16,-18,-13,16,16,-19,-26,-25,16,-24,-23,]),'ANYEXPR':([10,14,15,16,17,18,19,21,22,23,27,30,32,37,44,50,52,54,],[17,-11,-16,-17,-15,-14,-12,17,-18,-13,17,17,-19,-26,-25,17,-24,-23,]),'OUTPUTS':([14,15,16,17,18,19,20,21,22,23,29,32,34,37,44,52,54,],[-11,-16,-17,-15,-14,-12,28,-10,-18,-13,-9,-19,43,-26,-25,-24,-23,]),'LEFTPAREN':([22,46,],[30,50,]),'LEFTCARET':([22,],[31,]),'LITERAL':([10,14,15,16,17,18,19,21,22,23,27,30,32,37,44,47,50,52,54,],[18,-11,-16,-17,-15,-14,-12,18,-18,-13,18,18,-19,-26,-25,51,18,-24,-23,]),'RIGHTPAREN':([14,15,16,17,18,19,21,22,23,29,30,32,37,38,44,50,52,53,54,],[-11,-16,-17,-15,-14,-12,-10,-18,-13,-9,37,-19,-26,44,-25,52,-24,54,-23,]),'LEFTBRACKET':([5,7,10,14,15,16,17,18,19,21,22,23,27,30,32,37,44,50,52,54,],[11,-18,11,-11,-16,-17,-15,-14,-12,11,-18,-13,11,11,-19,-26,-25,11,-24,-23,]),'RIGHTCARET':([39,40,49,51,],[-28,46,-27,-29,]),'IMPORT':([0,2,6,9,35,36,48,],[4,4,4,-6,-30,-8,-7,]),'STRING':([28,43,],[35,35,]),'COMMA':([25,26,39,51,],[33,-22,45,-29,]),'ID':([0,2,4,6,9,10,11,14,15,16,17,18,19,21,22,23,27,30,31,32,33,35,36,37,44,45,48,50,52,54,],[7,7,9,7,-6,22,26,-11,-16,-17,-15,-14,-12,22,-18,-13,22,22,41,-19,26,-30,-8,-26,-25,41,-7,22,-24,-23,]),'$end':([1,2,3,6,8,9,13,35,36,48,],[0,-4,-1,-5,-2,-6,-3,-30,-8,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'xml':([10,21,27,30,50,],[14,14,14,14,14,]),'database':([0,],[1,]),'pattern':([0,2,6,],[2,2,2,]),'attribute':([31,45,],[39,39,]),'categValues':([11,33,],[24,42,]),'categValue':([11,33,],[25,25,]),'patterns':([0,2,6,],[3,8,13,]),'output':([28,43,],[36,48,]),'variable':([0,2,6,10,21,27,30,50,],[5,5,5,19,19,19,19,19,]),'import':([0,2,6,],[6,6,6,]),'expressions':([10,21,27,30,50,],[20,29,34,38,53,]),'attributes':([31,45,],[40,49,]),'expression':([10,21,27,30,50,],[21,21,21,21,21,]),'categories':([5,10,21,27,30,50,],[12,23,23,23,23,23,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> database","S'",1,None,None,None),
  ('database -> patterns','database',1,'p_database','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',91),
  ('patterns -> pattern patterns','patterns',2,'p_patterns','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',97),
  ('patterns -> import patterns','patterns',2,'p_patterns','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',98),
  ('patterns -> pattern','patterns',1,'p_patterns','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',99),
  ('patterns -> import','patterns',1,'p_patterns','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',100),
  ('import -> IMPORT ID','import',2,'p_import','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',111),
  ('pattern -> variable categories ASSIGNS expressions OUTPUTS output','pattern',6,'p_pattern','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',117),
  ('pattern -> variable ASSIGNS expressions OUTPUTS output','pattern',5,'p_pattern','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',118),
  ('expressions -> expression expressions','expressions',2,'p_expressions','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',129),
  ('expressions -> expression','expressions',1,'p_expressions','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',130),
  ('expression -> xml','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',145),
  ('expression -> variable','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',146),
  ('expression -> categories','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',147),
  ('expression -> LITERAL','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',148),
  ('expression -> ANYEXPR','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',149),
  ('expression -> MULTIEXPR','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',150),
  ('expression -> MULTINUMBEREDEXPR','expression',1,'p_expression','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',151),
  ('variable -> ID','variable',1,'p_variable','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',160),
  ('categories -> LEFTBRACKET categValues RIGHTBRACKET','categories',3,'p_categories','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',167),
  ('categValues -> categValue COMMA categValues','categValues',3,'p_categValues','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',174),
  ('categValues -> categValue','categValues',1,'p_categValues','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',175),
  ('categValue -> ID','categValue',1,'p_categValue','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',188),
  ('xml -> ID LEFTCARET attributes RIGHTCARET LEFTPAREN expressions RIGHTPAREN','xml',7,'p_xml','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',195),
  ('xml -> ID LEFTCARET attributes RIGHTCARET LEFTPAREN RIGHTPAREN','xml',6,'p_xml','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',196),
  ('xml -> ID LEFTPAREN expressions RIGHTPAREN','xml',4,'p_xml','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',197),
  ('xml -> ID LEFTPAREN RIGHTPAREN','xml',3,'p_xml','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',198),
  ('attributes -> attribute COMMA attributes','attributes',3,'p_attributes','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',212),
  ('attributes -> attribute','attributes',1,'p_attributes','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',213),
  ('attribute -> ID ASSIGNS LITERAL','attribute',3,'p_attribute','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',224),
  ('output -> STRING','output',1,'p_output','/Users/atrctech/Desktop/workspace/NiftyProseArticulator/src/mathml/database.py',230),
]
