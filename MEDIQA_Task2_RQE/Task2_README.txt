MEDIQA @ ACL-BioNLP 2019  -- Task 2: Recognizing Question Entailment Task (RQE) 

https://sites.google.com/view/mediqa2019
The MEDIQA challenge is an ACL-BioNLP 2019 shared task aiming to attract further research efforts in Natural Language Inference (NLI), Recognizing Question Entailment (RQE), and their applications in medical Question Answering (QA).  
Mailing List: https://groups.google.com/forum/#!forum/bionlp-mediqa 

The objective of the RQE task is to identify entailment between two questions in the context of QA. We use the following definition of question entailment: “a question A entails a question B if every answer to B is also a complete or partial answer to A” [1]
    [1] A. Ben Abacha & D. Demner-Fushman. “Recognizing Question Entailment for Medical Question Answering”. AMIA 2016.
 
=========================================
Training and Validation sets (AMIA 2016)
=========================================

The RQE training and validation sets are already published here: https://github.com/abachaa/RQE_Data_AMIA2016
- Training Dataset: A collection of 8,588 clinical question-question pairs.
- Validation Dataset: A collection of 302 medical pairs of NLM-questions and NIH-FAQs.

If you use the RQE training and validation sets, please cite the following paper:

Recognizing Question Entailment for Medical Question Answering. Asma Ben Abacha and Dina Demner-Fushman. AMIA Annual Symposium proceedings, pages 310-318, 2016. 

		 @inproceedings{RQE:AMIA16,      
	  	 author    = {Asma {Ben Abacha} and Dina Demner{-}Fushman},     
		   title     = {Recognizing Question Entailment for Medical Question Answering},  
		   booktitle = {AMIA 2016, American Medical Informatics Association Annual Symposium, Chicago, IL, USA, November 12-16, 2016}, 
		   year      = {2016},     
		   url       = {https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5333286/} 
      
==============================
New Test Set (MEDIQA 2019) 
============================== 

https://github.com/abachaa/MEDIQA2019/blob/master/MEDIQA_Task2_RQE/MEDIQA2019-Task2-RQE-TestSet-wLabels.xml 

If you use this dataset, please cite our overview paper:

Asma Ben Abacha, Chaitanya Shivade, and Dina Demner-Fushman. Overview of the MEDIQA 2019 Shared Task on Textual Inference, Question Entailment and Question Answering. ACL-BioNLP 2019.

@inproceedings{MEDIQA2019, 

  author    = {Asma {Ben Abacha} and Chaitanya Shivade and Dina Demner{-}Fushman},  
  
  title     = {Overview of the MEDIQA 2019 Shared Task on Textual Inference, Question Entailment and Question Answering}, 
  
  booktitle = {ACL-BioNLP 2019},
  
  year      = {2019}
  
}

