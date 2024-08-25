import pydantic
import os
import platform
import sys
import sysconfig

from pathlib import Path


if __name__ == '__main__':
    pydantic_version = pydantic.__version__
    os_name = os.name
    platform_machine = platform.machine()
    sysconfig_platform = sysconfig.get_platform()

    output_path = sys.argv[1]
    with open(output_path, 'w') as f:
        f.write(f"pydantic_version: {pydantic_version}\n")
        f.write(f"os_name: {os_name}\n")
        f.write(f"platform_machine: {platform_machine}\n")
        f.write(f"sysconfig_platform: {sysconfig_platform}\n")
