# Sentence Inference Multiple Choice
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/sentence_inference_multiple_choice)

## Overview
This model finds the most appropriate sentence among multiple choice sentences to follow the main sentence. It is a way to analyze the situation through the main sentence and infer the next sentence.

Github: [sentence_inference_multiple_choice](https://github.com/ehdwns1516/sentence_inference_multiple_choice)

Model: [HuggingFace](https://huggingface.co/ehdwns1516/bert-base-uncased_SWAG)

Model Code: [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/ehdwns1516/Multiple_choice_SWAG_finetunning)

## Usage
---
### how to run a Demo

* Input main sentence.
* Click add button to make inference sentence input area.
* Input inference sentences.
* Click "Find the most appropriate sentence." button to get result.

![demo](https://user-images.githubusercontent.com/85500873/128327238-8a3c52df-655a-4f1b-9238-13bf00ba51e2.png)

endpoint : [On Ainize](https://main-sentence-inference-multiple-choice-ehdwns1516.endpoint.ainize.ai/)


## With cli
---
### Post Parameter
```
count: count of inference senteces.
items[0]: item of inference sentences.
items[1]: item of inference sentences.
items[2]: item of inference sentences.
'
'
'
items[count]: item of inference sentences.
context: context of main sentence.
```

### input format
```
{
  "count" : number
  "items[0]" : string
  "items[1]" : string
  "items[2]" : string
  '
  '
  '
  "items[count-1]" : string
  "context" : string
}
```

### output format
```
{
  'result': 'blah blah blah'
}
```

### API Predict Test
```
$ curl --location --request POST 'https://main-sentence-inference-multiple-choice-ehdwns1516.endpoint.ainize.ai/generate' \
--form 'count="4"' \
--form 'items[0]="brings up a syringe."' \
--form 'items[1]="hangs his coat as he fidgets around then leans a case on his leg and rubs his shoulder."' \
--form 'items[2]="pulls a clipboard past a hanging panel a few inches along the bottom of a winding hallway."' \
--form 'items[3]="steps toward the door."' \
--form 'context="One hand in his pocket, someone strolls toward the dining room where two stewards stand outside its doors. Inside, someone"'
{
  'result': 'steps toward the door.'
}
```

### Healthy Check
```
$ curl --request GET 'https://main-sentence-inference-multiple-choice-ehdwns1516.endpoint.ainize.ai/healthz'
{
  Health
}
```

## Acknowledgements
---
* Dataset: [SWAG](https://huggingface.co/datasets/swag)
* Pre-trained model: [bert-base-uncased](https://huggingface.co/bert-base-uncased)

