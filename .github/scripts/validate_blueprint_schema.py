#!/usr/bin/env python3
import os
import yaml
import sys
import glob

VALID_MODES = ["single", "restart", "queued", "parallel"]

def validate_blueprint(file_path):
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return [f"{file_path}: YAML parsing error: {e}"]

    if not isinstance(data, dict):
        errors.append(f"{file_path}: Top-level structure is not a dictionary")
        return errors

    if "blueprint" not in data:
        errors.append(f"{file_path}: Missing top-level 'blueprint:' block")
        return errors

    bp = data["blueprint"]

    # Required blueprint fields
    for field in ["name", "description", "domain"]:
        if field not in bp:
            errors.append(f"{file_path}: Missing required blueprint field '{field}'")

    # Validate mode
    if "mode" in data and data["mode"] not in VALID_MODES:
        errors.append(
            f"{file_path}: Invalid mode '{data['mode']}', allowed: {', '.join(VALID_MODES)}"
        )

    # Validate inputs
    inputs = bp.get("input", {})
    if not isinstance(inputs, dict):
        errors.append(f"{file_path}: 'input:' must be a dictionary")
    else:
        for key, value in inputs.items():
            if "selector" in value and not isinstance(value["selector"], dict):
                errors.append(f"{file_path}: Input '{key}' has invalid selector definition")

    return errors


def main():
    yaml_files = glob.glob("**/*.yaml", recursive=True) + glob.glob("**/*.yml", recursive=True)

    if not yaml_files:
        print(f"⚠️ No Blueprint files found")
        return True
    
    problems = []

    for file_path in yaml_files:
        problems.extend(validate_blueprint(file_path))

    if problems:
        print("❌ Blueprint Validation FAILED:\n")
        for p in problems:
            print(" - " + p)
        sys.exit(1)

    print("✅ Blueprint Validation OK for all YAML files.")


if __name__ == "__main__":
    main()
