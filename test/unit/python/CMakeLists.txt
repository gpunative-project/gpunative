# Copyright 2026 Yeongu Choe
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

file(GLOB_RECURSE TestsToRun RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} CONFIGURE_DEPENDS test*.py)

foreach(test ${TestsToRun})
    get_filename_component(TName ${test} NAME_WE)
    add_test(NAME ${TName} COMMAND python3 -m pytest ${CMAKE_CURRENT_LIST_DIR}/${test})
endforeach()

add_custom_target(check-python COMMAND ${CMAKE_CTEST_COMMAND})
