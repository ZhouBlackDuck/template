## Code Template for Deep Learning Model

```text
├── abstracts
│   ├── __init__.py     # Import submodules
│   ├── builder.py      # Abstract dataset builder
│   ├── director.py     # Abstract model dataset director
│   └── model.py        # Abstract model
├── configs
│   └── config.yaml     # Default configuration file
├── datasets
│   ├── builders
│   │   └── __init__.py # Import submodules and produce builder
│   └── __init__.py     # Import submodules and add arguments
├── defaults
│   ├── __init__.py     # Import submodules and produce defaults
│   ├── dataset.py      # Default dataset arguments
│   └── logger.py       # Default logger arguments
├── models
│   ├── directors
│   │   └── __init__.py # Import submodules and produce director
│   └── __init__.py     # Import submodules, add arguments and produce model
├── modules
│   ├── __init__.py     # Import submodules and add arguments
│   ├── logger.py       # Logger module
│   └── parser.py       # Argument parser module
├── typings
│   ├── __init__.py     # Import submodules
│   └── defaults.py     # Types used in defaults
├── utils
│   ├── __init__.py     # Import submodules
│   ├── modules.py      # Module utility functions
│   ├── parser.py       # Argument parser utility functions
│   └── typings.py      # Typings utility functions
├── README.md
├── environment.yaml    # Environment file for conda
├── requirements.txt    # Requirements file for pip
└── main.py             # Main script to run the model
```
