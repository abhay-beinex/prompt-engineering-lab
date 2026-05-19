# Experiment Overview

This experiment evaluated the effectiveness of 10 prompt engineering techniques across three OpenAI models:

- GPT-5.5
- GPT-5.4
- GPT-5.4-mini

The selected business task was:

**Meeting Notes → Action Items Extraction**

Each prompt was executed against all three models using the same meeting transcript input. The goal was to compare:

- Prompting technique effectiveness
- Model capability differences
- Cost-quality tradeoffs
- Instruction-following reliability
- Production readiness

A total of:

- 10 prompt variants
- × 3 models
- = 30 experiment runs

were executed programmatically using the OpenAI Python SDK.

---

# Observed Trends

## 1. Zero-shot prompts produced usable outputs, but lacked consistency

Prompt 01 (basic zero-shot) successfully extracted action items across all models, demonstrating strong native reasoning ability.

However:

- Output formatting varied significantly
- Some models returned markdown tables instead of JSON
- Priority assignment was inconsistent
- Certain deadlines were inferred differently

GPT-5.5 produced the most complete baseline output, while GPT-5.4-mini generated simpler but still useful summaries.

---

## 2. Explicit formatting dramatically improved consistency

Prompt 02 showed a major improvement in:

- JSON validity
- Structural consistency
- Machine-readability
- Evaluation simplicity

This demonstrates that explicit schema guidance strongly improves deterministic output behavior.

Smaller models benefited the most from format constraints.

---

## 3. Few-shot prompting significantly improved extraction quality

Prompt 04 (few-shot) consistently produced:

- Better task identification
- More accurate ownership extraction
- Improved prioritization
- Cleaner formatting

The inclusion of:

- multiple positive examples
- one negative example

helped reduce irrelevant meeting discussion leakage.

This was especially effective for GPT-5.4-mini.

---

## 4. Chain-of-thought prompting increased reasoning depth but also increased token usage

Prompt 05 generated:

- very detailed outputs
- richer reasoning
- additional assumptions
- more contextual interpretation

However, it also:

- greatly increased completion tokens
- increased latency
- sometimes introduced unnecessary verbosity

For example:

- GPT-5.5 generated extremely detailed structured reasoning
- GPT-5.4-mini produced long JSON explanations with embedded notes

This demonstrates a classic tradeoff:

Higher reasoning quality ↔ higher computational cost.

---

## 5. Role prompting improved professionalism

Prompts using:

- Agile project manager personas
- enterprise coordination personas
- technical program manager roles

produced:

- more professional wording
- clearer prioritization
- cleaner task descriptions

Role prompting improved output tone consistency without significantly increasing token cost.

---

## 6. Hybrid prompts produced the best production-quality outputs

Prompt 08 and Prompt 10 consistently performed best overall.

These prompts combined:

- role prompting
- structured formatting
- reasoning guidance
- constraints
- examples

The resulting outputs were:

- concise
- valid JSON
- production-ready
- highly structured
- easy to evaluate programmatically

Prompt 10 delivered the strongest balance of:

- quality
- consistency
- professionalism
- conciseness

across all three models.

---

# Model Comparison

## GPT-5.5

### Strengths

- Best reasoning quality
- Most complete extraction
- Best contextual understanding
- Strongest prioritization logic
- Best handling of ambiguous instructions

### Weaknesses

- Highest latency
- Highest token usage
- Occasionally overly verbose during CoT prompting

### Observation

GPT-5.5 performed best overall, especially on:

- Chain-of-thought prompts
- hybrid prompts
- complex structured extraction

However, the quality improvement over GPT-5.4 was smaller than expected for this task.

---

## GPT-5.4

### Strengths

- Strong instruction following
- Excellent JSON formatting
- Lower latency than GPT-5.5
- Very balanced performance

### Weaknesses

- Slightly weaker reasoning depth
- Less contextual interpretation

### Observation

GPT-5.4 achieved near-frontier quality on most prompts.

For structured enterprise extraction tasks, it offered the best balance between:

- quality
- speed
- cost

