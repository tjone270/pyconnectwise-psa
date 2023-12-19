# ReportingService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**reporting_domain** | **str** |  Max length: 50; | [optional] 
**reporting_password** | **str** | To blank out the password, enter an empty string here. Max length: 50; | [optional] 
**reporting_url** | **str** |  Max length: 100; | [optional] 
**reporting_user_name** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.reporting_service import ReportingService

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingService from a JSON string
reporting_service_instance = ReportingService.from_json(json)
# print the JSON string representation of the object
print ReportingService.to_json()

# convert the object into a dict
reporting_service_dict = reporting_service_instance.to_dict()
# create an instance of ReportingService from a dict
reporting_service_form_dict = reporting_service.from_dict(reporting_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


