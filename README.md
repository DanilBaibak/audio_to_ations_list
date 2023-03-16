# Machine Learning Project to Convert an Audio Record into an Actions List 

In this project, we will use the OpenAI API to convert audio from a meeting to an actions list. The motivation is pretty simple - if you don't have a list of actions as an outcome of the meeting, you probably wasted your time. On the other hand, compiling such a list is a fairly routine job. So let the AI do the boring part of the job for you.

## Solution design

We break our solution into two stages:
1. Get the transcript from the audio recording.
2. Extract the action list from the text.

<p align="center">
  <img src="https://github.com/DanilBaibak/ml-in-production/blob/master/images/meeting_record_to_actions_list.png" width="300" title="A meeting record to the actions list">
</p>

You can find more details in the Medium article.

## Installation

* Run `make init`
* Insert your OpenAI key into the `config.ini` file

## Usage

* To convert audio to text, run: `make audio_to_text path_to_the_audio_file path_to_save_the_transcript`
* To generate a list of actions from text , run: `make text_to_actions_list path_to_the_text_file path_to_save_the_list_of_actions`

You can also use the Python version of these commands:

* Activate virtual environment: `. venv/bin/activate`
* To convert audio to text, run: `python3 audio_to_text.py path_to_the_audio_file path_to_save_the_transcript`
* To generate a list of actions from text, run: `python3 text_to_actions_list.py path_to_the_text_file path_to_save_the_list_of_actions`
