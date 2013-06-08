# MathML Parser Design

## Pattern Database

The MathML parser prepares for parsing by reading a pattern database that contains all the patterns that the parser needs to recognize. The grammar of a pattern is the following:

variable [categories] = mathml<attribute="something",attribute="something">(...) | variable | [category] | "literal" | ? | + | # -> 'output'

A pattern seeks to collapse a collection of elements into a single entity with a single output. The elements it collects can be used to help in the creation of the final output.

## Overview of Flow from MathML to Prose

MathML must somehow be fed into the parser, from which then it outputs the correct prose. It does this using a number of steps:

1. The MathML is converted to a data structure that is comparable to a pattern parsed from the database
2. For each pattern:

    * The pattern is first compared with the main MathML tree
	* All matches are labeled and marked
	* Then, matches that are marked are removed and replaced with the appropriate speech object
	* All speech object's children are then pattern matched like the main MathML tree
	
3. The final structure is checked to make sure it has collapsed into a single speech object successfully
4. A single string is extracted by evaluating every speech object and its dependencies recursively

## Common Pattern Tree

There must be a datatype that can successfully compare a MathML tree and a pattern tree in the same manner.