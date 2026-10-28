class HTMLNode:

    def __init__(self, tag: str = None, value: str = None, children: list[HTMLNode] = None, props: dict[str, str] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        res = ''
        for atr, val in self.props.items():
            res += f' {atr}=\"{val}\"'
        return res

    def __repr__(self) -> str:
        return f"""
                Tag: {self.tag}
                Value: {self.value}
                Children: {self.children}
                Props: {self.props}
                """

    


