# README

Description:

This script augments MS Learn data on modules and learning paths with additional data about World Wide Learning certifications to enable you to build reports on content at the certification and (hopefully soon) solution area.

Features:

- Takes list of cert URLs in via config file
- Crawls each cert page for Learning path UIDs
- Uses kusto query to look up metadata for Learn Path UID and Module UID
- Merges data frame with metadata with a previously downloaded csv files that contain performance data
- writes the resulting files to CSV - only contains performance data for all learning paths and modules associated with certs in the config file

Instructions:

1. The script pulls meta-data for modules and learning paths from CGA Kusto clusters. Please request access to the clusters [here](https://review.docs.microsoft.com/en-us/help/contribute/contribute-how-to-connect-kusto?branch=master#request-access-to-kusto-clusters).

2. Download the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).  Azure CLI is used to enable automatic authentication at the command prompt so that you can query the Kusto clusters for MS Learn data.

2. Get the latest monthly data from the MS Learn dashboard:
	1. Navigate to the [dashboard page](https://msit.powerbi.com/groups/9d83d204-82a9-4b36-98f2-a40099093839/reports/3ad7a43c-5334-4086-b762-8b4bdb2741ff/ReportSectionfb7e1b32d2783b56519d?ctid=72f988bf-86f1-41af-91ab-2d7cd011db47).
	2. Select the table at the bottom > Click the three ellipses in the upper right > Export data > Summarized data
	3. Save the module data export with the name "module_stats-latest.csv" in the /data subdirectory
	4. Save the learning path export with the name "learning_path_stats-latest.csv" in the /data subdirectory
	
3. Add/remove certification Exam pages to the list in the portfolio.config file.
4. Run the CLI command "az login" to login to Azure. Confirm the account in the browser window that opens.
4. Execute the driver script by typing "python ms_learn_crawler.py"
