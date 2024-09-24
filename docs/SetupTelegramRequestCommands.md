# SetupTelegramRequestCommands

Telegram bot commands.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**SetupTelegramRequestCommandsStart**](SetupTelegramRequestCommandsStart.md) |  | [optional] 
**ask** | [**SetupTelegramRequestCommandsAsk**](SetupTelegramRequestCommandsAsk.md) |  | [optional] 

## Example

```python
from quepasa.models.setup_telegram_request_commands import SetupTelegramRequestCommands

# TODO update the JSON string below
json = "{}"
# create an instance of SetupTelegramRequestCommands from a JSON string
setup_telegram_request_commands_instance = SetupTelegramRequestCommands.from_json(json)
# print the JSON string representation of the object
print(SetupTelegramRequestCommands.to_json())

# convert the object into a dict
setup_telegram_request_commands_dict = setup_telegram_request_commands_instance.to_dict()
# create an instance of SetupTelegramRequestCommands from a dict
setup_telegram_request_commands_from_dict = SetupTelegramRequestCommands.from_dict(setup_telegram_request_commands_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


