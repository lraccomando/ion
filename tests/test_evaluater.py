"""
"""
from nose.tools import assert_equals
from ion.parser import parse
from ion.evaluater import evaluate, Function

def test_simple_name_evaluation():
    assert_equals(parse('x'), evaluate(parse('x')))

def test_functions_created_properly():
    assert_equals(type(evaluate(parse('$x.x'))), Function)

def test_basic_applications_work_properly():
	assert_equals(evaluate(parse('($x.x y)')), 'y')

def test_complicated_applications_work_properly():
	evaluated = evaluate(parse('((($f.$g.$x.(f (g x)) $s.(s s)) $a.$b.b) $x.$y.x)'))
	assert_equals(str(evaluated), "$b.['b']")
