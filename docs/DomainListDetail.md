# DomainListDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status. | 
**data** | [**List[DomainDataDetail]**](DomainDataDetail.md) |  | 

## Example

```python
from quepasa.models.domain_list_detail import DomainListDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DomainListDetail from a JSON string
domain_list_detail_instance = DomainListDetail.from_json(json)
# print the JSON string representation of the object
print(DomainListDetail.to_json())

# convert the object into a dict
domain_list_detail_dict = domain_list_detail_instance.to_dict()
# create an instance of DomainListDetail from a dict
domain_list_detail_from_dict = DomainListDetail.from_dict(domain_list_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


