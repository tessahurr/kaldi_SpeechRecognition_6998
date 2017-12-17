# kaldi_SpeechRecognition_6998

This is Tessa Hurr's project for Columbia University's Fundamentals of Speech Recognition 6998.

In order to run this program, follow these steps:
1) This project uses Kaldi, so make sure to download all their prerequisite and instructions to install.
2) Navigate to: "/kaldi_SpeechRecognition_6998/egs/tedlium/s5_r2/local/" and run preprocess.py on the desired dataset. Note: It is likely that the path to your data in lines 60 and 127 will need to be changed in order to access your data.  Data should be taken in as .txt files
3) Navigate to "/kaldi_SpeechRecognition_6998/egs/tedlium/s5_r2/" and run "get_dict.sh".  This will give you the Tedlium dictionary.
4) Run "execute.sh" to start pocolm.
