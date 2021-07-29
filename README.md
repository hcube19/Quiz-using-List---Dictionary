This is an implementation of a QUIZ using list and dictionary.<br />
Features of QUIZ:
* Questions are divided into sections.
  * You can select any section at begining and at the end of each section.
* You can skip any questions and can comeback to them at the end.
  * If you skip second time, it will be regarded as not answered and no negative marking for it.
* Have negative marking
* Will show your performance and number of questions answered and unanswered.
* Rank the performance of candidates.

NOTE :<br /> 
my marking scheme is bit harsh. everytime u answer wrong it will be penalized by n times. <br />
Eg. - first wrong =  - 1x0.5, second wrong = - ( first wrong + 2 x 0.5  )... so on <br />
If u want to penalize 0.5 for every time then do : <br />
1. Remove **neg_score** from everywhere <br />
2. In the end change **score=correct*pos-neg_score** to score=correct*(-wrong*0.5) <br />
