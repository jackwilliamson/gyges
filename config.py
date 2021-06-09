import os

class NoMatch(Exception):
    pass

class Config:
    def __init__(self, rules=list([])):
        self.rules = rules

    def match_file(self, file):
        for rule in self.rules:
            if rule.match(file):
                return rule.get_chest(file)

        raise NoMatch()


