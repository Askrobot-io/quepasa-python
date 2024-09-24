# quepasa.DefaultApi

All URIs are relative to *https://api.quepasa.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_status**](DefaultApi.md#get_batch_status) | **GET** /upload/data/batches/{id} | Get batch status
[**get_document**](DefaultApi.md#get_document) | **GET** /upload/data/documents/{domain}/{id} | Get document details
[**list_documents**](DefaultApi.md#list_documents) | **GET** /upload/data/documents/{domain} | List documents
[**remove_document**](DefaultApi.md#remove_document) | **DELETE** /upload/data/documents/{domain}/{id} | Remove document
[**replace_documents**](DefaultApi.md#replace_documents) | **PUT** /upload/data/documents/{domain} | Replace documents
[**reset_documents**](DefaultApi.md#reset_documents) | **DELETE** /upload/data/documents/{domain} | Reset documents
[**retrieve_answer**](DefaultApi.md#retrieve_answer) | **POST** /retrieve/answer | Retrieve answers or search data
[**retrieve_chunks**](DefaultApi.md#retrieve_chunks) | **POST** /retrieve/chunks | Retrieve answers or search data
[**setup_telegram**](DefaultApi.md#setup_telegram) | **PATCH** /upload/data/telegram | Setup Telegram integration
[**upsert_documents**](DefaultApi.md#upsert_documents) | **POST** /upload/data/documents/{domain} | Upsert documents
[**upsert_files**](DefaultApi.md#upsert_files) | **POST** /upload/data/files/{domain} | Upsert files


# **get_batch_status**
> BatchStatus get_batch_status(id)

Get batch status

Retrieve the status of a batch using its batch ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.batch_status import BatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get batch status
        api_response = api_instance.get_batch_status(id)
        print("The response of DefaultApi->get_batch_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_batch_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BatchStatus**](BatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch status retrieved. |  -  |
**404** | Batch not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentDetail get_document(domain, id)

Get document details

Retrieve details of a document by its domain and ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.document_detail import DocumentDetail
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'default' # str |  (default to 'default')
    id = 'id_example' # str | 

    try:
        # Get document details
        api_response = api_instance.get_document(domain, id)
        print("The response of DefaultApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [default to &#39;default&#39;]
 **id** | **str**|  | 

### Return type

[**DocumentDetail**](DocumentDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document details retrieved. |  -  |
**404** | Document not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> CreatedBatchStatus list_documents(domain)

List documents

List all document IDs in the specified domain.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | The domain name.

    try:
        # List documents
        api_response = api_instance.list_documents(domain)
        print("The response of DefaultApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_document**
> CreatedBatchStatus remove_document(domain, id)

Remove document

Remove a specific document by its domain and ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | 
    id = 'id_example' # str | 

    try:
        # Remove document
        api_response = api_instance.remove_document(domain, id)
        print("The response of DefaultApi->remove_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_documents**
> CreatedBatchStatus replace_documents(domain, document)

Replace documents

Replace all documents in the specified domain with the provided documents.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.models.document import Document
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | The domain name.
    document = [quepasa.Document()] # List[Document] | 

    try:
        # Replace documents
        api_response = api_instance.replace_documents(domain, document)
        print("The response of DefaultApi->replace_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->replace_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 
 **document** | [**List[Document]**](Document.md)|  | 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_documents**
> CreatedBatchStatus reset_documents(domain)

Reset documents

Remove all documents from the specified domain.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | The domain name.

    try:
        # Reset documents
        api_response = api_instance.reset_documents(domain)
        print("The response of DefaultApi->reset_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->reset_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_answer**
> AnswerDetail retrieve_answer(retrieve_answer_request)

Retrieve answers or search data

This endpoint allows you to generate an answer based on your data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.answer_detail import AnswerDetail
from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    retrieve_answer_request = quepasa.RetrieveAnswerRequest() # RetrieveAnswerRequest | 

    try:
        # Retrieve answers or search data
        api_response = api_instance.retrieve_answer(retrieve_answer_request)
        print("The response of DefaultApi->retrieve_answer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_answer_request** | [**RetrieveAnswerRequest**](RetrieveAnswerRequest.md)|  | 

### Return type

[**AnswerDetail**](AnswerDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_chunks**
> ChunksDetail retrieve_chunks(retrieve_answer_request)

Retrieve answers or search data

This endpoint allows you to perform a search on your data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.chunks_detail import ChunksDetail
from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    retrieve_answer_request = quepasa.RetrieveAnswerRequest() # RetrieveAnswerRequest | 

    try:
        # Retrieve answers or search data
        api_response = api_instance.retrieve_chunks(retrieve_answer_request)
        print("The response of DefaultApi->retrieve_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->retrieve_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_answer_request** | [**RetrieveAnswerRequest**](RetrieveAnswerRequest.md)|  | 

### Return type

[**ChunksDetail**](ChunksDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_telegram**
> TelegramStatus setup_telegram(setup_telegram_request)

Setup Telegram integration

Configure Telegram for notifications or integrations.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.setup_telegram_request import SetupTelegramRequest
from quepasa.models.telegram_status import TelegramStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    setup_telegram_request = quepasa.SetupTelegramRequest() # SetupTelegramRequest | 

    try:
        # Setup Telegram integration
        api_response = api_instance.setup_telegram(setup_telegram_request)
        print("The response of DefaultApi->setup_telegram:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->setup_telegram: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_telegram_request** | [**SetupTelegramRequest**](SetupTelegramRequest.md)|  | 

### Return type

[**TelegramStatus**](TelegramStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Telegram successfully set up. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_documents**
> CreatedBatchStatus upsert_documents(domain, document)

Upsert documents

Insert new documents or update existing ones based on the ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.models.document import Document
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | The domain name.
    document = [quepasa.Document()] # List[Document] | 

    try:
        # Upsert documents
        api_response = api_instance.upsert_documents(domain, document)
        print("The response of DefaultApi->upsert_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->upsert_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 
 **document** | [**List[Document]**](Document.md)|  | 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_files**
> CreatedBatchStatus upsert_files(domain, file, language=language)

Upsert files

Upload and upsert files into the document system.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = quepasa.DefaultApi(api_client)
    domain = 'domain_example' # str | The domain name.
    file = None # bytearray | The file to be uploaded.
    language = 'language_example' # str | Two-character language code (e.g., \\\"en\\\"). (optional)

    try:
        # Upsert files
        api_response = api_instance.upsert_files(domain, file, language=language)
        print("The response of DefaultApi->upsert_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->upsert_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name. | 
 **file** | **bytearray**| The file to be uploaded. | 
 **language** | **str**| Two-character language code (e.g., \\\&quot;en\\\&quot;). | [optional] 

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

