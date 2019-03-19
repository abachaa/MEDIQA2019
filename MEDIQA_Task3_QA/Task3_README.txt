MEDIQA @ ACL-BioNLP 2019  -- Task 3: Question Answering (QA)

https://sites.google.com/view/mediqa2019
The MEDIQA challenge is an ACL-BioNLP 2019 shared task aiming to attract further research efforts in Natural Language Inference (NLI), Recognizing Question Entailment (RQE), and their applications in medical Question Answering (QA).  
Mailing List: https://groups.google.com/forum/#!forum/bionlp-mediqa

==============================
Task3: Question Answering (QA)
============================== 

Participants are tasked to:
- filter/classify the provided answers (1: correct, 0: incorrect). 
- re-rank the answers.  

Reuse of the systems developed in the first and second tasks is highly encouraged.

- For instance: 
i) the RQE system could be used to retrieve answered questions (e.g. from the MedQuAD dataset) that are entailed from the original questions and use their answers to validate the system's answers and re-rank them; 
ii) the NLI system could be used to identify the relations (i.e. entailment, contradiction, neutral) between the answers of the same question, as well as the answers of the questions related by the entailment relation.
   
- We encourage all other ideas and approaches for using textual inference and question entailment to filter and re-rank the retrieved answers.  

========================
Task3-QA: Training Sets 
========================

We provide two datasets of medical questions and the associated answers retrieved by CHiQA (https://chiqa.nlm.nih.gov/): 

    1) MEDIQA2019-Task3-QA-TrainingSet1-LiveQAMed.xml => 104 consumer health questions covering different types of questions about diseases and drugs (TREC-2017-LiveQA medical test questions), and the associated answers. 

    2) MEDIQA2019-Task3-QA-TrainingSet2-Alexa.xml => 104 simple questions about the most frequent diseases (dataset named Alexa), and the associated answers. 

a) SystemRank: corresponds to CHiQA's rank. 

b) ReferenceRank: corresponds to the correct rank. 

c) ReferenceScore: is an additional score that we provide only in the training and validation sets, and that corresponds to the manual judgment/rating of the answer [4: Excellent, 3: Correct but Incomplete, 2: Related, 1: Incorrect].  

For the answer classification task: answers with scores 1 and 2 are considered as incorrect (label 0), and answers with scores 3 and 4 are considered as correct (label 1).  
 
===================================
Task3-QA: Validation & Test Sets
===================================

The validation and test sets will be generated from a recent version of the medical QA system CHiQA, and will cover similar types of questions about diseases and drugs.  

The test set will have the same format, except that we will provide only the systemRank of the answer. 
<Question QID="">
        <QuestionText></QuestionText>
        <AnswerList>
            <Answer AID="" SystemRank="">
                <AnswerURL></AnswerURL>
                <AnswerText></AnswerText>
            </Answer>
        <AnswerList>
 </Question>

===================================
Task3-QA: Submission Format 
===================================

1) Each line should have the following format: QuestionID,AnswerID,Label. 
  Label = 0 (incorrect answer) 
  Label = 1 (correct answer)
  
2) For correct answers (label 1), the line order should correspond to the rank of the answer. 

Incorrect answers (label values of 0) will be used to compute accuracy.
For rank-based measures, incorrect answers will be filtered out automatically by our evaluation script. 

Example: 
Test question Q1 with 5 answers: A11, A12, A13, A14 and A15 (systemRanks)  

A submission file with 3 correct answers ranked: A13, A11, A15 and 2 incorrect answers: A12 and A15, should look like:  
Q1,A13,1
Q1,A11,1
Q1,A15,1
Q1,A12,0
Q1,A15,0


Contact Information: 
—————————------------- 
Asma Ben Abacha (asma.benabacha@nih.gov) 
