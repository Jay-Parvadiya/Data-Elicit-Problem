# Data-Elicit-Problem

Problem Statement
Write a code that reads the provided CSV file and converts it into JSON format. Further ingest that
JSON Data into Splunk Enterprise platform.
CSV: https://dataelicitinterviewdata.s3.ap-south-1.amazonaws.com/prices.csv
Description & Submissions
1) Download and install Splunk Enterprise on your local machine.
2) Write python code (Any other languages allowed) to convert CSV into JSON format. Consider
the first line in CSV as header.
3) Create a HEC token (HTTP Event Collector) in Splunk UI.
4) Ingest the converted JSON data using your code Splunk via HEC.
5) Submit the screenshot of ingested data on Splunk along with the code. (Copy your code in
text/word/pdf file and then share it in the mail.)

Correlate sales data with product information and prepare a chart that displays per day total
sales of each product.
Panel 1:
1) Write a Splunk query to find the count of total products.
2) Create a dashboard and save the panel “Total Products” as shown in the output below.

Panel 2:
1) Download the vendor_sales log file and ingest the data in Splunk.
https://dataelicitinterviewdata.s3.ap-south-1.amazonaws.com/vendor_sales.log
2) Find top 5 Vendors from the vendor_sales logs and create a piechart and add it in the existing
dashboard.
Panel 3:
1) Write a Splunk query to correlate the sales data with product data ingested in the first
submission.
2) Create a timechart that displays per day total sales of each product and add it to the existing
dashboard.

Submit the source code of dashboard and the output screenshot.
(To get the source code > Click Edit on top-right of dashboard > Click on Source button and copy the
XML code.)


# Output: 
![Screenshot 2025-07-02 212536](https://github.com/user-attachments/assets/0107feb4-0bba-4c82-bda9-46d106fc702f)
