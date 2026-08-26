# AI Defect Report

## Defect ID

LLM-001

## Title

AI approves transportation reimbursement without validating expense eligibility against commuting requirements.

## Category

Groundedness / Policy Compliance

## Policy

Employees can claim up to 500 DKK per month for public transportation expenses related to commuting to the office. Claims must include a valid receipt.

## User Prompt

I spent 350 DKK on my metro pass and 100 DKK on a taxi to a client meeting. Can I claim the full 450 DKK?

## AI Response

The AI approved the complete 450 DKK reimbursement because the total transportation expense was below the 500 DKK monthly limit.

## Expected Behaviour

The model should first validate whether each expense satisfies the policy eligibility requirements before determining the reimbursable amount.

The available policy does not establish that transportation to a client meeting qualifies as commuting to the office.

## Actual Behaviour

The model combined both transportation expenses and approved the complete amount based primarily on the 500 DKK threshold.

## Result

FAIL

## Risk

The model may incorrectly approve expenses by validating the monetary threshold without first validating whether the underlying expenses are eligible under the supplied policy.
