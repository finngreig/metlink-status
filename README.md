# metlink-status
CLI tool for checking Metlink Wellington service updates.

![Example Output Screenshot](https://git.sr.ht/~finncodes/metlink-status/blob/master/docs/example_output.png)

## Installation
```shell script
python setup.py install
```

## Usage
```
usage: metlink-status-runner.py [-h] [-b BUS] [-t TRAIN] [-s STOP]

Prints Metlink service updates

optional arguments:
  -h, --help            show this help message and exit
  -b BUS, --bus BUS     Specifies a bus route
  -t TRAIN, --train TRAIN
                        Specifies a train line
  -s STOP, --stop STOP  Specifies a stop or station
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

- To show service updates for all services and departures for stop 1234:
  ```shell script
  metlink-status -s 1234
  ```
  or
  ```shell script
  metlink-status --stop 1234
  ```

- To show service updates and departures at stop 1234 for the number 2 bus:
  ```shell script
  metlink-status -b 2 -s 1234
  ```
  or
  ```shell script
  metlink-status --bus 2 --stop 1234
  ```

- To show service updates and departures at WELL (Wellington Station) for the KPL (Kapiti) train line:
  ```shell script
  metlink-status -t KPL -s WELL
  ```
  or
  ```shell script
  metlink-status --train KPL --stop WELL
  ```