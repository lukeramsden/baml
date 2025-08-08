// Test file for the new @@dynamic type alias feature

// Define a dynamic type alias that can be replaced at runtime
type DynamicAliasReturn = @@dynamic

// Function that returns the dynamic type
function GetDynamic() -> DynamicAliasReturn {
  client GPT4
  prompt #"
    Generate output in the specified format:
    {{ctx.output_format}}
  "#
}

// Another function to test with dynamic input
function ProcessDynamic(input: DynamicAliasReturn) -> string {
  client GPT4
  prompt #"
    Process the input: {{input}}
  "#
}

// Test cases showing how to use TypeBuilder to replace the dynamic type
// TODO: Re-enable these tests when dynamic type override in type_builder is supported
// The feature should allow redefining @@dynamic types within type_builder blocks
//
// Example test cases that would be enabled:
// 1. TestDynamicTypeAlias - Replace DynamicAliasReturn with int
// 2. TestDynamicUnion - Replace DynamicAliasReturn with Action1 | Action2  
// 3. TestDynamicArray - Replace DynamicAliasReturn with string[]