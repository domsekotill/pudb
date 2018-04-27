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

    run_group = parser.add_argument_group(
        title="Run options",
        description="One of the following:"
    )
    run_group.add_argument('--module', '-m',
        help="Run MODULE as a script",
    )
    run_group.add_argument('script',
        nargs='?',
        help="Run SCRIPT"
    )

    arg_group = parser.add_argument_group(title="Run arguments")
    arg_group.add_argument('arguments',
        nargs=argparse.REMAINDER,
        help="Arguments for the script or module",
    )

    options = parser.parse_args()

    if options.module and options.script:
        # `script` is actually the first `arguments`
        options.arguments.insert(0, options.script)
        options.script = None

    from pudb import runscript
    runscript(options.module or options.script,
            as_module=bool(options.module),
            args=options.arguments,
            pre_run=options.pre_run,
            steal_output=options.steal_output)


if __name__ == '__main__':
    main()

# vim: foldmethod=marker:expandtab:softtabstop=4
