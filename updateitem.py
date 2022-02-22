class UpdateItem:

    def __init__(self, new_item, old_item):
        self.new_item = new_item
        self.old_item = old_item

    def is_update(self):
        return self.new_item.__dict__ == self.old_item.__dict__

    def look_changes(self):
        keys = []
        if not self.is_update():
            for key in self.new_item.__dict__:
                if self.new_item.__dict__[key] != self.old_item.__dict__[key]:
                    keys.append(key)
        return keys

    def update(self):
        keys = self.look_changes()
        if keys:
            for key in keys:
                self.old_item.__setattr__(key, self.new_item.__dict__[key])
        return self.old_item