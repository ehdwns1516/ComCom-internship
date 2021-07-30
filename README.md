# Review Generator
---
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/text_summarizer)

## Overview
This model is a service that summarizes English text. Trained with a dataset of news articles and can be run directly from demo.

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

endpoint : [On Ainize](https://main-text-summarizer-ehdwns1516.endpoint.ainize.ai/)


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
  "0":"this is summary sentence"
}
```

### API Predict Test
```
$ curl --location --request POST 'https://main-text-summarizer-ehdwns1516.endpoint.ainize.ai/generate' \
--form 'min_words="30"' \
--form 'max_words="100"' \
--form 'num_beams="2"' \
--form 'context="The twice-capped 22-year-old is out of contract at the end of the season and has been linked with the Scarlets. Patchell is thought to be unhappy at Gareth Anscombe being preferred at fly-half and Wilson says there is interest in the player from Wales and abroad. "We're in the middle of discussions with Rhys, as we are with other players," Wilson said. "He's had a fair amount of interest, it's fair to say, from within Wales and from out of Wales. "We've made approaches to keep him. But ultimately what we need and want here are players who want to be here and play for Cardiff Blues."He'll make the appropriate decisions at the right time, as we will."Patchell made his Wales debut against Japan in June 2013 and was identified as a major prospect at fly-half.However, the arrival of Anscombe at the Blues in July 2014 from Waikato Chiefs in New Zealand saw the Cardiff-born Patchell moved to full-back to accommodate the newcomer."'
{
  "0":"Wales fly-half Rhys Patchell has been linked with a move away from Saracens, according to the club's director of rugby Dai Wilson.",
  "1":"Wales fly-half Rhys Patchell has been linked with a move away from Saracens, according to BBC Wales rugby correspondent Gareth Wilson."
}
```

### Healthy Check
```
$ curl --request GET 'https://main-text-summarizer-ehdwns1516.endpoint.ainize.ai/healthz'
{
  Health
}
```

## Acknowledgements
---
* Dataset: [xsum](https://huggingface.co/datasets/xsum)
* Pre-trained model: [facebook/bart-large](https://huggingface.co/facebook/bart-large)

