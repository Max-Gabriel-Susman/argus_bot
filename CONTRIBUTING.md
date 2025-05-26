<!--
Copyright (c) 2025, Max Gabriel Susman
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->


# Contributing to **Argus Bot**

:tada: **Thanks for helping make Argus Bot better!** This document explains the ground rules for reporting issues, suggesting new features, and submitting code or documentation changes.

---

## 1. Ways to Contribute

| How | When to use it |
|-----|----------------|
| **Open an Issue** | • bug reports<br>• feature requests<br>• design questions |
| **Submit a Pull Request (PR)** | • code / URDF / launch files<br>• docs & tutorials<br>• CI or tooling improvements |
| **Review a PR** | • give feedback, request changes, or 👍 approvals |

> **Please search existing issues and PRs first** to avoid duplicates.

---

## 2. Prerequisites

| Requirement | Version / Notes |
|-------------|-----------------|
| Ubuntu | 20.04 LTS (tested) |
| ROS 2 | Foxy Fitzroy |
| Gazebo | Classic (gazebo11) |
| Other APT deps | `ros-foxy-xacro`, `ros-foxy-joint-state-publisher-gui`, `ros-foxy-gazebo-ros-pkgs` |
| Python | 3.8+ (comes with Foxy) |
| CLI tools | `colcon`, `rosdep`, `git`, `clang-format` |

A Docker dev container is planned (see [#15](../issues/15)).

---

## 3. Local Development Set-up

```bash
# one-time
sudo apt update && sudo apt install python3-colcon-ros ros-foxy-rosdep
sudo rosdep init             # if you haven’t already
rosdep update

# workspace
mkdir -p ~/dev_ws/src && cd ~/dev_ws/src
git clone https://github.com/Max-Gabriel-Susman/argus_bot
cd ..
rosdep install --from-paths src -yi --rosdistro foxy --ignore-src
colcon build --symlink-install
source install/setup.bash
