from bs4 import BeautifulSoup
import requests
from splitter import text_to_doc_splitter

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and clean the text content
        text = '\n'.join(
            section.get_text(separator='\n', strip=True) 
            for section in soup.findAll('div', {'class': 'description__text'})
        )
        
        # Split text into document format using the provided text_to_doc_splitter function
        document = text_to_doc_splitter(text)

        return document
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Test the function with your LinkedIn job URL
url = 'https://www.linkedin.com/jobs/view/3961701899/?alternateChannel=search&refId=1mEYxhdBPlDvxEKQCuDTHQ%3D%3D&trackingId=63WyeKH5AgkhI8h0EAqplg%3D%3D'
document = extract_text_from_url(url)

# Print the document to see the extracted content
print("Document:", document)
