# RetrieveAnswerRequestUserInfo

Optional user info to track requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique user ID. | [optional] 

## Example

```python
from quepasa.models.retrieve_answer_request_user_info import RetrieveAnswerRequestUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerRequestUserInfo from a JSON string
retrieve_answer_request_user_info_instance = RetrieveAnswerRequestUserInfo.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnswerRequestUserInfo.to_json())

# convert the object into a dict
retrieve_answer_request_user_info_dict = retrieve_answer_request_user_info_instance.to_dict()
# create an instance of RetrieveAnswerRequestUserInfo from a dict
retrieve_answer_request_user_info_from_dict = RetrieveAnswerRequestUserInfo.from_dict(retrieve_answer_request_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


