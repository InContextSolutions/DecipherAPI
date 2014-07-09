#Decipher

[![Build Status](https://api.shippable.com/projects/53bd62bb728a8df803885803/badge/master)](https://www.shippable.com/projects/53bd62bb728a8df803885803)

Python client for [Decipher](https://www.decipherinc.com) data and survey list API.

## Installation

    git clone git@github.com:InContextSolutions/Decipher.git
    cd Decipher
    pip install .

## Usage

### Create a client

Creating a client requires your decipher username and password.

```python
from decipher.client import Client
c = Client('you@example.org', 'Pa$$w0rd123')
```

By default, the client refers to the `v2.decipherinc.com/api` host. Alternate hosts can be specified in the constructor:

```python
c = Client('you@example.org', 'Pa$$w0rd123', host='custom.decipherinc.com/api')
```

All hosts are assumed to be over SSL (`https`).

### Retrieve list of available surveys

You can retrieve a list of all surveys in three formats:

- `json`: JavaScript Object Notation
- `csv`: comma-separated values
- `tsv`: tab-separated values

```python
c.list_surveys(fmt='json')
```

### Pull data for a specific survey

```python
c.get_survey(survey, start=None, end=None, status=None, columns=None, filters=None, fmt='json')
```

- `survey` is the full survey path
- `start` and `end` are Python datetimes (assumes UTC)
- `columns` is a list of column names to include in the results
- `filters` is a list of column-specific rules
- As above, `fmt` is the return format and can be `json`, `csv`, or `tsv`

### Command-line interface (CLI)

Included with the installation is a command-line utlity called `decipher` with built-in help:

```shell
$ decipher --help
usage: decipher [-h] -U USERNAME -P PASSWORD [-H HOST] {pull,list} ...

A command-line utility for interacting with the Decipher API. Help is
available on subcommands (e.g. `decipher pull --help`)

optional arguments:
  -h, --help            show this help message and exit
  -U USERNAME, --username USERNAME
                        user identification
  -P PASSWORD, --password PASSWORD
                        user password
  -H HOST, --host HOST  host

valid subcommands:
  {pull,list}
    pull                pull survey data
    list                list surveys
```

#### Get survey data

```shell
$ decipher pull --help
usage: decipher pull [-h] -s SURVEY [-t START] [-T END]
                     [-S {all,partial,complete,qualified,terminated,overquota}]
                     [-c COLUMNS] [-F FILTERS] [-f {json,tsv,csv}]

optional arguments:
  -h, --help            show this help message and exit
  -s SURVEY, --survey SURVEY
                        survey name
  -t START, --start START
                        utc start time: YYYY-MM-DDTHH:MM:SS.mmmmmm
  -T END, --end END     utc end time: YYYY-MM-DDTHH:MM:SS.mmmmmm
  -S {all,partial,complete,qualified,terminated,overquota}, --status {all,partial,complete,qualified,terminated,overquota}
                        survey status
  -c COLUMNS, --columns COLUMNS
                        columns
  -F FILTERS, --filters FILTERS
                        filter conditions
  -f {json,tsv,csv}, --fmt {json,tsv,csv}
                        return format
```

Example:

```shell
$ decipher -U dataapi -P dataapi pull -s 'kbdemo/data' -f csv -S qualified -c uuid,q1 -F 'q1=2'
```

#### Get list of surveys

```shell
$ decipher list --help
usage: decipher list [-h] [-f {json,tsv,csv}]

optional arguments:
  -h, --help            show this help message and exit
  -f {json,tsv,csv}, --fmt {json,tsv,csv}
                        return format
```

Example:

```shell
$ decipher -U dataapi -P dataapi list -f csv
```
