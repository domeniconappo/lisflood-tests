# Lisflood Test

This repository hosts pytest code to compare netCDF and TSS results produced by a given lisflood version 
with reference data.
It's also possible to compare existing results, without running a simulation.  

## Options

  * -P PYTHON, --python=PYTHON Path to python binary
  * -L LISFLOOD, --lisflood=LISFLOOD Path to main lisf1.py script
  * -R PATHROOT, --pathroot=PATHROOT Path to Lisflood root directory
  * -S PATHSTATIC, --pathstatic=PATHSTATIC Path to Lisflood static data (e.g. maps)
  * -M PATHMETEO, --pathmeteo=PATHMETEO Path to Lisflood meteo forcings
  * -I PATHINIT, --pathinit=PATHINIT Path to Lisflood init data
  * -O PATHOUT, --pathout=PATHOUT Path to Lisflood results
  * -X REFERENCE, --reference=REFERENCE Path to Lisflood oracle results
  * -T {ECD,EC6,EWD,EW6,GCD,GWD}, --runtype={ECD,EC6,EWD,EW6,GCD,GWD} Test Type: e.g. EC6=EFAS Cold 6hourly run; GWD=GloFAS Warm Daily run
  * -Q, --smallwindow  Pass to run a short test (1 month simulation)


## Example 1

Run a short (1 month) EFAS 6 hourly simulation with python3 for a given LISFLOOD version and compare reference data saved 
in /workarea/lf_results/reference/EFAS/out_6hourly_1month

```bash
PYTHONPATH=/opt/pcraster36/python && pytest listests/test_long_efas_run.py \ 
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
pytest listests/test_long_efas_run.py -O /workarea/lf_results/14_da0c9aa3/out -X /workarea/lf_results/reference/EFAS/out 
