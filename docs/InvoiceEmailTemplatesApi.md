# connectwise_psa.InvoiceEmailTemplatesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_invoice_email_templates_by_id**](InvoiceEmailTemplatesApi.md#delete_finance_invoice_email_templates_by_id) | **DELETE** /finance/invoiceEmailTemplates/{id} | Delete InvoiceEmailTemplate
[**get_finance_invoice_email_templates**](InvoiceEmailTemplatesApi.md#get_finance_invoice_email_templates) | **GET** /finance/invoiceEmailTemplates | Get List of InvoiceEmailTemplate
[**get_finance_invoice_email_templates_by_id**](InvoiceEmailTemplatesApi.md#get_finance_invoice_email_templates_by_id) | **GET** /finance/invoiceEmailTemplates/{id} | Get InvoiceEmailTemplate
[**get_finance_invoice_email_templates_by_id_usages**](InvoiceEmailTemplatesApi.md#get_finance_invoice_email_templates_by_id_usages) | **GET** /finance/invoiceEmailTemplates/{id}/usages | Get List of Usage Count
[**get_finance_invoice_email_templates_by_id_usages_list**](InvoiceEmailTemplatesApi.md#get_finance_invoice_email_templates_by_id_usages_list) | **GET** /finance/invoiceEmailTemplates/{id}/usages/list | Get List of Usage
[**get_finance_invoice_email_templates_count**](InvoiceEmailTemplatesApi.md#get_finance_invoice_email_templates_count) | **GET** /finance/invoiceEmailTemplates/count | Get Count of InvoiceEmailTemplate
[**patch_finance_invoice_email_templates_by_id**](InvoiceEmailTemplatesApi.md#patch_finance_invoice_email_templates_by_id) | **PATCH** /finance/invoiceEmailTemplates/{id} | Patch InvoiceEmailTemplate
[**post_finance_invoice_email_templates**](InvoiceEmailTemplatesApi.md#post_finance_invoice_email_templates) | **POST** /finance/invoiceEmailTemplates | Post InvoiceEmailTemplate
[**put_finance_invoice_email_templates_by_id**](InvoiceEmailTemplatesApi.md#put_finance_invoice_email_templates_by_id) | **PUT** /finance/invoiceEmailTemplates/{id} | Put InvoiceEmailTemplate


# **delete_finance_invoice_email_templates_by_id**
> delete_finance_invoice_email_templates_by_id(id, client_id)

Delete InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 

    try:
        # Delete InvoiceEmailTemplate
        api_instance.delete_finance_invoice_email_templates_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->delete_finance_invoice_email_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoice_email_templates**
> List[InvoiceEmailTemplate] get_finance_invoice_email_templates(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of InvoiceEmailTemplate
        api_response = api_instance.get_finance_invoice_email_templates(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoiceEmailTemplatesApi->get_finance_invoice_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->get_finance_invoice_email_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[InvoiceEmailTemplate]**](InvoiceEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of InvoiceEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoice_email_templates_by_id**
> InvoiceEmailTemplate get_finance_invoice_email_templates_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get InvoiceEmailTemplate
        api_response = api_instance.get_finance_invoice_email_templates_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoice_email_templates_by_id_usages**
> List[Usage] get_finance_invoice_email_templates_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage Count

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of Usage Count
        api_response = api_instance.get_finance_invoice_email_templates_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoice_email_templates_by_id_usages_list**
> List[Usage] get_finance_invoice_email_templates_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of Usage
        api_response = api_instance.get_finance_invoice_email_templates_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoice_email_templates_count**
> Count get_finance_invoice_email_templates_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get Count of InvoiceEmailTemplate
        api_response = api_instance.get_finance_invoice_email_templates_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->get_finance_invoice_email_templates_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_finance_invoice_email_templates_by_id**
> InvoiceEmailTemplate patch_finance_invoice_email_templates_by_id(id, client_id, patch_operation)

Patch InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch InvoiceEmailTemplate
        api_response = api_instance.patch_finance_invoice_email_templates_by_id(id, client_id, patch_operation)
        print("The response of InvoiceEmailTemplatesApi->patch_finance_invoice_email_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->patch_finance_invoice_email_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_invoice_email_templates**
> InvoiceEmailTemplate post_finance_invoice_email_templates(client_id, invoice_email_template)

Post InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    client_id = 'client_id_example' # str | 
    invoice_email_template = connectwise_psa.InvoiceEmailTemplate() # InvoiceEmailTemplate | invoiceEmailTemplate

    try:
        # Post InvoiceEmailTemplate
        api_response = api_instance.post_finance_invoice_email_templates(client_id, invoice_email_template)
        print("The response of InvoiceEmailTemplatesApi->post_finance_invoice_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->post_finance_invoice_email_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **invoice_email_template** | [**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)| invoiceEmailTemplate | 

### Return type

[**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | InvoiceEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_invoice_email_templates_by_id**
> InvoiceEmailTemplate put_finance_invoice_email_templates_by_id(id, client_id, invoice_email_template)

Put InvoiceEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.InvoiceEmailTemplatesApi(api_client)
    id = 56 # int | invoiceEmailTemplateId
    client_id = 'client_id_example' # str | 
    invoice_email_template = connectwise_psa.InvoiceEmailTemplate() # InvoiceEmailTemplate | invoiceEmailTemplate

    try:
        # Put InvoiceEmailTemplate
        api_response = api_instance.put_finance_invoice_email_templates_by_id(id, client_id, invoice_email_template)
        print("The response of InvoiceEmailTemplatesApi->put_finance_invoice_email_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceEmailTemplatesApi->put_finance_invoice_email_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceEmailTemplateId | 
 **client_id** | **str**|  | 
 **invoice_email_template** | [**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)| invoiceEmailTemplate | 

### Return type

[**InvoiceEmailTemplate**](InvoiceEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InvoiceEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

