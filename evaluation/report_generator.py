
def generate_report(results):
    total = len(results)

    passed = sum(
        1 for r in results
        if r["result"] == "PASS"
    )

    failed = sum(
        1 for r in results
        if r["result"] == "FAIL"
    )

    pass_rate = (passed / total) * 100 if total > 0 else 0

    failure_categories = {}

    for r in results:
        if r["result"] == "FAIL":
            category = r["category"]

            if category in failure_categories:
                failure_categories[category] += 1
            else:
                failure_categories[category] = 1

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round(pass_rate, 1),
        "failure_categories": failure_categories
    }

def format_report(report):
    print("\n=== LLM EVALUATION REPORT ===")
    print(f"Total Cases: {report['total']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print(f"Pass Rate: {report['pass_rate']}%")

    print("\nFailure Categories:")

    for category, count in report["failure_categories"].items():
        print(f"- {category}: {count}")