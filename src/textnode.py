from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url):
            return True
        return False
    
    def text_node_to_html(text_node):
        if text_node.text_type == None:
            raise Exception("text type not specified")
        elif text_node.text_type == text_type_text:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == text_type_bold:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == text_type_italic:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == text_type_code:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == text_type_link:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        elif text_node.text_type == text_type_image:
            return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
        else:
            raise Exception(f"Unknown text type: {text_node.text_type}")
        
    
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        text_nodes_list = []
        for node in old_nodes:
            if node.text_type != "text":
                text_nodes_list.append(TextNode(node, node.text_type))
                continue
            elif node.text_type == "text":
                temp_split = node.text.split(delimiter)
                for split_text in temp_split:
                    if temp_split.index(split_text) % 2 == 0:
                        text_nodes_list.append(TextNode(split_text, node.text_type))
                    else:
                        text_nodes_list.append(TextNode(split_text, text_type))
        return text_nodes_list
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"