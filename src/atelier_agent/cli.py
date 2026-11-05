import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Draft three Chinese WeChat messages for CA review."
    )
    parser.add_argument(
        "--question",
        required=True,
    )
    parser.add_argument(
        "--data-dir", 
        type=Path, 
        default=Path("data")
    )
    parser.add_argument(
        "--case-file", 
        type=Path, 
        default=Path("examples/cases/acceptance.json")
    )
    
    parser.add_argument(
        "--output", 
        type=Path, 
        default=Path("examples/live/single.json")
    )
    args = parser.parse_args()

    # 当前只验证命令行入口，尚未接入检索或模型。
    result = {
        "status": "incomplete",
        "question": args.question,
        "answer": None,
    }

    print(json.dumps(result, ensure_ascii=False))