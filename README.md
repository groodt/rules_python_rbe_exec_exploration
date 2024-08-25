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

```
cd REPO/bb-deployments/docker-compose
./run.sh
```

## Repro

```
bazel build \
  --config=remote-ubuntu-22-04 \
  --platforms=//tools/remote-toolchains:ubuntu-act-22-04-platform \
  //repro:foobar
```
