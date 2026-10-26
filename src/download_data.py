from datasets import load_dataset

gsm8k = load_dataset("openai/gsm8k", "main")
arc_c = load_dataset("allenai/ai2_arc", "ARC-Challenge")
arc_e = load_dataset("allenai/ai2_arc", "ARC-Easy")

for name, ds in [("GSM8K", gsm8k), ("ARC-Challenge", arc_c), ("ARC-Easy", arc_e)]:
    print(name, {split: len(ds[split]) for split in ds})
