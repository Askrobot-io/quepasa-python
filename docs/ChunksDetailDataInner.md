# ChunksDetailDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from quepasa.models.chunks_detail_data_inner import ChunksDetailDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChunksDetailDataInner from a JSON string
chunks_detail_data_inner_instance = ChunksDetailDataInner.from_json(json)
# print the JSON string representation of the object
print(ChunksDetailDataInner.to_json())

# convert the object into a dict
chunks_detail_data_inner_dict = chunks_detail_data_inner_instance.to_dict()
# create an instance of ChunksDetailDataInner from a dict
chunks_detail_data_inner_from_dict = ChunksDetailDataInner.from_dict(chunks_detail_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


