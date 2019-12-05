```bash
 pytest listests/test_long_efas_run.py \ 
       -L /workarea/lisflood_versions/lf_first_merged/lisf1.py \ 
       -R /workarea/EFAS/ \ 
       -M /workarea/EFAS/EFAS_forcings/ \ 
       -O /workarea/lf_results/1_run 
       -P /workarea/virtualenvs/lisflood27/bin/python \ 
       -I /workarea/lf_results/reference/EFAS/InitSafe/ \ 
       -X /workarea/lf_results/reference/EFAS/out_daily/ -s
```
