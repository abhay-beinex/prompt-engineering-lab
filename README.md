# Prompt Engineering Lab

## Overview

This project evaluates prompt engineering strategies across multiple OpenAI GPT models using a structured business task.

The selected task was:

Meeting Notes → Action Items Extraction

The experiment compares:
- Prompt engineering techniques
- Model quality
- Token usage
- Latency
- Cost-quality tradeoffs

---

## Models Evaluated

- GPT-5.5
- GPT-5.4
- GPT-5.4-mini

---

## Prompt Techniques

1. Zero-shot
2. Zero-shot + format guidance
3. One-shot prompting
4. Few-shot prompting
5. Chain-of-thought
6. System persona prompting
7. Role prompting
8. Role + few-shot
9. System + CoT
10. Optimized best-shot prompting

---

## Project Structure
```plaintext

prompt-engineering-lab/
│
├── prompts/
├── outputs/
├── scores.csv
├── experiment_results.csv
├── prompts_library.md
├── run_experiment.py
├── README.md
```

---

## Setup Instructions

1. Install dependencies

pip install -r requirements.txt

2. Create .env file

OPENAI_API_KEY=your_api_key_here

3. Run experiment

python run_experiment.py

---

## Key Findings

- Few-shot prompting significantly improved extraction quality.
- Explicit formatting improved JSON consistency.
- Chain-of-thought prompting increased reasoning quality but also increased token usage.
- GPT-5.4 achieved near GPT-5.5 quality for this task with lower operational cost.
- Hybrid prompts consistently performed best.

---

## Final Recommendation

Recommended Production Setup:
- Model: GPT-5.4
- Prompt: Prompt 10 (Optimized Best-Shot)

This combination provided the best balance between:
- quality
- reliability
- latency
- token efficiency
