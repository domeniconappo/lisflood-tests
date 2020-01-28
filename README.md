# Lisflood Test

This repository hosts pytest code to compare netCDF and TSS results produced by a given lisflood version 
with reference data.
It's also possible to compare existing results, without running a simulation.  

## Options

| Option           | Type         | Description                                |
| -----------------|--------------|--------------------------------------------|
| -P, --python     | Path/String  | Path to python binary                      |
| -L, --lisflood   | Path/String  | Path to lisf1.py script                    |
| -R, --pathroot   | Path/String  | Path to Lisflood data                      |
| -S, --pathstatic | Path/String  | Path to Lisflood static data (e.g. maps)   |
| -M, --pathmeteo  | Path/String  | Path to Lisflood meteo forcings            |
| -I, --pathinit   | Path/String  | Path to Lisflood init data                 |
| -O, --pathout    | Path/String  | Path to results for the version under test |
| -X, --reference  | Path/String  | Path to Lisflood oracle data               |
| -T, --runtype    | String       | Type of test to execute: see table below   |
| -Q, --smallwindow| String       | If passed, run short simulation (1 month)  |

| Runtype option    | Description                     | Simulation length  |
|:-----------------:|---------------------------------|--------------------|
| ECD               | EFAS Cold start Daily           |2,5 years / 1 month |
| EC6               | EFAS Cold start 6 hourly        |1,5 years / 1 month |
| EWD               | EFAS Warm start Daily           |                    |
| EW6               | EFAS Warm start 6 hourl         |                    |
| GCD               | GLOFAS Cold Start Daily         |1 year / 1 month    |
| GWD               | GLOFAS Warm start Daily         |                    |


## Example 1

Run a short (1 month) EFAS 6 hourly simulation with python3 for a given LISFLOOD version (version identified by commit da0c9aa36b117959ed14a52fba1fce532aaf0a57) 
and compare reference data saved in /workarea/lf_results/reference/EFAS/out_6hourly_1month

```bash
PYTHONPATH=/opt/pcraster36/python && pytest listests/test_results.py \
    -L /workarea/lisflood_versions/14_da0c9aa3/lisflood-code-da0c9aa36b117959ed14a52fba1fce532aaf0a57/src/lisf1.py \ 
    -R /workarea/EFAS/ \
    -M /workarea/EFAS/EFAS_forcings/6hourly \
    -O /workarea/lf_results/14_da0c9aa3/6hourly \
    -P /workarea/virtualenvs/lisflood36/bin/python \
    -I /workarea/lf_results/reference/EFAS/InitSafe/ \
    -X /workarea/lf_results/reference/EFAS/out_6hourly_1month \
    -T EC6 \
    -Q \
    --show-capture=no -s
```

## Example 2

Compare results between /workarea/lf_results/14_da0c9aa3/out and /workarea/lf_results/reference/EFAS/out

```bash
pytest listests/test_results.py -O /workarea/lf_results/14_da0c9aa3/out -X /workarea/lf_results/reference/EFAS/out 
```

## Example 3

Run a long (1.5y) GLOFAS simulation and compare results with reference data as saved in /workarea/lf_results/reference/GLOFAS/out_daily

```bash
PYTHONPATH=/opt/pcraster36/python && pytest listests/test_results.py \ 
    -L /workarea/lisflood_versions/14_da0c9aa3/lisflood-code-da0c9aa36b117959ed14a52fba1fce532aaf0a57/src/lisf1.py \ 
    -R /workarea/GLOFAS/ \
    -M /workarea/GLOFAS/GLOFAS_forcings/ \
    -O /workarea/lf_results/14_da0c9aa3/glofas \
    -P /workarea/virtualenvs/lisflood36/bin/python \
    -I /workarea/GLOFAS/init \
    -X /workarea/lf_results/reference/GLOFAS/out_daily \ 
    -T GCD \
    --show-capture=no -s
```
