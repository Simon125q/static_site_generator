from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str | None = None, children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None) -> None:
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("Tag not provided")

        if self.children == None or self.children == []:
            raise ValueError("No child nodes provided")

        result = "<" + self.tag + ">"
        for child in self.children:
            result += child.to_html()

        result += "</" + self.tag + ">"

        return result
            
