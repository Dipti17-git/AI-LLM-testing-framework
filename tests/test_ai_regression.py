import json
import pytest
from llm.client import LLMClient
from evaluation.correctness_evaluator import evaluate_correctness
from evaluation.correctness_evaluator import FakeCorrectnessJudge
from evaluation.report_generator import generate_report, format_report


def load_golden_dataset():
    with open("datasets/golden_dataset.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

client = LLMClient()
judgeClient = FakeCorrectnessJudge()

regression_results = []

@pytest.mark.parametrize ("test_case", load_golden_dataset())
def test_ai_regression(llm_client, judge_client,test_case):
 question = test_case["question"]
 context = test_case["context"]
 expected_behavior = test_case["expected_behavior"]
 category = test_case["category"]
 answer = llm_client.generate(context, question)
 evaluation = evaluate_correctness(judge_client, expected_behavior, answer)

 # Simulated failures used only to validate the reporting pipeline.
 # These are not actual semantic failures detected by the evaluator.
 if test_case["id"] in ["GD-007", "GD-008", "GD-016"]:
     result = "FAIL"
 elif "Result: PASS" in evaluation:
     result = "PASS"
 else:
     result = "FAIL"

 test_result = {
     "id": test_case["id"],
     "category": test_case["category"],
     "result": result,
 }

 regression_results.append(test_result)
 print(len(regression_results))

 if len(regression_results) == len(load_golden_dataset()):

  report = generate_report(regression_results)

  format_report(report)




