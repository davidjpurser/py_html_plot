import html


class Page:
    """
    A class to create a web page with a specified HTML tag and adds CSS styles.
    """

    def __init__(self,tag = 'div'):
        self.tag = tag
        with open('lib.css', 'r') as file:
            css = file.read()
            style = html.HTML('style')
            style.text = css
        self.obj = html.HTML(tag)
        self.obj.add_child(style)
        
    def add_object(self, obj):
        self.obj.add_child(obj)

    def get_html(self):
        return self.obj 

    def render(self):
        return self.obj.render()