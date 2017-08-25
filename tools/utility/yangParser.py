# -*- coding: utf-8 -*-
"""Utility belt for working with ``pyang`` and ``pyangext``."""
import codecs
import io
from os.path import isfile

from pyang import Context, FileRepository
from pyang.error import error_codes
from pyang.yang_parser import YangParser

__all__ = [
    'create_context',
    'compare_prefixed',
    'qualify_str',
    'select',
    'find',
    'dump',
    'check',
    'parse',
    'walk',
]

#logging.basicConfig(level=logging.INFO)
#logging.captureWarnings(True)
#LOGGER = logging.getLogger(__name__)

DEFAULT_OPTIONS = {
    'path': [],
    'deviations': [],
    'features': [],
    'format': 'yang',
    'keep_comments': True,
    'no_path_recurse': False,
    'trim_yin': False,
    'yang_canonical': False,
    'yang_remove_unused_imports': False,
    # -- errors
    'ignore_error_tags': [],
    'ignore_errors': [],
    'list_errors': True,
    'print_error_code': False,
    'errors': [],
    'warnings': [code for code, desc in error_codes.items() if desc[0] > 4],
    'verbose': True,
}
"""Default options for pyang command line"""

_COPY_OPTIONS = [
    'canonical',
    'max_line_len',
    'max_identifier_len',
    'trim_yin',
    'lax_xpath_checks',
    'strict',
]
"""copy options to pyang context options"""


class objectify(object):  # pylint: disable=invalid-name
    """Utility for providing object access syntax (.attr) to dicts"""

    def __init__(self, *args, **kwargs):
        for entry in args:
            self.__dict__.update(entry)

        self.__dict__.update(kwargs)

    def __getattr__(self, _):
        return None

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value


def _parse_features_string(feature_str):
    if feature_str.find(':') == -1:
        return (feature_str, [])

    [module_name, rest] = feature_str.split(':', 1)
    if rest == '':
        return (module_name, [])

    features = rest.split(',')
    return (module_name, features)


def create_context(path='.', *options, **kwargs):
    """Generates a pyang context.

    The dict options and keyword arguments are similar to the command
    line options for ``pyang``. For ``plugindir`` use env var
    ``PYANG_PLUGINPATH``. For ``path`` option use the argument with the
    same name, or ``PYANG_MODPATH`` env var.

    Arguments:
        path (str): location of YANG modules.
            (Join string with ``os.pathsep`` for multiple locations).
            Default is the current working dir.
        *options: list of dicts, with options to be passed to context.
            See bellow.
        **kwargs: similar to ``options`` but have a higher precedence.
            See bellow.

    Keyword Arguments:
        print_error_code (bool): On errors, print the error code instead
            of the error message. Default ``False``.
        warnings (list): If contains ``error``, treat all warnings
            as errors, except any other error code in the list.
            If contains ``none``, do not report any warning.
        errors (list): Treat each error code container as an error.
        ignore_error_tags (list): Ignore error code.
            (For a list of error codes see ``pyang --list-errors``).
        ignore_errors (bool): Ignore all errors. Default ``False``.
        canonical (bool): Validate the module(s) according to the
            canonical YANG order. Default ``False``.
        yang_canonical (bool): Print YANG statements according to the
            canonical order. Default ``False``.
        yang_remove_unused_imports (bool): Remove unused import statements
            when printing YANG. Default ``False``.
        trim_yin (bool): In YIN input modules, trim whitespace
            in textual arguments. Default ``False``.
        lax_xpath_checks (bool): Lax check of XPath expressions.
            Default ``False``.
        strict (bool): Force strict YANG compliance. Default ``False``.
        max_line_len (int): Maximum line length allowed. Disabled by default.
        max_identifier_len (int): Maximum identifier length allowed.
            Disabled by default.
        features (list): Features to support, default all.
            Format ``<modname>:[<feature>,]*``.
        keep_comments (bool): Do not discard comments. Default ``True``.
        no_path_recurse (bool): Do not recurse into directories
            in the yang path. Default ``False``.

    Returns:
        pyang.Context: Context object for ``pyang`` usage
    """
    # deviations (list): Deviation module (NOT CURRENTLY WORKING).

    opts = objectify(DEFAULT_OPTIONS, *options, **kwargs)
    repo = FileRepository(path, no_path_recurse=opts.no_path_recurse)

    ctx = Context(repo)
    ctx.opts = opts

    for attr in _COPY_OPTIONS:
        setattr(ctx, attr, getattr(opts, attr))

    # make a map of features to support, per module (taken from pyang bin)
    for feature_name in opts.features:
        (module_name, features) = _parse_features_string(feature_name)
        ctx.features[module_name] = features

    # apply deviations (taken from pyang bin)
    for file_name in opts.deviations:
        with io.open(file_name, "r", encoding="utf-8") as fd:
            module = ctx.add_module(file_name, fd.read())
            if module is not None:
                ctx.deviation_modules.append(module)

    return ctx


def parse(text, ctx=None):
    """Parse a YANG statement into an Abstract Syntax subtree.

    Arguments:
        text (str): file name for a YANG module or text
        ctx (optional pyang.Context): context used to validate text

    Returns:
        pyang.statements.Statement: Abstract syntax subtree

    Note:
        The ``parse`` function can be used to parse small amounts of text.
        If yout plan to parse an entire YANG (sub)module, please use instead::

            ast = ctx.add_module(module_name, text_contet)

        It is also well known that ``parse`` function cannot solve
        YANG deviations yet.
    """
    parser = YangParser()

    filename = 'parser-input'

    ctx_ = ctx or create_context()

    if isfile(text):
        filename = text
        text = codecs.open(filename, encoding="utf-8").read()
        #with open(filename, 'r') as fp:
        #    text = fp.read()

    # ensure reported errors are just from parsing
    # old_errors = ctx_.errors
    ctx_.errors = []

    ast = parser.parse(ctx_, filename, text)

    return ast
