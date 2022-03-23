# UPTIME-CHECK-MANAGER #

### What is this repository for? ###

* 이 프로젝트는 *GCP Monitoring*에서 uptime check하는 host가 많아지면서 *Slack*에 많은 메세지가 전송이 되어 수신받은 메세지들에 대한 정보가 한눈에 잘 보이지 않아 이를 해결하기 위해 시작되었습니다. 이 프로젝트를 사용하게 되면 기존에 host가 죽거나 복구되었을 때마다 alerting message를 받는 것이 아닌 일정 주기마다 각 host별로 간략한 status를 확인할 수 있습니다. 또한 확인하고싶지 않은 host는 slack에서 uptime 명령어를 이용하여 필터링할 수 있습니다.

* 기존 *GCP Monitoring*에서 *Slack*을 이용한 uptime check alerting 구조인 *GCP Monitoring* -> *Slack*에서 *GCP Monitoring* -> custom webhook server -> *Slack* 구조로 바꾸어 alerting message를 보기 쉽게 하기 위한 custom webhook server 프로젝트 입니다.
* custom webhook server를 이용하기 위한 외부 환경으로는 *GCP Monitoring*의 Alerting 탭에서 Notification channel 중 Webhooks 기능을 이용해야하며, *Slack*에서는 메세지를 수신받을 워크스페이스 채널에 *Incomming Webhook*과 *Outgoing Webhook* 앱을 추가하여야 합니다.


### How do I get set up? ###

* 이 프로젝트를 실행하는 환경에서는 'pip install -r requirements.txt' 를 실행하여 필요한 라이브러리들을 모두 설치하셔야합니다.
* config.py는 *GCP Monitoring*의 Webhooks 설정에서 HTTP 인증을 위한 user와 password를 포함하고 있으며, 또한 *Slack*에 message를 보내기 위한 *Slack Incomming Webhook* url를 포함하고 있습니다.
* custom webhook server -> Slack으로 메세지를 전송할 때 app.py의 APSscheduler JOBS에서 설정한 시간만큼 주기적으로 메세지가 전송이 됩니다.

### External environment guidelines ###

* *GCP Monitoring*

  - *GCP Monitoring*의 Alerting 탭에서 Edit Notification Channel에 들어간 후 Webhook 기능의 Add Webhook을 통해 이 프로젝트를 배포한 서버의 endpoint를 추가해주어야 합니다. 이 때 이 프로젝트에서 *GCP Monitoring*의 message를 수신받는 route는 '/fromGCPMonitoring'이므로 [ http://endpoint.url/fromGCPMonitoring ]와 같이 설정해주시면 됩니다.
  - HTTP Basic Auth의 user와 password는 config.py에서 설정한 user와 password를 입력하면 됩니다.<br/><br/>

* *Slack Incomming Webhook*
  - 메세지를 수신받을 *Slack*의 워크스페이스 채널에서 앱 추가를 통해 Incomming Webhooks를 추가 및 설정을 해줍니다.
  - 설정 중에 발급 받게 되는 Incomming Webook url은 config.py의 SLACK_URL에 적용시켜주어야 합니다.
  - *Slack Incomming Webhook* 추가 및 설정에 대한 자세한 설명은 [Incomming Webhooks Guide](https://api.slack.com/messaging/webhooks)에서 확인하실 수 있습니다.<br/><br/>


* *Slack Outgoing Webhook*
  - *Slack Incomming Webhook*과 마찬가지로 Slack의 워크스페이스 채널에서 Outgoing webhooks 앱을 추가 및 설정을 해줍니다.
  - 설정 중에 Trigger Word(s)는 'uptime'으로 설정해주시면 되며, URL(s)는 이 프로젝트에서 *Slack*의 message를 수신받는 route는 '/fromSlack'이므로 [ http://endpoint.url/fromSlack ]와 같이 설정해주시면 됩니다.
  - *Slack Outgoing Webhook* 추가 및 설정에 대한 자세한 설명은 [Outgoing Webhooks Guide](https://api.slack.com/legacy/custom-integrations/outgoing-webhooks)에서 확인하실 수 있습니다.

### How to use ###
*  프로젝트 셋업과 외부 환경 설정을 완료 후 프로젝트를 시작하면 설정한 주기적인 시간마다 *Slack*에서 uptime check list 메세지를 수신받게 됩니다.
   -  GCP Monitoring으로부터 아직 incident 메세지를 수신받지 못했을 때의 메세지 형식입니다. 
  <img width="549" src="./img/empty%20list.png"><br/><br/>
   -  GCP Monotoring으로부터 incident 메세지를 수신받은 후 메세지 형식입니다.
  <img width="618" src="./img/uptime%20check%20list.png"><br/><br/>
   -  이 프로젝트를 통해 지원되는 Slack에서 명령어 리스트를 확인할 수 있는 명령어 입니다. 메세지를 수신받는 채널에서 'uptime help'를 전송하면 작동하는 것을 확인할 수 있습니다.<br/>
  <img width="680" src="./img/uptime%20help.png"><br/><br/>
   -  'uptime check' 명령어 입니다. uptime check list를 바로 확인하고 싶을 때 사용할 수 있습니다.
  <img width="550" src="./img/uptime%20check.png"><br/><br/>
   -  'uptime remove {host.url}' 명령어를 사용하여 더 이상 확인하고 싶지 않은 host이거나 *GCP Monitoring*에서 uptime check를 해제한 host를 uptime check list에서 삭제할 수 있습니다.<br/>
  <img width="545" src="./img/uptime%20remove%20host.png"><br/><br/>
   -  'uptime removed' 명령어 입니다. 전에 'uptime remove {host.url}' 명령어로 삭제했던 host 목록을 보여줍니다.
  <img width="363" src="./img/uptime%20removed.png"><br/><br/>
   -  'uptime restore {host.url}' 명령어를 사용하여 이미 삭제한 host를 복구하여 다시 그 host에 대한 incident 메세지를 수신받을 수 있습니다.
  <img width="373" src="./img/uptime%20restore.png">

