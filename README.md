# KLUE-RoBERTa-base-KorNLI(Korean)

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/klue-roberta-base_kornli)

huggingface에 배포 되어있는 kakaobrain의 [KorNLI dataset](https://github.com/kakaobrain/KorNLUDatasets)을 이용하여 klue-RoBERTa-base model에 fine-tunning한 모델입니다.

Github: [klue-roberta-base_kornli](https://github.com/ehdwns1516/klue-roberta-base_kornli)

Open API: [On Ainize](https://ainize.web.app/redirect?git_repo=https://github.com/ehdwns1516/klue-roberta-base_kornli)

License: [CC-BY-SA-4.0](https://github.com/KLUE-benchmark/KLUE/blob/main/License.md)

Model: [HuggingFace](https://huggingface.co/ehdwns1516/klue-roberta-base-kornli)

Model Code: [Ainize Workspace](https://a966119d3186.ngrok.io/notebooks/DJ/KLUE-NLI/klue-roberta-base-kornli.ipynb)

## Post parameter
```
premise: 전제 문장
hypothesis: 가설 문장
```

## Output format
```
{
  "0":[
    {"label":"entailment","score": 점수},{"label":"neutral","score": 점수},{"label":"contradiction","score": 점수}
  ]
}
```

## API Health Check
```
$ curl --request GET 'https://main-klue-roberta-base-kornli-ehdwns1516.endpoint.ainize.ai/healthz'
{
  Health
}
```

## API Prediction Test
```
$ curl -X POST "https://main-klue-roberta-base-kornli-ehdwns1516.endpoint.ainize.ai/generate" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "premise={저는, 그냥 알아내려고 거기 있었어요.}" -F "hypothesis={이해하려고 거기에 있었을 뿐이에요.}"
{
  "0":[
    {"label":"entailment","score":0.8480604290962219},{"label":"neutral","score":0.1316358894109726},{"label":"contradiction","score":0.02030368708074093}
  ]
}
```
