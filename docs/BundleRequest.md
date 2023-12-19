# BundleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_request** | [**ApiRequest**](ApiRequest.md) |  | [optional] 
**resource_type** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.bundle_request import BundleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRequest from a JSON string
bundle_request_instance = BundleRequest.from_json(json)
# print the JSON string representation of the object
print BundleRequest.to_json()

# convert the object into a dict
bundle_request_dict = bundle_request_instance.to_dict()
# create an instance of BundleRequest from a dict
bundle_request_form_dict = bundle_request.from_dict(bundle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


