# metlink-status
CLI tool for checking Metlink Wellington service updates.

![Example Output Screenshot](https://raw.githubusercontent.com/finncodes/metlink-status/master/docs/example_output.png "Example Output")

## Installation
```shell script
python setup.py install
```

## Usage
```
usage: metlink-status [-h] [-b BUS] [-t TRAIN]

Prints Metlink service updates

optional arguments:
  -h, --help            show this help message and exit
  -b BUS, --bus BUS     Specifies a bus route
  -t TRAIN, --train TRAIN
                        Specifies a train line
```

## Examples

- To show all service updates:
    ```shell script
    metlink-status
    ```

- To show any service updates for the number 2 bus:
    ```shell script
    metlink-status -b 2
    ```
    or
    ```shell script
    metlink-status --bus 2
    ```

- To show any service updates for the KPL (Kapiti) train line:
    ```shell script
    metlink-status -t KPL
    ```
    or
    ```shell script
    metlink-status --train KPL
    ```