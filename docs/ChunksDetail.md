# ChunksDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status. | [optional] 
**data** | [**List[ChunksDetailDataInner]**](ChunksDetailDataInner.md) |  | [optional] 

## Example

```python
from quepasa.models.chunks_detail import ChunksDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ChunksDetail from a JSON string
chunks_detail_instance = ChunksDetail.from_json(json)
# print the JSON string representation of the object
print(ChunksDetail.to_json())

# convert the object into a dict
chunks_detail_dict = chunks_detail_instance.to_dict()
# create an instance of ChunksDetail from a dict
chunks_detail_from_dict = ChunksDetail.from_dict(chunks_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


