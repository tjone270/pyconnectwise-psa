# ApiRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**IRestIdentifiedItem**](IRestIdentifiedItem.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**fields** | **str** |  | [optional] 
**filters** | [**FilterValues**](FilterValues.md) |  | [optional] 
**format** | **str** |  | [optional] 
**grand_parent_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**member_context** | **str** |  | [optional] 
**misc_properties** | **Dict[str, object]** |  | [optional] 
**page** | [**PageValues**](PageValues.md) |  | [optional] 
**parent_id** | **int** |  | [optional] 
**update_only_ces_properties** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.api_request import ApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRequest from a JSON string
api_request_instance = ApiRequest.from_json(json)
# print the JSON string representation of the object
print ApiRequest.to_json()

# convert the object into a dict
api_request_dict = api_request_instance.to_dict()
# create an instance of ApiRequest from a dict
api_request_form_dict = api_request.from_dict(api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


