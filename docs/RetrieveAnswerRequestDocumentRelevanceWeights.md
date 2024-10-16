# RetrieveAnswerRequestDocumentRelevanceWeights

A hybrid ranking formula for documents, balancing two parameters: text for full-text search and semantic for semantic search. The format allows you to adjust the weight of each component. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **float** | The ranking weight for the full-text search factor. | [optional] 
**semantic** | **float** | The ranking weight for the semantic search factor. | [optional] 

## Example

```python
from quepasa.models.retrieve_answer_request_document_relevance_weights import RetrieveAnswerRequestDocumentRelevanceWeights

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerRequestDocumentRelevanceWeights from a JSON string
retrieve_answer_request_document_relevance_weights_instance = RetrieveAnswerRequestDocumentRelevanceWeights.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnswerRequestDocumentRelevanceWeights.to_json())

# convert the object into a dict
retrieve_answer_request_document_relevance_weights_dict = retrieve_answer_request_document_relevance_weights_instance.to_dict()
# create an instance of RetrieveAnswerRequestDocumentRelevanceWeights from a dict
retrieve_answer_request_document_relevance_weights_from_dict = RetrieveAnswerRequestDocumentRelevanceWeights.from_dict(retrieve_answer_request_document_relevance_weights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


