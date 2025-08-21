"""Test dynamic type functionality in BAML."""

import pytest
from baml_client import b
from baml_client.type_builder import TypeBuilder


def test_dynamic_type_with_int():
    """Test that dynamic types can be replaced with int at runtime."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.int())
    
    # Call a function that returns @@dynamic type
    result = b.GetDynamicValue(tb=tb)
    assert isinstance(result, int)
    assert result == 42


def test_dynamic_type_with_string():
    """Test that dynamic types can be replaced with string at runtime."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.string())
    
    # Call a function that returns @@dynamic type
    result = b.GetDynamicValue(tb=tb)
    assert isinstance(result, str)


def test_dynamic_type_with_union():
    """Test that dynamic types can be replaced with union types at runtime."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.union([tb.string(), tb.int()]))
    
    # Call a function that returns @@dynamic type
    result = b.GetDynamicValue(tb=tb)
    assert isinstance(result, (str, int))


def test_dynamic_type_with_list():
    """Test that dynamic types can be replaced with list types at runtime."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.list(tb.int()))
    
    # Call a function that returns @@dynamic type
    result = b.GetDynamicValue(tb=tb)
    assert isinstance(result, list)
    if result:  # if not empty
        assert all(isinstance(item, int) for item in result)


def test_dynamic_type_with_class():
    """Test that dynamic types can be replaced with class types at runtime."""
    tb = TypeBuilder()
    
    # Define a dynamic class
    user_class = tb.add_class("User")
    user_class.add_property("name", tb.string())
    user_class.add_property("age", tb.int())
    
    tb.type_alias("DynamicReturnType", user_class.type())
    
    # Call a function that returns @@dynamic type
    result = b.GetDynamicValue(tb=tb)
    assert hasattr(result, 'name')
    assert hasattr(result, 'age')


def test_multiple_dynamic_types():
    """Test that multiple dynamic types can be used in the same function."""
    tb = TypeBuilder()
    tb.type_alias("DynamicInputType", tb.string())
    tb.type_alias("DynamicReturnType", tb.int())
    
    # Call a function with both dynamic input and output types
    result = b.ProcessDynamicData(input_data="test", tb=tb)
    assert isinstance(result, int)


def test_nested_dynamic_types():
    """Test dynamic types in nested structures."""
    tb = TypeBuilder()
    
    # Create a class with a dynamic field
    data_class = tb.add_class("DataContainer")
    data_class.add_property("id", tb.int())
    data_class.add_property("value", tb.type_alias("DynamicFieldType", tb.string()))
    
    tb.type_alias("DynamicReturnType", data_class.type())
    
    result = b.GetDynamicValue(tb=tb)
    assert hasattr(result, 'id')
    assert hasattr(result, 'value')
    assert isinstance(result.value, str)


def test_dynamic_type_error_when_not_provided():
    """Test that an error is raised when dynamic type is not provided."""
    tb = TypeBuilder()
    # Don't set the dynamic type alias
    
    with pytest.raises(Exception) as exc_info:
        b.GetDynamicValue(tb=tb)
    
    assert "Dynamic type alias" in str(exc_info.value)
    assert "was not replaced at runtime" in str(exc_info.value)


@pytest.mark.asyncio
async def test_dynamic_type_async():
    """Test dynamic types work with async functions."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.string())
    
    result = await b.GetDynamicValueAsync(tb=tb)
    assert isinstance(result, str)


def test_dynamic_type_with_optional():
    """Test dynamic types can be made optional."""
    tb = TypeBuilder()
    tb.type_alias("DynamicReturnType", tb.optional(tb.string()))
    
    result = b.GetDynamicValue(tb=tb)
    assert result is None or isinstance(result, str)