# UDEL Health Checker

This program fills out UDEL's daily health check and generates the green check mark.

## Use
To use this program, you need to be a University of Delaware student or employee. It will also only fill out the form 
as if you do not have COVID-19 or do not have symptoms. If you do have COVID-19 or have symptoms of COVID-19, **DO NOT 
USE THIS PROGRAM**.

To use the program, all you need to do is fork this repository, and add your USERNAME and PASSWORD as repository secrets.
Once that has been done, the health check will automatically be filled out every day at the scheduled time in 
[RunHealthCheck.yaml](.github/workflows/RunHealthCheck.yaml). If you would like to change the schedule on which the health
check is run, look at this [scheduling format](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule).


### Important Notes
As stated before, this only completes the health check and generates a green check mark. **DO NOT ABUSE THIS!** If you 
know that you have COVID-19, or have come in close contact with somebody that has had COVID-19, please remove the schedule
line from [RunHealthCheck.yaml](.github/workflows/RunHealthCheck.yaml).