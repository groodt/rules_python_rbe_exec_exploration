# RBE exec native deps repro

Repro of native deps issues with RBE

## Prerequisites

1. Clone the repo

```
git clone REPO_URL --recursive
```

or

```
git clone REPO_URL
git submodule update --init --recursive
```

2. Launch RBE

In a separate terminal, launch a buildbarn remote build setup using docker compose.

Note: I'm on a mac, it asks for my password, this is due to some `sudo` commands in relation to mounting a volume. See `run.sh` for more detail. I am not entirely sure if its necessary, but this script is an unmodified `build barn` docker compose setup. It works on my machine 🤷‍♂️

```
cd REPO/bb-deployments/docker-compose
./run.sh
```

## Repro

In a different terminal to the one you have buildbarn RBE running.

```
bazel build \
  --config=remote-ubuntu-22-04 \
  --platforms=//tools/remote-toolchains:ubuntu-act-22-04-platform \
  //repro:foobar
```

You should see an error:

```
⋊> ~/w/rules_python_rbe_exec_exploration on main ◦ bazel build \                                                                          13:28:46
                                                         --config=remote-ubuntu-22-04 \
                                                         --platforms=//tools/remote-toolchains:ubuntu-act-22-04-platform \
                                                         //repro:foobar
INFO: Invocation ID: 38b164a9-99d8-4542-81a8-f2d8b1e6e3e2
INFO: Analyzed target //repro:foobar (0 packages loaded, 0 targets configured).
ERROR: /Users/groodt/work/rules_python_rbe_exec_exploration/repro/BUILD.bazel:3:4: Action repro/foobar failed: (Exit 1): foo_tool failed: error executing Action command (from target //repro:foobar) bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool bazel-out/darwin_x86_64-fastbuild/bin/repro/foobar
Action details (uncached result): http://localhost:7984/fuse/blobs/sha256/historical_execute_response/b4dcd7b6ca2e50dafdebafb59d68e810abbd1714a46ecbfef08c94baafb901f8-901/
Traceback (most recent call last):
  File "/worker/build/63f1c63798dc7288/root/bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool.runfiles/_main/../rules_foo~/private/foo_tool.py", line 12, in <module>
    class MyModel(pydantic.BaseModel):
  File "/worker/build/63f1c63798dc7288/root/bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool.runfiles/rules_python~~pip~pypi_310_pydantic/site-packages/pydantic/__init__.py", line 395, in __getattr__
    module = import_module(module_name, package=package)
  File "/worker/build/63f1c63798dc7288/root/bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool.runfiles/rules_python~~python~python_3_10_x86_64-unknown-linux-gnu/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/worker/build/63f1c63798dc7288/root/bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool.runfiles/rules_python~~pip~pypi_310_pydantic/site-packages/pydantic/main.py", line 12, in <module>
    import pydantic_core
  File "/worker/build/63f1c63798dc7288/root/bazel-out/darwin_x86_64-opt-exec-ST-7d61c53ce9b9/bin/external/rules_foo~/private/foo_tool.runfiles/rules_python~~pip~pypi_310_pydantic_core/site-packages/pydantic_core/__init__.py", line 6, in <module>
    from ._pydantic_core import (
ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'
Target //repro:foobar failed to build
Use --verbose_failures to see the command lines of failed build steps.
INFO: Elapsed time: 2.033s, Critical Path: 0.92s
INFO: 2 processes: 2 internal.
ERROR: Build did NOT complete successfully
```

