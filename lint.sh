#!/bin/bash
mypy --ignore-missing-imports main.py
if [[ $? -eq 0 ]]; then
    echo "No typing errors found";
else
    exit $?;
fi
