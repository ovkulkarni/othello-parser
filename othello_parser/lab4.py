from argparse import ArgumentParser


class Lab4Parser(ArgumentParser):

    def __init__(self, *args, **kwargs):
        self.default_puzzle = '...........................OX......XO...........................'
        super(Lab4Parser, self).__init__(*args, **kwargs)
        self.add_argument("puzzle", nargs='?', default=self.default_puzzle)
        self.add_argument("human_token", nargs='?', default=self.calc_human(self.default_puzzle))
        self.add_argument("extra", nargs='*')

    def valid_puzzle(self, puzzle):
        return isinstance(puzzle, str) and len(puzzle) == 64

    def valid_player(self, player):
        return player.lower() in {'x', 'o'}

    def calc_player(self, puzzle):
        return ["X", "O"][puzzle.count('.') % 2 == 1]

    def calc_human(self, puzzle):
        return ["o", "x"][puzzle.count('.') % 2 == 1]

    def parse_args(self, args=None, namespace=None):
        args = super(Lab4Parser, self).parse_args(args, namespace)
        set_player = False
        if not self.valid_player(args.human_token):
            args.extra = [args.human_token] + args.extra
            set_player = True
        if not self.valid_puzzle(args.puzzle):
            if not self.valid_player(args.puzzle):
                args.extra = [args.puzzle] + args.extra
            else:
                args.human_token = args.puzzle
                set_player = False
            args.puzzle = self.default_puzzle
        if set_player:
            args.human_token = self.calc_human(args.puzzle)
        if args.human_token.upper() == args.human_token:
            args.next_player = args.human_token
        else:
            args.next_player = self.calc_player(args.puzzle)
        args.human_token = args.human_token.upper()
        args.next_player = args.next_player.upper()
        return args
