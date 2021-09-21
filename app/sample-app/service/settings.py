import os
"""
This file contains configurations for receiver service.
The configurations can be over-ridden with Environment Variables during run time.
"""

JSON_DIR = os.getenv("JSON_DIR", "/Users/nayanajith/Desktop/k8s-lab/k8s-live-interview/app/sample-app/resources")
FILE_NAME = os.getenv("FILE_NAME", "input.json")