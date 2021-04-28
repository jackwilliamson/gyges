class Matcher:

    def match(self, file):
        pass

class DefaultMatcher(Matcher):

    def match(self, file):
        return True

class ContainsMatcher(Matcher):

    def match(self, file):
        pass

class ExtensionMatcher(Matcher):

    def __init__(self, exts=list([])):
        self.exts = exts

    def match(self, file):
        return file.ext in self.exts

class ImageMatcher(ExtensionMatcher):

    def __init__(self):
        allowed_exts = ['jpg', 'jpeg', 'png', 'pdf']
        super().__init__(allowed_exts)
