// Test file for the new @@dynamic type alias feature

// Define a dynamic type alias that can be replaced at runtime
type DynamicReturnType = @@dynamic

// Function that returns the dynamic type
function GetDynamic() -> DynamicReturnType {
  client GPT4
  prompt #"
    Generate output in the specified format:
    {{ctx.output_format}}
  "#
}

// Another function to test with dynamic input
function ProcessDynamic(input: DynamicReturnType) -> string {
  client GPT4
  prompt #"
    Process the input: {{input}}
  "#
}

// Test case showing how to use TypeBuilder to replace the dynamic type
test TestDynamicTypeAlias {
  functions [GetDynamic]
  type_builder {
    // Replace DynamicReturnType with int
    type DynamicReturnType = int
  }
  args {
    // No args needed for GetDynamic
  }
}

test TestDynamicUnion {
  functions [GetDynamic]
  type_builder {
    // Replace DynamicReturnType with a union type
    class Action1 {
      type string
      data string
    }
    
    class Action2 {
      type string
      value int
    }
    
    type DynamicReturnType = Action1 | Action2
  }
  args {
    // No args needed
  }
}

test TestDynamicArray {
  functions [GetDynamic]
  type_builder {
    // Replace DynamicReturnType with an array
    type DynamicReturnType = string[]
  }
  args {
    // No args needed
  }
}