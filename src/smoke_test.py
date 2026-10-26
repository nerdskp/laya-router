from laya import Router

router = Router()  # first run downloads the checkpoint (~800 MB)

query = "A train travels 60 km in 1.5 hours. What is its average speed?"
questions = {
    "solvable": {
        "type": "choice",
        "instructions": "Will a small 1.5B-parameter model answer this question correctly?",
        "criteria": {"A": "yes, the small model will be correct", "B": "no, the small model will be wrong"},
    }
}

result = router.predict(query, questions)
print(result["answers"]["solvable"])
print(result["routing"]["model"])