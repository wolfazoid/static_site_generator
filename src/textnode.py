from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node_1, text_node_2):
        if text_node_1 == text_node_2:
            return True
    
    def __repr__(self):
        return str(f'TextNode({self.text}, {self.text_type.value}, {self.url})')