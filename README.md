> **Note**
> The EBI Cloud Portal has been retired and its code base is no longer updated. This includes all tooling for the VM-related features of the BioExcel Portal.

# biotools API mock for integration testing of Bioexcel Portal

## Requirement 
python 3.6

## Install Flask
pip3 install Flask

## Make executable & Run
biotools.py

## Publish changes to mock API server
1. Push the changes to git repo
2. Run ansible playbook for frontend servers

ansible-playbook frontends.yml -i tsi-inventory

