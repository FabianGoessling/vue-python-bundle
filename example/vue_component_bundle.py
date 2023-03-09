import os
import re
from typing import List, Optional

from pydantic import BaseModel, root_validator, validator


class VueComponent(BaseModel):
    file_name: str
    name: Optional[str]
    path: str
    props: Optional[str]
    data: Optional[str]
    template: Optional[str]

    @validator("name", always=True)
    def set_name(cls, v, values):
        return values["file_name"].rstrip(".vue")

    @root_validator(pre=False)
    def load_single_file_component(cls, values):
        with open(f"./{values['path']}/{values['file_name']}", "r") as f:
            data = f.read().splitlines()
        stripped = "".join([dat.lstrip().rstrip() for dat in data])

        out = re.search(
            (
                r"<script>\s*export\s+default\s*{\s*props:\s*\[(?P<props>.*?)\],"
                r"\s*data\(\)\s*{\s*return\s*{(?P<data>.*?)};\s*},\s*};\s*</script>\s*"
                r"<template>(?P<template>.*?)</template>\s*<style>(?P<style>.*?)</style>"
                ),
            stripped,
        )

        values["data"] = f"(function () {{ return {{ {out.group('data')} }} }})"
        values["template"] = out.group("template")
        values["props"] = f'[ {out.group("props")} ]'
        values["style"] = out.group("style")
        return values


class VueComponentBundle(BaseModel):
    path: str = "components"
    components: Optional[List[VueComponent]]

    @validator("components", always=True)
    def load_components(cls, v, values):
        files = os.listdir(f"./{values['path']}")
        return [VueComponent(file_name=file_name, path=values["path"]) for file_name in files] # type: ignore
