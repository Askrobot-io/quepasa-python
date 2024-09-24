# RetrieveAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Natural language query to retrieve or answer. | [optional] 
**user_info** | [**RetrieveAnswerRequestUserInfo**](RetrieveAnswerRequestUserInfo.md) |  | [optional] 

## Example

```python
from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerRequest from a JSON string
retrieve_answer_request_instance = RetrieveAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnswerRequest.to_json())

# convert the object into a dict
retrieve_answer_request_dict = retrieve_answer_request_instance.to_dict()
# create an instance of RetrieveAnswerRequest from a dict
retrieve_answer_request_from_dict = RetrieveAnswerRequest.from_dict(retrieve_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


