from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

def classify(logs):
    labels=[]
    for source,log in logs:
        label=classify_log(source,log)
        labels.append(label)
    return labels

def classify_log(source,log):
    if source=="LegacyCRM":
       label=classify_with_llm(log)
    else:
        label=classify_with_regex(log)
        if not label:
            label=classify_with_bert(log)
    return label

def classify_csv(input_file):
    import pandas as pd
    df = pd.read_csv(input_file)

    df["target_label"]=classify(list(zip(df["source"],df["log_message"])))
    output_file="output.csv"
    df.to_csv(output_file,index=False)
    return output_file
if __name__=="__main__":
     classify_csv("resources/test_classify.csv")