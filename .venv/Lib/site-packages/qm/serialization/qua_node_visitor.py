from typing import Literal, Optional, cast

import betterproto

from qm.utils import list_fields
from qm.program.program import Program
from qm.utils.protobuf_utils import Node


class QuaNodeVisitor:
    def _default_enter(self, node: Node) -> bool:
        return True

    def _default_leave(self, node: Node) -> None:
        return

    def _default_visit(self, node: Node) -> None:
        for field in list_fields(node).values():
            self.__visit(field)

    def __call(self, name: str, node: Node, t: Literal["enter", "visit", "leave"]) -> Optional[bool]:
        attr_name = f"{t}_{name}".replace(".", "_")
        attr = getattr(self, attr_name, None)
        if attr:
            ret = attr(node)
            if t == "enter":
                return cast(bool, ret)
            return None
        elif t == "enter":
            return self._default_enter(node)
        elif t == "leave":
            self._default_leave(node)
            return None
        elif t == "visit":
            self._default_visit(node)
            return None
        raise Exception(f"unknown call type {t}. only 'enter', 'leave' or 'visit' are supported")

    def __call_enter(self, name: str, node: Node) -> bool:
        return cast(bool, self.__call(name, node, "enter"))

    def __call_visit(self, name: str, node: Node) -> None:
        self.__call(name, node, "visit")

    def __call_leave(self, name: str, node: Node) -> None:
        self.__call(name, node, "leave")

    def visit(self, node: Node) -> None:
        if isinstance(node, Program):
            return self.visit(node._program)

        if isinstance(node, betterproto.Message):
            self.__visit(node)
        else:
            raise Exception(f"Failed to find descriptor on {node}")

    def __visit(self, node: Node) -> None:
        if isinstance(node, betterproto.Message):
            self._enter_visit_leave(node)
        elif isinstance(node, list):
            for n in node:
                self.__visit(n)

    def _enter_visit_leave(self, node: Node) -> None:
        type_fullname = f"{type(node).__module__}.{type(node).__name__}"
        if self.__call_enter(type_fullname, node):
            self.__call_visit(type_fullname, node)
        self.__call_leave(type_fullname, node)
