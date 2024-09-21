import pydantic
import os
import platform
import sys
import sysconfig

from pathlib import Path

from typing_extensions import Annotated


class MyModel(pydantic.BaseModel):
    name: str = "Tweed"


if __name__ == '__main__':

    model = MyModel(name = "Jacket")
    output_path = sys.argv[1]

    with open(output_path, 'w') as f:
        f.write(str(model.dict()))
