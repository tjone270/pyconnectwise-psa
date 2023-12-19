# ImportMassMaintenance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_company_count** | **int** |  | [optional] 
**deleted_contact_count** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.import_mass_maintenance import ImportMassMaintenance

# TODO update the JSON string below
json = "{}"
# create an instance of ImportMassMaintenance from a JSON string
import_mass_maintenance_instance = ImportMassMaintenance.from_json(json)
# print the JSON string representation of the object
print ImportMassMaintenance.to_json()

# convert the object into a dict
import_mass_maintenance_dict = import_mass_maintenance_instance.to_dict()
# create an instance of ImportMassMaintenance from a dict
import_mass_maintenance_form_dict = import_mass_maintenance.from_dict(import_mass_maintenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


