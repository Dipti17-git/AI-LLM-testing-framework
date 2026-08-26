# AI/LLM Test Strategy

## Objective

The objective of this testing approach is to evaluate whether an LLM-based application produces responses that are accurate, relevant, grounded in the provided context, and compliant with system instructions.

## Testing Approach

Unlike traditional deterministic applications, LLM applications may produce different valid responses for the same input.

Therefore, testing should evaluate both deterministic properties and semantic quality.

## Key Validation Areas

### Functional Validation

Validate whether the model follows the application's defined requirements and instructions.

### Groundedness

Validate whether factual claims made by the model are supported by the provided context or source information.

### Missing Information

Validate whether the model appropriately identifies when sufficient information is unavailable rather than generating unsupported answers.

### Unsupported Inference

Validate whether the model makes conclusions that are not explicitly supported by the available information.

### Privacy

Validate whether the model protects restricted or personal information according to its instructions.

### Boundary and Negative Testing

Validate model behaviour when receiving ambiguous, incomplete, conflicting or unsupported questions.

## Test Design Principle

Each AI response should be evaluated at claim level rather than treating the complete response as correct simply because most of the answer is accurate.

Important factual claims should be traceable to the supplied source or context when the model is instructed to answer only from that information.
