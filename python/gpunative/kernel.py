# Copyright 2026 Yeongu Choe
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

__all__ = ["kernel"]


class kernel:
    def __init__(self, func):
        self.func = func

    def __getitem__(self, config):
        match config:
            case (gridDim, blockDim):
                print("success")
            case (gridDim, blockDim, sharedMem):
                print("success")
            case (gridDim, blockDim, sharedMem, stream):
                print("success")
            case _:
                print("failure")

        def launch(*args):
            print(args)

        return launch
