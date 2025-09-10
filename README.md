# Requirements-Template-Checker

## Project Description
The idea is to use AI to examine the structure of software requirements written according to a specific sentence template.
For the AI to be able to perform such a check, it is given a predefined sentence template and a list of process verbs. 
I used the sentence template provided by SOPHISTs. This can be found in the brochure "Schablonen für alle Fälle". A description of the sentence templates is also provided in English. See https://sophist.de/w4f/

All prompts and requirements are written in German.

## Features
- Begin with the first prompt (`Promt-for-start.docx`) in the AI tool you have chosen.
- Then provide the AI with the following specifications:
  - `Promt-for-requirement-template.docx`: Defines the structure of a valid requirement
  - `Promt-for-process-verb.docx`: Lists all valid process verbs
  - `Promt-for-result-formatting.docx`: Specifies the evaluation criteria and format
- Then let the AI check your requirements. You can either have individual requirements checked, or a collection (`requirements.csv`) of requirements.

## todo

