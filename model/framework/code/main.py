import os
import csv
import sys
import re
import numpy as np
from rdkit import Chem
from ersilia_pack_utils.core import read_smiles, write_out

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
smarts_file = os.path.join(root, "NTD.txt")


def _sanitize_name(name):
    name = name.lower()
    name = name.replace("> ", "more_than_")
    name = re.sub(r"[^a-z0-9\s_]", "_", name)
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"_+", "_", name)
    return name.strip("_")


def _load_patterns(path):
    # two-pass: first collect raw sanitized names to find duplicates
    raw = []
    smarts_rows = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)
        for row in reader:
            raw.append(_sanitize_name(row[0].strip()))
            smarts_rows.append(row[1].strip())

    from collections import Counter
    counts = Counter(raw)
    seen = {}
    patterns = []
    for base_name, smarts_str in zip(raw, smarts_rows):
        if counts[base_name] > 1:
            seen[base_name] = seen.get(base_name, 0) + 1
            col_name = base_name + "_" + chr(96 + seen[base_name])
        else:
            col_name = base_name
        mol_patt = Chem.MolFromSmarts(smarts_str)
        patterns.append((col_name, mol_patt))
    return patterns


patterns = _load_patterns(smarts_file)
headers = [name for name, _ in patterns] + ["n_hits"]
empty_output = [None] * len(patterns) + [None]


def my_model(smiles_list):
    results = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            results.append(empty_output)
            continue
        row = [
            1 if patt is not None and mol.HasSubstructMatch(patt) else 0
            for _, patt in patterns
        ]
        results.append(row + [sum(row)])
    return results


_, smiles_list = read_smiles(input_file)
outputs = my_model(smiles_list)

assert len(smiles_list) == len(outputs)

write_out(outputs, headers, output_file, np.float32)
