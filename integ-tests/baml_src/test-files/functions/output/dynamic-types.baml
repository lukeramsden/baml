// Test file for dynamic type functionality

// Define a dynamic type alias that can be replaced at runtime
type DynamicReturnType = @@dynamic
type DynamicInputType = @@dynamic
type DynamicFieldType = @@dynamic

client<llm> DynamicTestClient {
  provider openai
  options {
    model gpt-4
    api_key env.OPENAI_API_KEY
  }
}

// Simple function that returns a dynamic type
function GetDynamicValue() -> DynamicReturnType {
  client DynamicTestClient
  prompt #"
    Return the number 42 if expecting an integer.
    Return 'Hello, dynamic world!' if expecting a string.
    Return a list of numbers [1, 2, 3] if expecting a list.
    Return an object with name and age if expecting a class.
  "#
}

// Async version of the function
function GetDynamicValueAsync() -> DynamicReturnType {
  client DynamicTestClient
  prompt #"
    Return a string value: 'Async dynamic response'
  "#
}

// Function with dynamic input and output
function ProcessDynamicData(input_data: DynamicInputType) -> DynamicReturnType {
  client DynamicTestClient
  prompt #"
    You received: {{ input_data }}
    Return the length of the input as an integer.
  "#
}

// Test cases for the functions
test TestDynamicInt {
  functions [GetDynamicValue]
  args {}
  // TypeBuilder will set DynamicReturnType to int at runtime
}

test TestDynamicString {
  functions [GetDynamicValue]
  args {}
  // TypeBuilder will set DynamicReturnType to string at runtime
}

test TestDynamicWithInput {
  functions [ProcessDynamicData]
  args {
    input_data "test string"
  }
  // TypeBuilder will set types at runtime
}