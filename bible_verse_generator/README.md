# Bible Verse Generator(GPT-2)

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/bible_verse_generator)

## Motive
성경은 인류 역사상 가장 많이 팔린 책입니다. 종교적인 이유도 있겠지만, 성경의 내용에 좋은 글이 많이 있어서 꾸준히 베스트 셀러 자리를 지키고 있지 않나 생각이 듭니다. 저는 기독교 신자가 아니지만 가끔 성경의 내용이 궁금할 때가 있어 언젠가 한 번 읽어보고 싶었습니다. 성경의 양은 워낙 방대해서 쉽게 읽을 수 없기 때문에 keyword를 기반으로 제가 궁금한 부분을 읽고 싶었고, 그래서 keyword를 입력했을 때 그 keyword에 관련된 성경 구문을 만들어주는 서비스를 만들게 되었습니다.

## Dataset
kaggle에서 [bible dataset](https://www.kaggle.com/rexhaif/rus-eng-bible)을 받아와 [Teacherble NLP](https://ainize.ai/teachable-nlp)를 통해 dataset을 gpt2-small에 fine-tunning하여 모델을 만들었습니다.

## How to use

![Initial](https://user-images.githubusercontent.com/85500873/124550427-9655bb80-de6b-11eb-8dc1-85d74dbb0e13.png)
* 성경책에서 찾아보고 싶은 keyword를 textarea에 입력하고 Make Verse! 버튼을 누르면 입력한 keyword로 시작하는 성경책 구문이 작성됩니다.(ex: when the world)
* 입력하는 keyword는 영어만 지원합니다.
* 생성되는 문장은 약 50개의 단어로 생성됩니다.

## API Health Check
```
$ curl --request GET 'https://train-95y6kshrdyxtj652igs7-gpt2-train-teachable-ainize.endpoint.ainize.ai/ping'
{
  "status": "Healthy"
}
```

## API Prediction Test
```
$ curl --request POST 'https://train-95y6kshrdyxtj652igs7-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-en-small-finetune' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "text": "when the world",
    "num_samples": 1,
    "length": 50
  }'
[
  "when the world shall come full to meet him again his disciples will rejoice in him saying he shall not be afraid of them nor shall they be shaken from him he will not bring them into captivity for he hath sent them not into the city that they should see him"
]
```

## other API uses
* text to vector => https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/preprocess
* vector to text => https://main-gpt-2-server-gkswjdzz.endpoint.ainize.ai/postprocess