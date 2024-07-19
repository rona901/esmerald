from __future__ import annotations

from typing import Type, TypeVar, Union

from esmerald.permissions import BasePermission

PermissionType = TypeVar("PermissionType", bound=BasePermission)
Permission = Union[Type[PermissionType], Type[BasePermission]]
