from argparse import ArgumentParser

class GygesArgsParser(ArgumentParser):

    def __init__(self):
        super().__init__()

        self.add_argument(
            'hopper',
            type=str
        )

        self.add_argument(
            '--config',
            type=str,
            default='gyges_config.yml'
        )

        self.add_argument(
            '--watch',
            action='store_true',
            help='Continue watching for additional files'
        )
