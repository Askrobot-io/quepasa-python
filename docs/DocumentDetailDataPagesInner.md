# DocumentDetailDataPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The content of the chunk. | 
**language** | **str** | Two-character language code (e.g., "en"). | 
**keywords** | **str** | Optional keywords for search optimization. | [optional] 

## Example

```python
from quepasa.models.document_detail_data_pages_inner import DocumentDetailDataPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailDataPagesInner from a JSON string
document_detail_data_pages_inner_instance = DocumentDetailDataPagesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailDataPagesInner.to_json())

# convert the object into a dict
document_detail_data_pages_inner_dict = document_detail_data_pages_inner_instance.to_dict()
# create an instance of DocumentDetailDataPagesInner from a dict
document_detail_data_pages_inner_from_dict = DocumentDetailDataPagesInner.from_dict(document_detail_data_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


