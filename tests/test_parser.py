from nose.tools import assert_equals
from ion.parser import parse

def test_basic_name_is_parsed_okay():
    assert_equals(parse('name'), 'name')

def test_basic_function_is_parsed_okay():
    assert_equals(parse('$x.x'), ['$x', 'x'])

def test_nested_functions_are_parsed_okay():
    assert_equals(parse('$x.$y.x'), ['$x', ['$y', 'x']])

def test_basic_applications_are_parsed_okay():
    assert_equals(parse('($x.x y)'), [['$x', 'x'], 'y'])

def test_complicated_function_parsed_okay():
    complicated = '$a.(a $b.(b a))'
    expected = ['$a', ['a', ['$b', ['b', 'a']]]]
    assert_equals(parse(complicated), expected)

def test_complicated_application_parsed_okay():
    complicated = '(($x.$y.(y x) $p.$q.p) $i.i)'
    expected = [[['$x', ['$y', ['y', 'x']]], ['$p', ['$q', 'p']]], ['$i', 'i']]
    assert_equals(parse(complicated), expected)

def test_very_complicated_application_parsed_okay():
    complicated = '((($f.$g.$x.(f (g x)) $s.(s s)) $a.$b.b) $x.$y.x)'
    expected = [[[['$f', ['$g', ['$x', ['f', ['g', 'x']]]]], ['$s', ['s', 's']]], ['$a', ['$b', 'b']]], ['$x', ['$y', 'x']]]
    assert_equals(parse(complicated), expected)
