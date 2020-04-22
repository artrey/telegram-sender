# Telegram sender

Service for sending messages via bots (bypassing locks).

## Usage instructions

Send POST request with json body:

```json
{
  "tok": "<service token associated with bot>",
  "cid": "<telegram chat or channel id>",
  "mes": "<some message>"
}
```


## Examples

#### curl

```bash
curl -X POST -d '{"tok":"<token>","cid":"<chat id>","mes":"test message"}' <service address>/api/v1/send/
```
