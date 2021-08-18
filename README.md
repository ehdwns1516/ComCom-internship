# Grasping Sentence Intent
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/KLUE-RoBERTa-base_sae)

## Overview
This model grasp the intent for a given sentence and classifies whether it is yes/no, alternative, wh-questions, prohibitions, requirements, or strong requirements.

Github: [KLUE-RoBERTa-base_sae](https://github.com/ehdwns1516/KLUE-RoBERTa-base_sae)

Model: [HuggingFace](https://huggingface.co/ehdwns1516/klue-roberta-base_sae)

Model Code: [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/ehdwns1516/Multiple_choice_SWAG_finetunning)

## Usage
---
### how to run a Demo

* Input sentence what you want to grasp intent.
* Click "Grasp sentence intent" button to get intent.

![demo](https://user-images.githubusercontent.com/85500873/129871109-78672d5d-a51a-4b98-b04d-05f6783f3be9.png)

endpoint : [On Ainize](https://main-klue-ro-ber-ta-base-sae-ehdwns1516.endpoint.ainize.ai/)


## With cli
---
### Post Parameter
```
context: sentence what you want to grasp intent.
```

### input format
```
{
  "context" : string
}
```

### output format
```
{
  "label":"intent","score":percentage
}
```

### API Predict Test
```
$ curl --location --request POST 'https://main-klue-ro-ber-ta-base-sae-ehdwns1516.endpoint.ainize.ai/generate' \
--form 'context="내일 날씨가 어떨까?"'
{
  "label":"wh- questions","score":0.9992098808288574
}
```

### Healthy Check
```
$ curl --request GET 'https://main-klue-ro-ber-ta-base-sae-ehdwns1516.endpoint.ainize.ai/healthz'
{
  Health
}
```

## Acknowledgements
---
* Dataset: [kor_sae](https://huggingface.co/datasets/kor_sae)
* Pre-trained model: [klue/roberta-base](https://huggingface.co/klue/roberta-base)

