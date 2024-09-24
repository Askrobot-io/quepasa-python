# AnswerDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | The answer generated in response to the query. | [optional] 
**links** | [**Dict[str, AnswerDetailDataLinksValue]**](AnswerDetailDataLinksValue.md) | A list of references used in the generated answer. | [optional] 
**markdown** | **str** | Answer formatted in Markdown, with links. | [optional] 
**labeled_links** | [**Dict[str, AnswerDetailDataLabeledLinksValue]**](AnswerDetailDataLabeledLinksValue.md) | References in Markdown format. | [optional] 

## Example

```python
from quepasa.models.answer_detail_data import AnswerDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerDetailData from a JSON string
answer_detail_data_instance = AnswerDetailData.from_json(json)
# print the JSON string representation of the object
print(AnswerDetailData.to_json())

# convert the object into a dict
answer_detail_data_dict = answer_detail_data_instance.to_dict()
# create an instance of AnswerDetailData from a dict
answer_detail_data_from_dict = AnswerDetailData.from_dict(answer_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


