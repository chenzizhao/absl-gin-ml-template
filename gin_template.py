from absl import flags
import gin

_GIN_FILE = flags.DEFINE_multi_string(
    'gin_file', None, 'List of paths to the config files.')
_GIN_BINDINGS = flags.DEFINE_multi_string(
    'gin_param', None, 'Newline separated list of Gin parameter bindings.')


def parse_and_log_config():
    gin.parse_config_files_and_bindings(
        _GIN_FILE.value, _GIN_BINDINGS.value, print_includes_and_imports=True)
    print(gin.operative_config_str())
    return
