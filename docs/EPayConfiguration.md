# EPayConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**encryption_key** | **str** |  Max length: 500; | [optional] 
**id** | **int** |  | [optional] 
**initialization_vector** | **str** |  Max length: 500; | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**store_identifier** | **str** |  Max length: 500; | 
**url** | **str** |  Max length: 400; | 

## Example

```python
from connectwise_psa.models.e_pay_configuration import EPayConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of EPayConfiguration from a JSON string
e_pay_configuration_instance = EPayConfiguration.from_json(json)
# print the JSON string representation of the object
print EPayConfiguration.to_json()

# convert the object into a dict
e_pay_configuration_dict = e_pay_configuration_instance.to_dict()
# create an instance of EPayConfiguration from a dict
e_pay_configuration_form_dict = e_pay_configuration.from_dict(e_pay_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


