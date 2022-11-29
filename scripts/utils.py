from pathlib import Path

import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)


def root_dir():
    return Path(__file__).parent.parent


def load_citation(citation_file):
    with open(citation_file, "r", encoding="utf8") as input_file:
        return yaml.load(input_file)


def write_citation(citation_file, citation):
    with open(citation_file, "w", encoding="utf8") as output_file:
        return yaml.dump(citation, output_file)