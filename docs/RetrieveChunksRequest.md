# RetrieveChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Natural language query to retrieve or answer. | [optional] 
**domain** | **str** | The name of a group of documents. | [optional] 
**document_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 
**chunk_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 

## Example

```python
from quepasa.models.retrieve_chunks_request import RetrieveChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveChunksRequest from a JSON string
retrieve_chunks_request_instance = RetrieveChunksRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveChunksRequest.to_json())

# convert the object into a dict
retrieve_chunks_request_dict = retrieve_chunks_request_instance.to_dict()
# create an instance of RetrieveChunksRequest from a dict
retrieve_chunks_request_from_dict = RetrieveChunksRequest.from_dict(retrieve_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


