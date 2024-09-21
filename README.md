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

There is an expectation that this command should fail. However, it appears to succeed. I am probably misunderstanding the problem (very likely).
