#!/usr/bin/python3

import pandas as pd
from collections import defaultdict


def main():
    df = pd.read_csv('29847_HF_PROCS.csv')

    dict_procedure = defaultdict(list)

    for idx, row in df.iterrows():
        procedure_report = str(df['procedure_report'][idx])
        
        if 'IMPRESSION:' in procedure_report:
            finding = str(procedure_report.split('IMPRESSION:')[0])
            impression = str(procedure_report.split('IMPRESSION:')[1])
            record_id = df['record_id'][idx]
            procedure_name = df['procedure_name'][idx]
        
            dict_procedure['record_id'].append(record_id)
            dict_procedure['procedure_name'].append(procedure_name)
            dict_procedure['finding'].append(finding)
            dict_procedure['impression'].append(impression)

    df_final = pd.DataFrame(dict_procedure)

    df_final.to_csv("heart_failure_procedures.csv", index=False)

    print(df_final.head())

if __name__ == "__main__":
    main()
