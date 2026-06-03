# NTD chemistry rules

The NTD Rule (Brenk et al., 2008) screens molecules against 105 SMARTS patterns representing unwanted functionalities for neglected tropical disease drug discovery. These include reactive groups (aldehydes, acid halides, Michael acceptors), potentially toxic groups (nitro compounds, heavy metals, polyhalogenated rings), assay-interfering groups (catechols, quinones), and groups with poor ADME properties (long aliphatic chains, perfluorinated chains). Returns a binary flag per substructure and total matched count (n\_hits).

This model was incorporated on 2026-06-02.


## Information
### Identifiers
- **Ersilia Identifier:** `eos7dg4`
- **Slug:** `ntd-rule`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Frequent hitter`, `Neglected tropical disease`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `106`
- **Output Consistency:** `Fixed`
- **Interpretation:** TBinary indicators (1 = substructure present, 0 = absent) and total number of hits (n_hits).

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| more_than_2_ester_groups | integer | high | Presence of unwanted functionality: > 2 ester groups |
| 2_halo_pyridine | integer | high | Presence of unwanted functionality: 2-halo pyridine |
| acid_halide | integer | high | Presence of unwanted functionality: acid halide |
| acyclic_c_c_o | integer | high | Presence of unwanted functionality: acyclic C=C-O |
| acyl_cyanide | integer | high | Presence of unwanted functionality: acyl cyanide |
| acyl_hydrazine | integer | high | Presence of unwanted functionality: acyl hydrazine |
| aldehyde | integer | high | Presence of unwanted functionality: aldehyde |
| aliphatic_long_chain | integer | high | Presence of unwanted functionality: Aliphatic long chain |
| alkyl_halide | integer | high | Presence of unwanted functionality: alkyl halide |
| amidotetrazole | integer | high | Presence of unwanted functionality: amidotetrazole |

_10 of 106 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`

### Resource Consumption


### References
- **Source Code**: [https://github.com/antwiser/ChemFH](https://github.com/antwiser/ChemFH)
- **Publication**: [https://doi.org/10.1002/cmdc.200700139](https://doi.org/10.1002/cmdc.200700139)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2008`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7dg4
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7dg4
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
