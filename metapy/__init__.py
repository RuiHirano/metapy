import os
import sys
from pathlib import Path
sys.path.append(str(Path(os.path.dirname(__file__)).joinpath('.').resolve()))

from .api import MetaPy