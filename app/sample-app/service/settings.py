import os
"""
This file contains configurations for receiver service.
The configurations can be over-ridden with Environment Variables during run time.
"""

JSON_DIR = os.getenv("JSON_DIR", "/usr/src/sample-app/resources")