
class HTML:

    def __init__(self, type):
        self.type = type
        self.attr = {}
        self.style = {}
        self.children = []
        self.classes = []
        self.text = ''
        self.self_closing = False

    def set_attr(self, key, value):
        self.attr[key] = value
    
    def set_style(self, key, value):
        self.style[key] = value

    def add_class(self, class_name):
        if class_name not in self.classes:
            self.classes.append(class_name)
            self.attr['class'] = ' '.join(self.classes)

    def set_text(self, text):
        self.text = text

    def add_child(self, child):
        if isinstance(child, HTML):
            self.children.append(child)
        else:
            self.text += str(child)

    def render(self):
        attr_str = ' '.join([f'{key}="{value}"' for key, value in self.attr.items()])
        style_str = '; '.join([f'{key}: {value}' for key, value in self.style.items()])
        if style_str:
            attr_str += f' style="{style_str}"'
        if self.self_closing:
            return f'<{self.type} {attr_str}/>'
        else:
            children_str = '\n'.join([child.render() if isinstance(child, HTML) else child for child in self.children])
            return f'<{self.type} {attr_str}>{self.text}{children_str}</{self.type}>'