# Token


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print Token.to_json()

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_form_dict = token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


