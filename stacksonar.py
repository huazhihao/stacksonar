#!/usr/bin/env python

import os
import re
import argparse

from jinja2 import Environment, FileSystemLoader

DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_TEMPLATE = 'index_template.html'

def run_pysonar(src_root, html_root="./html"):
    os.system('java -jar pysonar-2.1.jar "%s" "%s"' % (src_root, html_root))


def gen_log_html(log_path, src_root, html_root="./html"):
    with open(log_path) as log_file:
        lines = log_file.readlines()

    for i in xrange(len(lines)):
        line = lines[i]
        # Trim terminal colors
        line = re.sub(u"\\x1b\[\d{1,3}(;\d{1,3})?m", "", line)
        # TODO: logging_exception_prefix logging_debug_format_suffix
        #       logging_default_format_string logging_context_format_string
        repl = u'<a href="\g<2>#L\g<3>" target="stack">\g<2>:\g<3></a>'
        line = re.sub("("+src_root + u")([^:]+\.py):(\d+)", repl, line)
        lines[i] = line

    env = Environment(loader=FileSystemLoader(DIR))
    template = env.get_template(INDEX_TEMPLATE)
    html_index = os.path.join(html_root, 'index.html')
    template.stream(lines=lines).dump(html_index)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "./stacksonar /opt/stack/nova/ /opt/stack/logs/n-cpu.log")
    parser.add_argument("src")
    parser.add_argument("log")

    args = parser.parse_args()

    run_pysonar(args.src)
    gen_log_html(args.log, args.src)
