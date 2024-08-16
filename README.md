# test-task
Test project of credit application system

The project is implemented as an API service using the Django REST framework. To demonstrate how the system works, run the Docker container. 

To add test data and get unique manufacturer IDs by contract number, use the following endpoints:

* **adding test data**:
 
  api/v1/add_manufacturer/
  
  api/v1/add_contract/
  
  api/v1/add_product/
  
  credit application will be created automatically after contract creation.

* **getting unique manufacturer IDs by contract number**
  
   api/v1/ api/v1/get_manufacturers_by_contract/<int:contract_id>/
  
  notice that contract_id means not pk value in db table Contracts, but number that you provide when create a new contract. 
