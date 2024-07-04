from __future__ import annotations

class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None,
            children: list[HTMLNode] | None = None,
            props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        result: str = ""
        for key in self.props.keys():
            result += (' ' + key + '=' + '"' + self.props[key] + '"')
        return result

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"




