PARAMS_SEP = '|'
NESTED_SEP = '--'
ITEMS_SEP = '\n'
BLOCK_SEP = '---'


class MenuItem:
    def __init__(self, text, **params):
        self.text = text
        self.params = params
        self.items = []

    def add_item(self, text, **params):
        new_item = MenuItem(text, **params)
        self.items.append(new_item)
        return new_item

    def add_sep(self):
        self.add_item(BLOCK_SEP)

    def render(self, depth=0):
        rendered_params = PARAMS_SEP.join(f'{k}={v}' for k, v in self.params.items())
        sep1 = ' ' if depth > 0 else ''
        sep2 = PARAMS_SEP if rendered_params else ''
        title = (NESTED_SEP * depth) + sep1 + self.text + sep2 + rendered_params
        sep = ITEMS_SEP if self.items else ''
        return title + sep + ITEMS_SEP.join([item.render(depth + 1) for item in self.items])

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()


class Menu(MenuItem):
    def __init__(self):
        self.items = []

    def render(self):
        return ITEMS_SEP.join([item.render() for item in self.items])
