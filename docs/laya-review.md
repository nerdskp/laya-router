# Laya review (Group B)

Owner: Surya
Status: draft

## 1. Laya fine-tuning data format
- Input: state (text or JSON) + dict of typed questions
- Question fields: type, instructions, criteria
- Targets: hard label or soft teacher distribution? (check notebook)
- Schema the notebook expects: <paste the key fields from the notebook>

## 2. How others framed routing
| Model | Routes what | Labels from | Notes |
|---|---|---|---|
| Mimir (impacte/mimir-laya-router) | Which model should answer | | |
| laya-conductor (mvilacad) | Route vs continue, coding agent | Claude Sonnet | 66% one class |
| palboy/laya-model-router | Route labels | | 39-example eval |
| thechristyjo/laya-model-routing | Six model classes | Judge | 200 queries |
| Tollgate (ihemanthc) | Minimum sufficient tier | | calibration split |
| head-rout-gold (ngdghfdc) | Action routing | | option shuffling |

Key point: all of them predict a property of the query, not whether a specific small model was correct.

## 3. Limits from Laya's Honest Limits section that affect us
- <limit> → <what it means for our 1.5B/GSM8K setup>
- Token budget: options share head_max_len (192 on English)
- Base checkpoint below majority-class baseline on typed-decisions
- Temperatures clamped to [0.5, 5.0]

## 4. Router question (draft)
- Option A: noul with labels {"false": "B", "true": "A"}
- Option B: two-option choice
- Chosen: <fill after team decision>
- Example row: <paste one JSON example>

## 5. Open questions for the team
- How do we parse GSM8K and ARC answers reliably?
- Do we fine-tune on GSM8K and ARC together or separately?
