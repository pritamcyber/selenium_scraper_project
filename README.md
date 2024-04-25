The selenium_scraper script is designed to scrape web pages for links, image links, paragraphs, and body text. 
It generates an Excel file for each link specified in a DOCX file. 
Please note that currently, the script only works with DOCX files and extracts data only from the links provided within the DOCX file. 
Future updates may expand its functionality to support additional file types and enhance link handling.

Environment Setup:
Ensure you have Python installed on your system.
Install the required dependencies listed in the requirements.txt file using pip install -r requirements.txt.
Input Data:
Prepare a DOCX file containing the links you want to scrape. Ensure each link is formatted correctly and placed within the document.
Running the Script:
Execute the selenium_scraper.py script.
Pass the path to the DOCX file containing the links as a command-line argument.


The script will generate an Excel file for each link provided in the DOCX file.
Each Excel file will contain the extracted data, including links, image links, paragraphs, and body text.

Output:
The script will generate an Excel file for each link provided in the DOCX file.
Each Excel file will contain the extracted data, including links, image links, paragraphs, and body text.


Important Notes:

The script currently only supports DOCX files for specifying links.
Ensure the links within the DOCX file are properly formatted and accessible.
Future updates may enhance functionality and support for additional file types.
Use responsibly and adhere to website scraping guidelines and terms of service.
Contributing:
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

Disclaimer:
This script is provided as-is with no warranties. Use it responsibly and respect the terms of service of the websites you scrape.
