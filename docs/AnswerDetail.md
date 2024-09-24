# AnswerDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status. | [optional] 
**data** | [**AnswerDetailData**](AnswerDetailData.md) |  | [optional] 

## Example

```python
from quepasa.models.answer_detail import AnswerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerDetail from a JSON string
answer_detail_instance = AnswerDetail.from_json(json)
# print the JSON string representation of the object
print(AnswerDetail.to_json())

# convert the object into a dict
answer_detail_dict = answer_detail_instance.to_dict()
# create an instance of AnswerDetail from a dict
answer_detail_from_dict = AnswerDetail.from_dict(answer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


