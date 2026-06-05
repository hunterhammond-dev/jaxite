# Bazel helpers for jaxite

load("//tools/build_defs/testing:bzl_library.bzl", "bzl_library")

package(
    default_applicable_licenses = ["@jaxite//:license"],
    default_visibility = ["//visibility:public"],
)

bzl_library(
    name = "test_bzl",
    srcs = ["test.bzl"],
    parse_tests = False,
    visibility = ["//visibility:private"],
    deps = [
        "//devtools/build_cleaner/skylark:build_defs_lib",
        "//devtools/python/blaze:pytype_bzl",
        "//third_party/bazel_rules/rules_python/python:py_test_bzl",
        "//third_party/bazel_skylib/lib:sets",
        "//third_party/tensorflow:tensorflow_bzl",
    ],
)

bzl_library(
    name = "test_oss_bzl",
    srcs = ["test_oss.bzl"],
    parse_tests = False,
    visibility = ["//visibility:private"],
    deps = ["//third_party/bazel_rules/rules_python/python:py_test_bzl"],
)
