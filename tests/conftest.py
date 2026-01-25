"""Pytest configuration and fixtures"""

import sys
import os

# Add the sourcesage package to path for testing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
