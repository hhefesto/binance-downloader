# This file was made to debug load_data from script.py. It is sort of a rough draft. It is not intended to work with or along script.py.
import numpy as np
import pandas as pd
def load_data(*filenames):
    raw_data = pd.DataFrame()
    for filename in filenames:
        f = filename + ".csv"
        args = ['date_'+filename,
                'open_'+filename,
                'high_'+filename,
                'low_'+filename,
                'close_'+filename,
                'volume_'+filename]
        aux_data = pd.read_csv(f, index_col=0, parse_dates=True,
                               dtype =
                               {args[0]:object,
                                args[1]:float,
                                args[2]:float,
                                args[3]:float,
                                args[4]:float,
                                args[5]:float}
                               , header = 0
                               , usecols = [0,4,5])
        print(aux_data)
        raw_data=raw_data.join(aux_data, how='outer')
        #raw_data = pd.concat([raw_data, aux_data], axis=1, sort=False)
    print(raw_data)
    raw_data = raw_data.values
    print(raw_data)
    for x in range(0, raw_data.shape[0]):
        for y in range(0, raw_data.shape[1]):
            print(raw_data[x][y],"::",type(raw_data[x][y]), end =", ")
            if(np.isnan(raw_data[x][y])):
                raw_data[x][y] = raw_data[x-1][y]
        print()
    print(raw_data)

load_data("ADABTC_PRUEBA", "BTCUSDT_PRUEBA")
