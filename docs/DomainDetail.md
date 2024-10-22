# DomainDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status. | 
**data** | [**DomainDataDetail**](DomainDataDetail.md) |  | 

## Example

```python
from quepasa.models.domain_detail import DomainDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDetail from a JSON string
domain_detail_instance = DomainDetail.from_json(json)
# print the JSON string representation of the object
print(DomainDetail.to_json())

# convert the object into a dict
domain_detail_dict = domain_detail_instance.to_dict()
# create an instance of DomainDetail from a dict
domain_detail_from_dict = DomainDetail.from_dict(domain_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


