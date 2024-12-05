# RetrieveAnswerRequestRelevanceWeights

A hybrid ranking formula that balances the contributions of two parameters: `document` and `chunk`. This structure allows fine-tuning the weight assigned to each component in the ranking process. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **float** | The ranking weight assigned to the entire document. Adjust this value to influence the importance of document-level factors in the ranking. | [optional] 
**chunk** | **float** | The ranking weight assigned to individual chunks of a document. Adjust this value to influence the importance of chunk-level factors in the ranking. | [optional] 

## Example

```python
from quepasa.models.retrieve_answer_request_relevance_weights import RetrieveAnswerRequestRelevanceWeights

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerRequestRelevanceWeights from a JSON string
retrieve_answer_request_relevance_weights_instance = RetrieveAnswerRequestRelevanceWeights.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnswerRequestRelevanceWeights.to_json())

# convert the object into a dict
retrieve_answer_request_relevance_weights_dict = retrieve_answer_request_relevance_weights_instance.to_dict()
# create an instance of RetrieveAnswerRequestRelevanceWeights from a dict
retrieve_answer_request_relevance_weights_from_dict = RetrieveAnswerRequestRelevanceWeights.from_dict(retrieve_answer_request_relevance_weights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


