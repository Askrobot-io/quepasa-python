# DomainDataDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of a group of documents. | 
**processed_ids** | **List[str]** |  | 

## Example

```python
from quepasa.models.domain_data_detail import DomainDataDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDataDetail from a JSON string
domain_data_detail_instance = DomainDataDetail.from_json(json)
# print the JSON string representation of the object
print(DomainDataDetail.to_json())

# convert the object into a dict
domain_data_detail_dict = domain_data_detail_instance.to_dict()
# create an instance of DomainDataDetail from a dict
domain_data_detail_from_dict = DomainDataDetail.from_dict(domain_data_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


