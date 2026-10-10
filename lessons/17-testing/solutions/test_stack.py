import pytest

from stack import Stack


def test_new_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()
    assert len(stack) == 0


def test_push_then_pop():
    stack = Stack()
    stack.push(42)
    assert stack.pop() == 42
    assert stack.is_empty()


def test_pop_order_is_last_in_first_out():
    stack = Stack()
    for item in ["a", "b", "c"]:
        stack.push(item)
    assert stack.pop() == "c"
    assert stack.pop() == "b"
    assert stack.pop() == "a"


def test_peek_leaves_item_on_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    assert stack.peek() == "b"
    assert stack.peek() == "b"
    assert len(stack) == 2


def test_length_changes_with_push_and_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    stack.pop()
    assert len(stack) == 1
    assert not stack.is_empty()


def test_pop_empty_stack():
    with pytest.raises(IndexError):
        Stack().pop()


def test_peek_empty_stack():
    with pytest.raises(IndexError):
        Stack().peek()


def test_separate_stacks_are_independent():
    # This would fail if `_items` were shared between stacks by mistake
    first = Stack()
    second = Stack()
    first.push(1)
    assert second.is_empty()
