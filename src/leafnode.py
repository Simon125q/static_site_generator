from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str | None = None,
                 props: dict[str, str] | None = None) -> None:
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("All leaf nodes require value")

        if self.tag == None and self.props != None:
            raise ValueError("Raw text cant have properties")
        elif self.tag == None:
            return self.value

        return "<" + self.tag + self.props_to_html() + ">" + \
            self.value + "</" + self.tag + ">"