This model appears highly suitable for production deployment.

---

## GPT-5.4-mini

### Strengths

- Fastest responses
- Lowest computational cost
- Surprisingly strong structured extraction

### Weaknesses

- Less nuanced reasoning
- Occasionally simplified outputs
- More sensitive to weak prompts

### Observation

GPT-5.4-mini performed significantly better when:

- examples were provided
- formatting constraints existed
- role prompting was used

Without guidance, output quality dropped noticeably.

---

# Technique Ranking (Estimated Overall Performance)

| Rank | Prompt Technique | Observation |
|---|---|---|
| 1 | Prompt 10 — Optimized Best-Shot | Best overall balance |
| 2 | Prompt 08 — Role + Few-shot | Excellent structure + consistency |
| 3 | Prompt 09 — System + CoT | Strong reasoning quality |
| 4 | Prompt 04 — Few-shot | Strong extraction reliability |
| 5 | Prompt 07 — Role Prompting | Professional outputs |
| 6 | Prompt 06 — System Persona | Better behavioral control |
| 7 | Prompt 05 — CoT | Strong reasoning but expensive |
| 8 | Prompt 03 — One-shot | Improved consistency |
| 9 | Prompt 02 — Format Guidance | Better structure only |
| 10 | Prompt 01 — Zero-shot | Weakest consistency |

---

# Cost-Quality Tradeoff Analysis

## Key Finding

The largest increase in token usage came from chain-of-thought prompting.

Prompt 05 generated substantially larger responses across all models.

Examples observed:

- GPT-5.5 generated extensive reasoning traces
- GPT-5.4-mini produced verbose structured explanations

This increased:

- latency
- completion tokens
- overall operational cost

---

## Was GPT-5.5 Worth the Premium?

For this task:

### Partially.

GPT-5.5 produced the highest-quality outputs overall.

However:

- GPT-5.4 often achieved comparable structured extraction quality
- the quality gap was smaller than the latency/token gap

Therefore:

- GPT-5.5 is ideal for premium enterprise workflows requiring maximum reliability
- GPT-5.4 is likely the most cost-effective production choice

---

# Failure Analysis

## Failure Case 1 — Prompt 01 + GPT-5.4-mini

### Issue

Returned a markdown table instead of structured JSON.

### Cause

No explicit formatting instruction was provided.

### Insight

Smaller models require stronger structural guidance.

---

## Failure Case 2 — Prompt 05 + GPT-5.5

### Issue

Output became extremely verbose with additional assumptions and metadata.

### Cause

Chain-of-thought prompting encouraged expanded reasoning generation.

### Insight

Reasoning prompts improve quality but can dramatically increase operational cost.

---

## Failure Case 3 — Prompt 01 + GPT-5.4

### Issue

Included descriptive summaries alongside action items.

### Cause

Prompt lacked constraints on output filtering.

### Insight

Zero-shot prompts often fail to distinguish:

- actionable tasks
- contextual discussion

without explicit guidance.

---

# Production Recommendation

## Recommended Production Configuration

### Model

GPT-5.4

### Prompt

Prompt 10 — Optimized Best-Shot

---

## Why?

This combination provided:

- excellent instruction following
- valid JSON outputs
- concise formatting
- strong extraction accuracy
- reasonable latency
- balanced token usage

Compared to GPT-5.5:

- quality was very close
- operational cost would likely be significantly lower

Compared to GPT-5.4-mini:

- reliability and consistency were noticeably better

---

# Final Conclusion

This experiment demonstrated that prompt engineering significantly affects output quality, even when using highly capable frontier models.

The results showed:

- Explicit structure improves reliability
- Few-shot prompting strongly improves extraction accuracy
- Chain-of-thought improves reasoning but increases cost
- Hybrid prompts consistently outperform simple prompts
- Smaller models benefit more from strong prompt engineering

Most importantly, the experiment demonstrated that carefully designed prompts can allow mid-tier production models to achieve near-frontier quality for structured business automation tasks.

This highlights the importance of prompt engineering as a practical optimization layer in real-world AI systems.

