# DocumentPagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The content of the chunk. | 
**language** | **str** | Two-character language code (e.g., "en"). | 

## Example

```python
from quepasa.models.document_pages_inner import DocumentPagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPagesInner from a JSON string
document_pages_inner_instance = DocumentPagesInner.from_json(json)
# print the JSON string representation of the object
print(DocumentPagesInner.to_json())

# convert the object into a dict
document_pages_inner_dict = document_pages_inner_instance.to_dict()
# create an instance of DocumentPagesInner from a dict
document_pages_inner_from_dict = DocumentPagesInner.from_dict(document_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


