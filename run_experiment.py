import os
import json
import time
import pandas as pd

from dotenv import load_dotenv
from openai import OpenAI

# ----------------------------------------
# Load environment variables
# ----------------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ----------------------------------------
# Models to evaluate
# ----------------------------------------

MODELS = [
    "gpt-5.5",
    "gpt-5.4",
    "gpt-5.4-mini"
]

# ----------------------------------------
# Prompt files
# ----------------------------------------

PROMPT_FILES = [
    "prompt_01_zeroshot.txt",
    "prompt_02_format.txt",
    "prompt_03_oneshot.txt",
    "prompt_04_fewshot.txt",
    "prompt_05_cot.txt",
    "prompt_06_systempersona.txt",
    "prompt_07_role.txt",
    "prompt_08_rolefewshot.txt",
    "prompt_09_systemcot.txt",
    "prompt_10_optimized.txt"
]

# ----------------------------------------
# Load master meeting notes
# ----------------------------------------

with open("prompts/master_meeting_notes.txt", "r", encoding="utf-8") as file:
    meeting_notes = file.read()

# ----------------------------------------
# Store experiment results
# ----------------------------------------

results = []

# ----------------------------------------
# Run experiment
# ----------------------------------------

for model in MODELS:

    print(f"\nRunning model: {model}")

    for prompt_file in PROMPT_FILES:

        print(f"Processing: {prompt_file}")

        # Load prompt template
        with open(f"prompts/{prompt_file}", "r", encoding="utf-8") as file:
            prompt_template = file.read()

        # Insert meeting notes
        final_prompt = prompt_template.replace(
            "{{meeting_notes}}",
            meeting_notes
        )

        # Start latency timer
        start_time = time.time()

        try:

             # API call
            if model == "gpt-5.5":

              response = client.responses.create(
                model=model,
                input=final_prompt
             )

            else:

                response = client.responses.create(
                  model=model,
                  input=final_prompt,
                  temperature=0
                )

            # End latency timer
            end_time = time.time()

            latency = round(end_time - start_time, 2)

            # Extract response text
            output_text = response.output_text

            # Token usage
            usage = response.usage

            prompt_tokens = usage.input_tokens
            completion_tokens = usage.output_tokens
            total_tokens = usage.total_tokens

            # Save raw output JSON
            output_filename = (
                f"outputs/"
                f"{model.replace('.', '_')}_"
                f"{prompt_file.replace('.txt', '.json')}"
            )

            with open(output_filename, "w", encoding="utf-8") as json_file:

                json.dump(
                    {
                        "model": model,
                        "prompt_file": prompt_file,
                        "latency_seconds": latency,
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": total_tokens,
                        "response": output_text
                    },
                    json_file,
                    indent=4
                )

            # Store CSV row
            results.append({
                "model": model,
                "prompt_file": prompt_file,
                "latency_seconds": latency,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
                "response_preview": output_text[:150]
            })

            print("Completed successfully.")

        except Exception as error:

            print(f"Error: {error}")

# ----------------------------------------
# Save experiment summary CSV
# ----------------------------------------

df = pd.DataFrame(results)

df.to_csv("experiment_results.csv", index=False)

print("\nExperiment completed successfully.")