# Review Generator
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/review_generator)

## Overview


Github: [review_generator](https://github.com/ehdwns1516/text_summarizer)

Model: [HuggingFace](https://huggingface.co/ehdwns1516/bart_finetuned_xsum)

Model Code: [Ainize Workspace](https://ainize.ai/workspace/create?imageId=hnj95592adzr02xPTqss&git=https://github.com/ehdwns1516/bart_finetuned_xsum-notebook)

## Usage
---
### how to run a Demo

* Input your text what you want to summary.
* Adjust the range of min words, max words and beamsearch.
* Click summarize button for summary.
* You will receive the sentences in order of accuracy as the number of beam search.
* Only for English.

endpoint : [On Ainize](https://main-review-generator-ehdwns1516.endpoint.ainize.ai/)


## With cli
---
### Post Parameter
```
min_words: count of minimum words
max_words: count of maximum words
num_beams: count of beam search
context: context
```

### input format
```
{
  "min_words" : number
  "max_words" : number
  "num_beams" : number
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

