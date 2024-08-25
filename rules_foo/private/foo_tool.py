import pydantic
import sys

from pathlib import Path


if __name__ == '__main__':
    pydantic_version = pydantic.__version__
    f = sys.argv[1]
    Path(f).write_text(pydantic_version)
