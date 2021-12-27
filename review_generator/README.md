# Review Generator
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/review_generator)

## Overview
This service is models that generate reviews based on star rating and text. You can choose Language that English or Korean.

Github: [review_generator](https://github.com/ehdwns1516/review_generator)

Model_Kor: [HuggingFace](https://huggingface.co/ehdwns1516/gpt2_review_star1)

Model_En: [HuggingFace](https://huggingface.co/ehdwns1516/gpt3-kor-based_gpt2_review_SR1)

Model Code: [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/ehdwns1516/gpt2_review_fine-tunning_note)

## Usage
---
### how to run a Demo

* Select language you want generate review.
* Choose star rating and input your text.
* Click submit button for generating review.
* If the context is longer than 1200 characters, the context may be cut in the middle and the result may not come out well.

endpoint : [On Ainize](https://main-review-generator-ehdwns1516.endpoint.ainize.ai/)


## With cli
---
### Post Parameter
```
sel_lan: Language
star_rating: star rating
context: context
```

### input format
```
{
  "sel_lan" : string
  "star_rating" : string
  "context" : string
}
```

### output format
```
{
  "0":[
    {"generated_text":"blah blah blah"}
  ]
}
```

### API Predict Test
```
$ curl --location --request POST 'https://main-review-generator-ehdwns1516.endpoint.ainize.ai/generate' \
--form 'sel_lan="English"' \
--form 'star_rating="5"' \
--form 'context="the cost"'
{
  "0":[
    {
      "generated_text" : "the cost is right so it’s what I needed.It's a little difficult to get it out of my hands but once you do, the feel nice and keeps my toes from cutting. The only thing I noticed is the little plastic piece" 
    }
  ]
}
```

### Healthy Check
```
$ curl --request GET 'https://main-review-generator-ehdwns1516.endpoint.ainize.ai//healthz'
{
  Health
}
```

## Acknowledgements
---
* Dataset_Kor: [naver shopping review dataset](https://github.com/bab2min/corpus/tree/master/sentiment)
* Dataset_En: [amazon review dataset](https://huggingface.co/datasets/amazon_reviews_multi)
* Pre-trained model_Kor: [kykim/gpt3-kor-small_based_on_gpt2](https://huggingface.co/klue/roberta-base)
* Pre-trained model_En: [GPT2](https://huggingface.co/gpt2)

