def f1_score_implementation(tp, fp, fn):
    '''
    this functions aims to evaluate classification model using F1-score
    this functions has 3 input: tp is true positive, fp is false positive and fn is false negative.
    this functions print precision, recall and calculate F1-score by harmonic mean.
    '''

    # kiểm tra giá trị nhận vào là type int hay không, sử dụng isinstance.
    if isinstance(tp, int) == False:
        return "tp must be int"
    elif isinstance(fp, int) == False:
        return "fp must be int"
    elif isinstance(fn, int) == False:
        return "fn must be int"

    # kiểm tra tp, fp, fn > 0.
    if tp <= 0 or fp <= 0 or fn <= 0:
        return "tp and fp and fn must be greater than zero"

    # tính toán các giá trị precision, recall và f1-score
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*precision*recall/(precision+recall)

    print(f"""precision is: {precision}
          recall is: {recall}
          F1-score is {f1_score}""")


if __name__ == "__main__":
    print(f1_score_implementation(tp=2.1, fp=3, fn='a'))
