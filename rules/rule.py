from config import Config, NoMatch

class Rule:
    def __init__(self):
        self.matcher = None
        self.chest = None
        self.inner_config = None

    def has_inner_config(self):
        return self.inner_config is None

    def set_inner_config(self, inner_config):
        self.inner_config = inner_config

    def match(self, file):
        return self.matcher.match(file)

    def get_chest(self, file):
        if self.inner_config is not None:
            try:
                self.inner_config.match_file(file)
            except NoMatch:
                pass

