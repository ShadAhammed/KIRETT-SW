# KIRETT-Demonstrator

Use for the KIRETT Project demonstration with test data.

## Description

The software is used to test the developed ANN models with specific test data provided with software(/data/TestData/TestData.xlsx).
Total 6 complication models are developed in this project which are:
1. Cardiovascular Complication
2. Respiratory and Cardio Complication
3. Neurology Complication
4. Metabollic Complication
5. Psychiatric Complication
6. Abdominal Complication

All the Keras ANN models stored as .h5 files are provided(/src/models/NNModels).

All the Pytorch ANN models stored as .pt files are provided(/src/models/PTModels).

## Test Data

Test data are created for each complication. Some features are written in short form as below:

RR - Respiratory rate<br>
BG - Blood glucose<br>
PR - Pulse rate<br>
PRh - Pulse Rhythm<br>
Abd - Abdominal<br>
Circ - Circulation<br>
Meta - Metabollic<br>

First letter of each complication is sometimes used as a shortcut.

Health vitals are continuous variable. All others except circulation are binary where 0 indicates normal or no anomaly condition and 1 indicates anomaly or 
abnormal condition exists for the feature. The value of circulation range from 0 to 6. Highest value indicates the test capability of checking the blood circulation of the patient.

Each of the test data comes with a key feature - 'case'. This column indicates the case identification number of the test case. To know more information about any test case,
refer to the master data file and use the key.


### Dependencies

* Check requirements.txt for the required library
* Windows/Linux

### How to use

Clone the repository to your local computer using git clone <remote>. Then follow the steps using a python IDE:

1. Run the file Demonstration.py
2. Select the test file
2. Select a test case based on relevant complication
3. If you want to modify the selected test data, simply type  'yes' or skip
4. The results will highlight the probability percentage of each complication for the selected test data

## Author

Abu Shad Ahammed(abu.ahammed@uni-siegen.de)  
Chair of Embedded Systems, Universität Siegen

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Don't
Please don't change anything in this remote repository. 
Create a branch or make changes to your local repo.



