# DeliveryMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**email_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**integration_active_flag** | **bool** |  | [optional] 
**integration_email_flag** | **bool** |  | [optional] 
**integration_print_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.delivery_method import DeliveryMethod

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryMethod from a JSON string
delivery_method_instance = DeliveryMethod.from_json(json)
# print the JSON string representation of the object
print DeliveryMethod.to_json()

# convert the object into a dict
delivery_method_dict = delivery_method_instance.to_dict()
# create an instance of DeliveryMethod from a dict
delivery_method_form_dict = delivery_method.from_dict(delivery_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


