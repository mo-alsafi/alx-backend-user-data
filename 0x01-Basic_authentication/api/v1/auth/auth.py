#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return f"{False} {path}"

    def authorization_header(self, request=None) -> str:
        if request == None:
            return None
        return f"{None} {request}"

    def current_user(self, request=None) -> TypeVar('User'):
        if request == None:
            return None
        return f"{None} {request}"