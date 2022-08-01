# Modified by TUBITAK BILGEM TUTEL from https://developers.google.com/silicon/guides/digital-inverter-openlane
import pandas as pd
import pathlib

pd.options.display.max_rows = None
final_summary_reports = sorted(pathlib.Path('/home/USERNAME/OpenLane/designs/spm/runs/RUN_2022.08.01_09.48.27').glob('*/metrics.csv'))
df = pd.read_csv(final_summary_reports[-1])
df.transpose()
print(df.transpose())
