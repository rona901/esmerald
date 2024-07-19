from __future__ import annotations

import sys
from inspect import Signature as InspectSignature
from typing import Any, Callable, Mapping


class Signature(InspectSignature):
    """
    A subclass of `InspectSignature` that provides additional functionality for creating signatures from callables.
    """

    @classmethod
    def from_callable(
        cls,
        obj: Callable[..., Any],
        *,
        follow_wrapped: bool = True,
        globals: Mapping[str, Any] | None = None,
        locals: Mapping[str, Any] | None = None,
        eval_str: bool = False,
    ) -> Signature:
        """
        Create a `Signature` object from a callable object.

        Args:
            obj: The callable object from which to create the signature.
            follow_wrapped: Whether to follow wrapped callables to retrieve the signature.
            globals: A mapping of global variables to use during signature evaluation.
            locals: A mapping of local variables to use during signature evaluation.
            eval_str: Whether to evaluate the signature as a string.

        Returns:
            A `Signature` object representing the signature of the callable.

        Raises:
            None.

        Note:
            This method is compatible with Python 3.10 and above. For earlier versions, it falls back to the
            `from_callable` method of the base class `InspectSignature`.
        """
        if sys.version_info < (3, 10):
            return super().from_callable(
                obj,
                follow_wrapped=follow_wrapped,
            )
        return super().from_callable(
            obj, follow_wrapped=follow_wrapped, globals=globals, locals=locals, eval_str=eval_str
        )
