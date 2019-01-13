# From the original file example_evaluator.py by Sharada Mohanty (https://github.com/AICrowd/aicrowd-example-evaluator)
# Adapted to MEDIQA 2019 by Asma Ben Abacha (Accuracy for Tasks 1 and 2) 

import pandas as pd
import numpy as np

class MediqaEvaluator:
  def __init__(self, answer_file_path, round=1):
    """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.
    """
    self.answer_file_path = answer_file_path
    self.round = round

  def _evaluate(self, client_payload, _context={}):
    """
    `client_payload` will be a dict with (atleast) the following keys :
      - submission_file_path : local file path of the submitted file
      - aicrowd_submission_id : A unique id representing the submission
      - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
    """
    submission_file_path = client_payload["submission_file_path"]
    aicrowd_submission_id = client_payload["aicrowd_submission_id"]
    aicrowd_participant_uid = client_payload["aicrowd_participant_id"]
    
    ## 
    col_names = ['pair_id', 'label']

    submission = pd.read_csv(submission_file_path, header=None, names=col_names)
    gold_truth = pd.read_csv(self.answer_file_path, header=None, names=col_names)

    # Drop duplicates except for the first occurrence.
    submission = submission.drop_duplicates(['pair_id'])

    submission.label = submission.label.astype(str)
    gold_truth.label = gold_truth.label.astype(str)

    submission['entry'] = submission.apply(lambda x: '_'.join(x), axis=1)
    gold_truth['entry'] = gold_truth.apply(lambda x: '_'.join(x), axis=1)
    
    s1 = submission[submission['entry'].isin(gold_truth['entry'])]

    accuracy = s1.size / gold_truth.size

    _result_object = {
        "accuracy": accuracy
    }

    return _result_object

if __name__ == "__main__":
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.txt
    answer_file_path = "data/ground_truth.txt"
    _client_payload = {}
    _client_payload["submission_file_path"] = "data/sample_submission.txt"
    _client_payload["aicrowd_submission_id"] = 1123
    _client_payload["aicrowd_participant_id"] = 1234
    
    # Instaiate a dummy context
    _context = {}
    # Instantiate an evaluator
    aicrowd_evaluator = MediqaEvaluator(answer_file_path)
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    print(result)
