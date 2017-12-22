# extract_empirical_results

Extract empirical results from abstracts of computer science papers!

## Installation

This project requires **Python 3.6**.

You can clone the repo via:

```
git clone https://github.com/allenai/extract_empirical_results.git
```

You can install all the **dependencies** via:

```
pip install -r requirements.txt
```

You'll also need **PDFLib's TET toolkit v5.1** for parsing PDFs.  You'll need to provide the path to the binary executable `bin/tet` after downloading/extracting.

You can run all the **tests** via:

```
cd extract_empirical_results
nosetests tests
```

## Projects

- [data_generator](#data_generator)
- [extraction_model](#extraction_model)

