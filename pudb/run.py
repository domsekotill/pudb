from __future__ import absolute_import, division, print_function

import sys
import argparse
import importlib
from os import path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--steal-output', '-s',
        action='store_true',
    )
    parser.add_argument('--pre-run',
        metavar='COMMAND', default='',
        help="Run command before each program run",
    )
    run_group = parser.add_mutually_exclusive_group()
    run_group.add_argument('--module', '-m',
        help="Run MODULE as a script",
    )
    run_group.add_argument('script',
        nargs='?',
        help="Run SCRIPT"
    )
    parser.add_argument('arguments', nargs='*')

    options = parser.parse_args()

    from pudb import runscript
    runscript(options.module or options.script,
            as_module=bool(options.module),
            args=options.arguments,
            pre_run=options.pre_run,
            steal_output=options.steal_output)


if __name__ == '__main__':
    main()

# vim: foldmethod=marker:expandtab:softtabstop=4
